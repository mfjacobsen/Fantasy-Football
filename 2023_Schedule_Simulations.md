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

Unfortunately, this analysis is only for the regular season. The reason I can't
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

|   Rank | Username           |   Points For |   Points Against | Record   |
|-------:|:-------------------|-------------:|-----------------:|:---------|
|      1 | pacc               |      2008.96 |          1765.22 | 9-5      |
|      2 | thezirconisdragon  |      2000.73 |          1895.99 | 9-5      |
|      3 | herbietime         |      2114.47 |          1990.59 | 8-6      |
|      4 | alecwilson         |      2107.20 |          1854.36 | 8-6      |
|      5 | empireyikesback    |      1798.42 |          1662.93 | 8-6      |
|      6 | burgertownthicnred |      1769.67 |          1778.89 | 8-6      |
|      7 | therealfergus      |      1814.81 |          2027.19 | 6-8      |
|      8 | mackjyers21        |      1730.29 |          1818.54 | 6-8      |
|      9 | shakylegs          |      1650.25 |          1838.57 | 6-8      |
|     10 | tonygordzilla22    |      1625.72 |          1735.48 | 6-8      |
|     11 | black8yellownation |      1495.60 |          1615.37 | 6-8      |
|     12 | namebrant          |      1645.83 |          1778.82 | 4-10     |

### 10 Million Simulations

I simulated 10 million possible schedules, and recorded the final season
rankings for each. Below are the results. These are the raw counts from the 
10 million simulations. For example, herbietime placed first in 5,191,110 
simulations, whereas tonygordzilla22 placed first only 36 times.

| username           |       1 |       2 |       3 |       4 |       5 |       6 |       7 |       8 |       9 |      10 |      11 |      12 |
|:-------------------|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|--------:|
| herbietime         | 5191110 | 2466258 | 1263125 |  638384 |  281700 |  108655 |   38014 |   10242 |    2192 |     300 |      20 |       0 |
| thezirconisdragon  | 2074697 | 2171155 | 2116925 | 1910464 |  908055 |  432684 |  211870 |  104144 |   44943 |   18354 |    6032 |     677 |
| pacc               | 1301049 | 2361512 | 2587268 | 2017290 |  952164 |  439508 |  200778 |   89029 |   34619 |   12850 |    3618 |     315 |
| alecwilson         | 1209358 | 2309450 | 2423388 | 2001998 | 1123941 |  556264 |  243843 |   95928 |   28520 |    6519 |     771 |      20 |
| empireyikesback    |  100340 |  300327 |  652351 | 1275076 | 2215778 | 2300439 | 1551716 |  906495 |  443471 |  187408 |   59043 |    7556 |
| therealfergus      |   79027 |  231050 |  524234 | 1112273 | 2232044 | 2101218 | 1603096 | 1077066 |  611100 |  301181 |  112416 |   15295 |
| mackjyers21        |   29770 |   97803 |  239929 |  529663 | 1024433 | 1574398 | 2006172 | 2136204 | 1266054 |  688986 |  334023 |   72565 |
| burgertownthicnred |   12441 |   50768 |  148201 |  374902 |  863380 | 1594773 | 2346878 | 2212003 | 1351781 |  705852 |  291124 |   47897 |
| shakylegs          |    1832 |    8321 |   27895 |   79198 |  204288 |  428686 |  818694 | 1486333 | 2669906 | 2335301 | 1514670 |  424876 |
| namebrant          |     340 |    2944 |   13802 |   46325 |  136744 |  302059 |  591635 | 1072327 | 1910769 | 2822535 | 2315996 |  784524 |
| tonygordzilla22    |      36 |     403 |    2825 |   14000 |   54992 |  151888 |  361161 |  736419 | 1446341 | 2425927 | 3904713 |  901295 |
| black8yellownation |       0 |       9 |      57 |     427 |    2481 |    9428 |   26143 |   73810 |  190304 |  494787 | 1457574 | 7744980 |


