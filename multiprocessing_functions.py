import random
import numpy as np
import pandas as pd
from tqdm import tqdm

def generate_schedule(all_weeks, similar_weeks):
    """Generates a 14 week season schedule for an 12 team leage. Each team plays
    all other teams once in the first 11 weeks. The first 3 weeks are repeated
    for the last 3 weeks.

    Returns:
        list: A length 14 list of length 6 tuples containing the matchup ids for
    each week.
    """
    weeks = set(all_weeks)
    schedule = []

    # Recursively fills the weekly schedule at random
    def pick_week(weeks):
        if len(schedule) == 11:
            return
        else:
            tuple_weeks = tuple(weeks)
            choice = random.choice(tuple_weeks)
            schedule.append(choice)
            weeks -= similar_weeks[choice]
            pick_week(weeks)
    
    # The above method has about a 70% success rate to pick a valid yearly 
    # schedule. This while loop will continue until a valid schedule is picked.
    while len(schedule) != 11:
        try:
            pick_week(weeks)
        except IndexError:
            weeks = set(all_weeks)
            schedule = []

    # Adds the first three weeks of the schedule to the end to finish the 14
    # week season
    schedule += schedule[:3]

    return(np.array(schedule))

def get_ranking(schedule, owners, matchup_to_roster_id, matchups, owners_points):
    """Gets the regular season rankings of the team given a season schedule

    Args:
        schedule (list): A list of tuples containing the matchup ids for each
        week.

    Returns:
        pd.Series: a pandas series indexed by username containing the rank of 
        each team at the end of the season.
    """

    standings = {username: pd.Series([0,0,0], index=["win", "loss", "draw"]) 
             for username in owners["username"]}

    # Records the outcome of a single match in the standings dictionary
    def record_outcome(week_num, matchup_id):

        team1, team2 = matchup_to_roster_id[matchup_id]

        df = (
            matchups[(matchups["week"] == week_num) 
                     & ((matchups["roster_id"] == team1) 
                        | (matchups["roster_id"] == team2))]
            )
        
        if df["team_points"].nunique() == 1:
            standings[df.iloc[0, 1]]["draw"] += 1
            standings[df.iloc[1, 1]]["draw"] += 1
        
        else:
            max_username = df.loc[df["team_points"].idxmax(), "username"]
            min_username = df.loc[df["team_points"].idxmin(), "username"]

            standings[max_username]["win"] += 1
            standings[min_username]["loss"] += 1
        
    # Records the outcome of all matches in the standings
    for week_num in range(1, len(schedule) + 1):
        for matchup_id in schedule[week_num - 1]:
            record_outcome(week_num, matchup_id)

    # Determines the team ranks of the season
    df = (pd.DataFrame.from_dict(standings, orient='index')
          .merge(owners_points, left_index = True, right_index= True)
          .sort_values(by=["win", "team_points"], ascending = False)
          .assign(rank = np.arange(1,13)))

    return df["rank"]

def simulate_schedules(all_weeks, similar_weeks, owners, matchup_to_roster_id, matchups, owners_points, total_records, ranking_counts, num_sims):

    temp_records = {username: np.zeros(12,dtype=int) for username in 
                    owners["username"]}
    temp_ranking = {}

    for i in range(num_sims):

        ranks = get_ranking(generate_schedule(all_weeks, similar_weeks), owners, matchup_to_roster_id, matchups, owners_points)

        # Store each user's rank in the temporary records dict
        for username, rank in ranks.items():
            temp_records[username][rank-1] += 1

        # Stores the rank order in the temporary ranking dic
        ranks_order = tuple(ranks.index)

        if ranks_order in temp_ranking:
            temp_ranking[ranks_order] += 1
        else:
            temp_ranking[ranks_order] = 1

    for username, record in temp_records.items():
        for i in range(12):
            total_records[username][i] += record[i]

    for rank_order, count in temp_ranking.items():
        if rank_order in ranking_counts:
            ranking_counts[rank_order] += count
        else:
            ranking_counts[rank_order] = count


