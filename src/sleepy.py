import requests
import pandas as pd
import numpy as np
import json
import random


def get_user_data(username):
    #Works for username or user_id
    return requests.get(f'https://api.sleeper.app/v1/user/{username}').json()

def get_league_ids(user_id, year):
    leagues = requests.get(f'https://api.sleeper.app/v1/user/{user_id}/leagues/nfl/{year}').json()
    ids = [league["league_id"] for league in leagues]
    return ids

def get_leage(league_id):
    return requests.get(f'https://api.sleeper.app/v1/league/{league_id}').json()

def get_owners(league_id):

    rosters = requests.get(f'https://api.sleeper.app/v1/league/{league_id}/rosters').json()

    rosters = pd.DataFrame(rosters)

    user_ids = rosters["owner_id"]
    users = [get_user_data(user_id) for user_id in user_ids]
    users = pd.DataFrame(users)

    settings = pd.DataFrame(list((rosters["settings"])))
    rosters = rosters.merge(settings, left_index=True,  right_index=True).drop(columns = "settings")

    owners = (users
              .merge(rosters, left_on = 'user_id', right_on = 'owner_id')
              .dropna(how = 'all', axis=1))
    
    return owners

def load_player_data(filename = 'players.json', include_teams = False):
    """Loads player data from a json file. Default behavior will load data from 
    the file saved by the function get_player_data()

    Args:
        filename (str, optional): The filename to load. Defaults to 
        'players.json'.

    Returns:
        dict: A dictionary containing all NFL player data.
    """
    with open('players.json', 'r') as json_file:
        players = json.load(json_file)

    players, teams = _clean_players(players)
    
    if not include_teams:
        return players
    else:
        return players, teams 

def get_player_data(save = True, filename = 'players.json', include_teams = False):
    """Gets all NFL Player data from the Sleeper API. Only call this once per 
    day as requested by Sleeper. The file is ~ 12MB. Automatically saves the 
    data in a json file named 'players.json'

    Args:
        save (bool, optional): If False, a file of the player data will not be 
        saved. Defaults to True.

        filename (str, optional): The filename to save the player data. Defaults
        to 'players.json'.

        include_teams (bool, optional): If Ture, includes returns team defenses
        as a second output

    Returns:
        dict: A dictionary containing all NFL player data. If include_teams is 
        True, also outputs a pandas dataframe containg team defense data.
    """
    response = requests.get(f'https://api.sleeper.app/v1/players/nfl')  

    players = response.json()

    if save:
        with open(filename, 'w') as json_file:
            json.dump(players, json_file)

    players, teams = _clean_players(players)
    
    if not include_teams:
        return players
    else:
        return players, teams  

def get_matchups(league_id, week = 1, season = False):
    """Gets league matchup data from a specifc week or entire season

    Args:
        league_id (int, str): The Sleeper leage identification number
        week (int, optional): The week of matchups that should be returned.
            Defaults to 1.
        season (bool, optional): If True, returns matchup data from the 
            entire season. Defaults to False.

    Returns:
        pandas data frame: A dataframe containing the requested matchup data
    """

    def request_matchup(week):
        """Requests the matchups from a single week from Sleeper API

        Args:
            week (int, str): The week to requests matchups

        Returns:
            list: A list of dictionaries, each dictionary corresponds to a
            single row in the eventual dataframe
        """
        url = f'https://api.sleeper.app/v1/league/{league_id}/matchups/{week}'
        matchups_raw = requests.get(url).json()
        return [{"week": week,
                 "player": player,
                 "player_points": team["players_points"][player],
                 "starter": player in team["starters"],
                 "matchup_id": team["matchup_id"],
                 "roster_id": team["roster_id"],
                 "team_points": team["points"],
                 "custom_points": team["custom_points"]}
                 for team in matchups_raw for player in team["players"]]
    
    if season:
        matchups = []
        for week in range(1,18):
            matchups += request_matchup(week) 
    else:
        matchups = request_matchup(week)
        
    return pd.DataFrame(matchups)

def _clean_players(players):

    teams = pd.DataFrame({key: players[key] for key in players.keys() if key.isalpha()}).transpose()
    players = pd.DataFrame({key: players[key] for key in players.keys() if key.isnumeric()}).transpose()

    players = (players
               .assign(years_exp = players["years_exp"].apply(_clean_int))
               .assign(weight = players["weight"].apply(_clean_int))
               .assign(age = players["age"].apply(_clean_int))
               .assign(depth_chart_order = players["depth_chart_order"]
                                           .apply(_clean_int))
               .assign(height = players["height"].apply(_clean_height))
               .assign(birth_date = pd.to_datetime(players["birth_date"], 
                                                   format = '%Y-%m-%d')))
    
    return players, teams

def _clean_int(x):
    if x not in ["", "0", None]:
        return int(x) 
    else:
        return None
    
def _clean_height(height):
    if height in ["", "0", None]:
        return None
    try:
        height = int(height)
    except:
        height = height.strip("\"").split('\'')
        height = int(height[0]) * 12 + int(height[1])

    if height > 96 or height < 36:
        return None
    else:
        return height