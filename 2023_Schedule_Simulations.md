<style>
.dataframe {
  overflow-x: auto; /* Enable horizontal scrolling if needed */
}

table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

/* Alternating row colors */
tr:nth-child(even) {
  background-color: #f2f2f2; /* Light gray background color */
}
tr:nth-child(odd) {
  background-color: #ffffff; /* White background color */
}

/* Sticky column style */
th:first-child,
td:first-child {
  position: sticky;
  left: 0;
  z-index: 1;
  background-color: #ffffff;
}
</style>

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

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Username</th>
      <th>Points For</th>
      <th>Points Against</th>
      <th>Record</th>
    </tr>
    <tr>
      <th>Rank</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>pacc</td>
      <td>2008.96</td>
      <td>1765.22</td>
      <td>9-5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>thezirconisdragon</td>
      <td>2000.73</td>
      <td>1895.99</td>
      <td>9-5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>herbietime</td>
      <td>2114.47</td>
      <td>1990.59</td>
      <td>8-6</td>
    </tr>
    <tr>
      <th>4</th>
      <td>alecwilson</td>
      <td>2107.20</td>
      <td>1854.36</td>
      <td>8-6</td>
    </tr>
    <tr>
      <th>5</th>
      <td>empireyikesback</td>
      <td>1798.42</td>
      <td>1662.93</td>
      <td>8-6</td>
    </tr>
    <tr>
      <th>6</th>
      <td>burgertownthicnred</td>
      <td>1769.67</td>
      <td>1778.89</td>
      <td>8-6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>therealfergus</td>
      <td>1814.81</td>
      <td>2027.19</td>
      <td>6-8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>mackjyers21</td>
      <td>1730.29</td>
      <td>1818.54</td>
      <td>6-8</td>
    </tr>
    <tr>
      <th>9</th>
      <td>shakylegs</td>
      <td>1650.25</td>
      <td>1838.57</td>
      <td>6-8</td>
    </tr>
    <tr>
      <th>10</th>
      <td>tonygordzilla22</td>
      <td>1625.72</td>
      <td>1735.48</td>
      <td>6-8</td>
    </tr>
    <tr>
      <th>11</th>
      <td>black8yellownation</td>
      <td>1495.60</td>
      <td>1615.37</td>
      <td>6-8</td>
    </tr>
    <tr>
      <th>12</th>
      <td>namebrant</td>
      <td>1645.83</td>
      <td>1778.82</td>
      <td>4-10</td>
    </tr>
  </tbody>
</table>

### 10 Million Simulations

I simulated 10 million possible schedules, and recorded the final season
rankings for each. Below are the results. These are the raw counts from the 
10 million simulations. For example, herbietime placed first in 5,191,110 
simulations, whereas tonygordzilla22 placed first only 36 times.

<table border="1" class="dataframe_stickycol">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
      <th>12</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>herbietime</th>
      <td>5191110</td>
      <td>2466258</td>
      <td>1263125</td>
      <td>638384</td>
      <td>281700</td>
      <td>108655</td>
      <td>38014</td>
      <td>10242</td>
      <td>2192</td>
      <td>300</td>
      <td>20</td>
      <td>0</td>
    </tr>
    <tr>
      <th>thezirconisdragon</th>
      <td>2074697</td>
      <td>2171155</td>
      <td>2116925</td>
      <td>1910464</td>
      <td>908055</td>
      <td>432684</td>
      <td>211870</td>
      <td>104144</td>
      <td>44943</td>
      <td>18354</td>
      <td>6032</td>
      <td>677</td>
    </tr>
    <tr>
      <th>pacc</th>
      <td>1301049</td>
      <td>2361512</td>
      <td>2587268</td>
      <td>2017290</td>
      <td>952164</td>
      <td>439508</td>
      <td>200778</td>
      <td>89029</td>
      <td>34619</td>
      <td>12850</td>
      <td>3618</td>
      <td>315</td>
    </tr>
    <tr>
      <th>alecwilson</th>
      <td>1209358</td>
      <td>2309450</td>
      <td>2423388</td>
      <td>2001998</td>
      <td>1123941</td>
      <td>556264</td>
      <td>243843</td>
      <td>95928</td>
      <td>28520</td>
      <td>6519</td>
      <td>771</td>
      <td>20</td>
    </tr>
    <tr>
      <th>empireyikesback</th>
      <td>100340</td>
      <td>300327</td>
      <td>652351</td>
      <td>1275076</td>
      <td>2215778</td>
      <td>2300439</td>
      <td>1551716</td>
      <td>906495</td>
      <td>443471</td>
      <td>187408</td>
      <td>59043</td>
      <td>7556</td>
    </tr>
    <tr>
      <th>therealfergus</th>
      <td>79027</td>
      <td>231050</td>
      <td>524234</td>
      <td>1112273</td>
      <td>2232044</td>
      <td>2101218</td>
      <td>1603096</td>
      <td>1077066</td>
      <td>611100</td>
      <td>301181</td>
      <td>112416</td>
      <td>15295</td>
    </tr>
    <tr>
      <th>mackjyers21</th>
      <td>29770</td>
      <td>97803</td>
      <td>239929</td>
      <td>529663</td>
      <td>1024433</td>
      <td>1574398</td>
      <td>2006172</td>
      <td>2136204</td>
      <td>1266054</td>
      <td>688986</td>
      <td>334023</td>
      <td>72565</td>
    </tr>
    <tr>
      <th>burgertownthicnred</th>
      <td>12441</td>
      <td>50768</td>
      <td>148201</td>
      <td>374902</td>
      <td>863380</td>
      <td>1594773</td>
      <td>2346878</td>
      <td>2212003</td>
      <td>1351781</td>
      <td>705852</td>
      <td>291124</td>
      <td>47897</td>
    </tr>
    <tr>
      <th>shakylegs</th>
      <td>1832</td>
      <td>8321</td>
      <td>27895</td>
      <td>79198</td>
      <td>204288</td>
      <td>428686</td>
      <td>818694</td>
      <td>1486333</td>
      <td>2669906</td>
      <td>2335301</td>
      <td>1514670</td>
      <td>424876</td>
    </tr>
    <tr>
      <th>namebrant</th>
      <td>340</td>
      <td>2944</td>
      <td>13802</td>
      <td>46325</td>
      <td>136744</td>
      <td>302059</td>
      <td>591635</td>
      <td>1072327</td>
      <td>1910769</td>
      <td>2822535</td>
      <td>2315996</td>
      <td>784524</td>
    </tr>
    <tr>
      <th>tonygordzilla22</th>
      <td>36</td>
      <td>403</td>
      <td>2825</td>
      <td>14000</td>
      <td>54992</td>
      <td>151888</td>
      <td>361161</td>
      <td>736419</td>
      <td>1446341</td>
      <td>2425927</td>
      <td>3904713</td>
      <td>901295</td>
    </tr>
    <tr>
      <th>black8yellownation</th>
      <td>0</td>
      <td>9</td>
      <td>57</td>
      <td>427</td>
      <td>2481</td>
      <td>9428</td>
      <td>26143</td>
      <td>73810</td>
      <td>190304</td>
      <td>494787</td>
      <td>1457574</td>
      <td>7744980</td>
    </tr>
  </tbody>
</table>


