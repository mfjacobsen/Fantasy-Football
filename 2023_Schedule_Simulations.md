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

Some questions we'll answer:

* What were the chances of team X placing where they did last season?
* What were the chances of each team placing first/last for the season?
* What were each team's chances of making the playoffs?

Lastly, we'll look at some interesting and unlikley rankings that could have 
occured.

### Just The Regular Season

Unofortunately, this analysis is only for the regular season. The reason I can't
include the playoffs is because of the first-round byes that four teams have. 
These byes mean that I don't have team point totals for four teams from week
fifteen. When we simulate a new schedule, those four teams that had byes might
not have them anymore, but since they didn't play that week, we can't determine 
the game outcome. 

If you guys enjoy this analysis then next year I can include the playoffs. We'll
just have to have the four teams with first-round byes tell me the players they
would roster for that week if they didn't have a bye.

### Schedule Generation

At the start of the season Sleeper randomly generates the season schedules. The 
regular season is fourteen weeks long. In the first eleven weeks, each team 
plays every other team once. Then, the first three weeks are repeated for the
last three weeks. 

Ideally, we could generate every possible schedule, which would give us an exact
distribution of each owner's rankings. The exact number of possible schedules is 
a tricky combinatorics problem, but I've estimated it to be somewhere around 
10^25 (a 1 with 25 zeros after it). With this many possible schedules, we can't 
generate them all, but we can generate a very large number that will give us 
a fairly accurate picture of the 'true' distribution. 

### Season Results

It's been a few months since the season ended, so as a reminder, here are the 
final standings from the regular season.

'|   rank | username           |   points_for |   points_against | record   |\n|-------:|:-------------------|-------------:|-----------------:|:---------|\n|      1 | pacc               |      2008.96 |          1765.22 | 9-5      |\n|      2 | thezirconisdragon  |      2000.73 |          1895.99 | 9-5      |\n|      3 | herbietime         |      2114.47 |          1990.59 | 8-6      |\n|      4 | alecwilson         |      2107.2  |          1854.36 | 8-6      |\n|      5 | empireyikesback    |      1798.42 |          1662.93 | 8-6      |\n|      6 | burgertownthicnred |      1769.67 |          1778.89 | 8-6      |\n|      7 | therealfergus      |      1814.81 |          2027.19 | 6-8      |\n|      8 | mackjyers21        |      1730.29 |          1818.54 | 6-8      |\n|      9 | shakylegs          |      1650.25 |          1838.57 | 6-8      |\n|     10 | tonygordzilla22    |      1625.72 |          1735.48 | 6-8      |\n|     11 | black8yellownation |      1495.6  |          1615.37 | 6-8      |\n|     12 | namebrant          |      1645.83 |          1778.82 | 4-10     |'
