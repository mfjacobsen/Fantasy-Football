# 2023 Simulated Schedules

### Introduction

With the 2024 season coming up, let's look back at last season and see how 
different the outcome could have been if the schedule had been different. 

Every week, each team 'plays' another team in the league. However, there is no 
real interaction between the two teams. Each team tries to score the most points
they can, independent of their opponent. That is, Team A's owner will roster the
players he thinks will get the most points that week, regardless of whether he
is playing Team B, C, or D. 

Using this premise we'll perform the following workflow:

* Generate a new season schedule
* Use the number of points each team actually scored in each week to determine
the outcome of every game
* Calculate the season standings from the new schedule

### Schedule Generation

At the start of the season Sleeper randomly generates the season schedules. The 
regular season is fourteen weeks long. In the first eleven weeks, each team 
plays every other team once. Then the first three weeks are repeated for the
last three weeks. Ideally, we could generate every possible schedule, then The exact number of possible schedules is a tricky 
combinatorics problem, but I've estimated it to be somewhere around 10^25 (a 1 
with 25 zeros after it). 

With this many possible schedules, we can't generate
each possible schedule and get exact 
