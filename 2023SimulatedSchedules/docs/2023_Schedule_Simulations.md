<style>
.dataframe {
  overflow-x: auto; /* Enable horizontal scrolling if needed */
}

table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
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
  background-color: #ffffff; /* Background color for sticky column */
}

/* Alternating row colors including sticky column */
tr:nth-child(even) th:first-child,
tr:nth-child(odd) th:first-child,
tr:nth-child(even) td:first-child,
tr:nth-child(odd) td:first-child {
  background-color: inherit; /* Inherit row background color for sticky column */
}
</style>

# 2023 Simulated Schedules

See the [2022 Simulated Schedules](../../2022SimulatedSchedules/docs/2022_Schedule_Simulations.md).

## Introduction

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
      <th>Rank</th>
      <th>Username</th>
      <th>Points For</th>
      <th>Points Against</th>
      <th>Record</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>pacc</td>
      <td>2008.96</td>
      <td>1765.22</td>
      <td>9-5</td>
    </tr>
    <tr>
      <td>2</td>
      <td>thezirconisdragon</td>
      <td>2000.73</td>
      <td>1895.99</td>
      <td>9-5</td>
    </tr>
    <tr>
      <td>3</td>
      <td>herbietime</td>
      <td>2114.47</td>
      <td>1990.59</td>
      <td>8-6</td>
    </tr>
    <tr>
      <td>4</td>
      <td>alecwilson</td>
      <td>2107.20</td>
      <td>1854.36</td>
      <td>8-6</td>
    </tr>
    <tr>
      <td>5</td>
      <td>empireyikesback</td>
      <td>1798.42</td>
      <td>1662.93</td>
      <td>8-6</td>
    </tr>
    <tr>
      <td>6</td>
      <td>burgertownthicnred</td>
      <td>1769.67</td>
      <td>1778.89</td>
      <td>8-6</td>
    </tr>
    <tr>
      <td>7</td>
      <td>therealfergus</td>
      <td>1814.81</td>
      <td>2027.19</td>
      <td>6-8</td>
    </tr>
    <tr>
      <td>8</td>
      <td>mackjyers21</td>
      <td>1730.29</td>
      <td>1818.54</td>
      <td>6-8</td>
    </tr>
    <tr>
      <td>9</td>
      <td>shakylegs</td>
      <td>1650.25</td>
      <td>1838.57</td>
      <td>6-8</td>
    </tr>
    <tr>
      <td>10</td>
      <td>tonygordzilla22</td>
      <td>1625.72</td>
      <td>1735.48</td>
      <td>6-8</td>
    </tr>
    <tr>
      <td>11</td>
      <td>black8yellownation</td>
      <td>1495.60</td>
      <td>1615.37</td>
      <td>6-8</td>
    </tr>
    <tr>
      <td>12</td>
      <td>namebrant</td>
      <td>1645.83</td>
      <td>1778.82</td>
      <td>4-10</td>
    </tr>
  </tbody>
</table>

## 10 Million Simulations

I simulated 10 million possible schedules, and recorded the final season
rankings for each. Lets look at some of the results.

### Ranking Counts
These are the raw counts from the 10 million simulations. For example, 
herbietime placed first in 5,191,110 simulations, whereas tonygordzilla22 placed
 first only 36 times. Some interesting things to note:

 * Every team except herbietime could have placed last
 * Every team except blackandyelllownation could have placed first

There could be schedules were herbietime placed last or blackandyellownation
placed first. However, they didn't occur in the 10 million simulations performed
here.

<table border="1" class="dataframe">
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

### Ranking Percentage

This is the same table as above, however, now it shows as a percentage. I've
also highlighted the ranking that each team actually had in the 2023 season.
Now, we can see the herbietime had about a 51.9% chance of taking first place, 
a 24.6% chance of taking second, and a 12.6% chance of taking third, which he
did. 

* The first column is each team's chance of placing first
* The last column is each team's chance of placing last

<style type="text/css">
#T_8d0e4_row0_col2, #T_8d0e4_row1_col1, #T_8d0e4_row2_col0, #T_8d0e4_row3_col3, #T_8d0e4_row4_col4, #T_8d0e4_row5_col6, #T_8d0e4_row6_col7, #T_8d0e4_row7_col5, #T_8d0e4_row8_col8, #T_8d0e4_row9_col11, #T_8d0e4_row10_col9, #T_8d0e4_row11_col10 {
  color: red;
}
</style>
<table id="T_8d0e4" border="1" class="dataframe">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_8d0e4_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_8d0e4_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_8d0e4_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_8d0e4_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_8d0e4_level0_col4" class="col_heading level0 col4" >5</th>
      <th id="T_8d0e4_level0_col5" class="col_heading level0 col5" >6</th>
      <th id="T_8d0e4_level0_col6" class="col_heading level0 col6" >7</th>
      <th id="T_8d0e4_level0_col7" class="col_heading level0 col7" >8</th>
      <th id="T_8d0e4_level0_col8" class="col_heading level0 col8" >9</th>
      <th id="T_8d0e4_level0_col9" class="col_heading level0 col9" >10</th>
      <th id="T_8d0e4_level0_col10" class="col_heading level0 col10" >11</th>
      <th id="T_8d0e4_level0_col11" class="col_heading level0 col11" >12</th>
    </tr>
    <tr>
      <th class="index_name level0" >username</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
      <th class="blank col7" >&nbsp;</th>
      <th class="blank col8" >&nbsp;</th>
      <th class="blank col9" >&nbsp;</th>
      <th class="blank col10" >&nbsp;</th>
      <th class="blank col11" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_8d0e4_level0_row0" class="row_heading level0 row0" >herbietime</th>
      <td id="T_8d0e4_row0_col0" class="data row0 col0" >51.9111</td>
      <td id="T_8d0e4_row0_col1" class="data row0 col1" >24.66258</td>
      <td id="T_8d0e4_row0_col2" class="data row0 col2" >12.63125</td>
      <td id="T_8d0e4_row0_col3" class="data row0 col3" >6.38384</td>
      <td id="T_8d0e4_row0_col4" class="data row0 col4" >2.817</td>
      <td id="T_8d0e4_row0_col5" class="data row0 col5" >1.08655</td>
      <td id="T_8d0e4_row0_col6" class="data row0 col6" >0.38014</td>
      <td id="T_8d0e4_row0_col7" class="data row0 col7" >0.10242</td>
      <td id="T_8d0e4_row0_col8" class="data row0 col8" >0.02192</td>
      <td id="T_8d0e4_row0_col9" class="data row0 col9" >0.003</td>
      <td id="T_8d0e4_row0_col10" class="data row0 col10" >0.0002</td>
      <td id="T_8d0e4_row0_col11" class="data row0 col11" >0.0</td>
    </tr>
    <tr>
      <th id="T_8d0e4_level0_row1" class="row_heading level0 row1" >thezirconisdragon</th>
      <td id="T_8d0e4_row1_col0" class="data row1 col0" >20.74697</td>
      <td id="T_8d0e4_row1_col1" class="data row1 col1" >21.71155</td>
      <td id="T_8d0e4_row1_col2" class="data row1 col2" >21.16925</td>
      <td id="T_8d0e4_row1_col3" class="data row1 col3" >19.10464</td>
      <td id="T_8d0e4_row1_col4" class="data row1 col4" >9.08055</td>
      <td id="T_8d0e4_row1_col5" class="data row1 col5" >4.32684</td>
      <td id="T_8d0e4_row1_col6" class="data row1 col6" >2.1187</td>
      <td id="T_8d0e4_row1_col7" class="data row1 col7" >1.04144</td>
      <td id="T_8d0e4_row1_col8" class="data row1 col8" >0.44943</td>
      <td id="T_8d0e4_row1_col9" class="data row1 col9" >0.18354</td>
      <td id="T_8d0e4_row1_col10" class="data row1 col10" >0.06032</td>
      <td id="T_8d0e4_row1_col11" class="data row1 col11" >0.00677</td>
    </tr>
    <tr>
      <th id="T_8d0e4_level0_row2" class="row_heading level0 row2" >pacc</th>
      <td id="T_8d0e4_row2_col0" class="data row2 col0" >13.01049</td>
      <td id="T_8d0e4_row2_col1" class="data row2 col1" >23.61512</td>
      <td id="T_8d0e4_row2_col2" class="data row2 col2" >25.87268</td>
      <td id="T_8d0e4_row2_col3" class="data row2 col3" >20.1729</td>
      <td id="T_8d0e4_row2_col4" class="data row2 col4" >9.52164</td>
      <td id="T_8d0e4_row2_col5" class="data row2 col5" >4.39508</td>
      <td id="T_8d0e4_row2_col6" class="data row2 col6" >2.00778</td>
      <td id="T_8d0e4_row2_col7" class="data row2 col7" >0.89029</td>
      <td id="T_8d0e4_row2_col8" class="data row2 col8" >0.34619</td>
      <td id="T_8d0e4_row2_col9" class="data row2 col9" >0.1285</td>
      <td id="T_8d0e4_row2_col10" class="data row2 col10" >0.03618</td>
      <td id="T_8d0e4_row2_col11" class="data row2 col11" >0.00315</td>
    </tr>
    <tr>
      <th id="T_8d0e4_level0_row3" class="row_heading level0 row3" >alecwilson</th>
      <td id="T_8d0e4_row3_col0" class="data row3 col0" >12.09358</td>
      <td id="T_8d0e4_row3_col1" class="data row3 col1" >23.0945</td>
      <td id="T_8d0e4_row3_col2" class="data row3 col2" >24.23388</td>
      <td id="T_8d0e4_row3_col3" class="data row3 col3" >20.01998</td>
      <td id="T_8d0e4_row3_col4" class="data row3 col4" >11.23941</td>
      <td id="T_8d0e4_row3_col5" class="data row3 col5" >5.56264</td>
      <td id="T_8d0e4_row3_col6" class="data row3 col6" >2.43843</td>
      <td id="T_8d0e4_row3_col7" class="data row3 col7" >0.95928</td>
      <td id="T_8d0e4_row3_col8" class="data row3 col8" >0.2852</td>
      <td id="T_8d0e4_row3_col9" class="data row3 col9" >0.06519</td>
      <td id="T_8d0e4_row3_col10" class="data row3 col10" >0.00771</td>
      <td id="T_8d0e4_row3_col11" class="data row3 col11" >0.0002</td>
    </tr>
    <tr>
      <th id="T_8d0e4_level0_row4" class="row_heading level0 row4" >empireyikesback</th>
      <td id="T_8d0e4_row4_col0" class="data row4 col0" >1.0034</td>
      <td id="T_8d0e4_row4_col1" class="data row4 col1" >3.00327</td>
      <td id="T_8d0e4_row4_col2" class="data row4 col2" >6.52351</td>
      <td id="T_8d0e4_row4_col3" class="data row4 col3" >12.75076</td>
      <td id="T_8d0e4_row4_col4" class="data row4 col4" >22.15778</td>
      <td id="T_8d0e4_row4_col5" class="data row4 col5" >23.00439</td>
      <td id="T_8d0e4_row4_col6" class="data row4 col6" >15.51716</td>
      <td id="T_8d0e4_row4_col7" class="data row4 col7" >9.06495</td>
      <td id="T_8d0e4_row4_col8" class="data row4 col8" >4.43471</td>
      <td id="T_8d0e4_row4_col9" class="data row4 col9" >1.87408</td>
      <td id="T_8d0e4_row4_col10" class="data row4 col10" >0.59043</td>
      <td id="T_8d0e4_row4_col11" class="data row4 col11" >0.07556</td>
    </tr>
    <tr>
      <th id="T_8d0e4_level0_row5" class="row_heading level0 row5" >therealfergus</th>
      <td id="T_8d0e4_row5_col0" class="data row5 col0" >0.79027</td>
      <td id="T_8d0e4_row5_col1" class="data row5 col1" >2.3105</td>
      <td id="T_8d0e4_row5_col2" class="data row5 col2" >5.24234</td>
      <td id="T_8d0e4_row5_col3" class="data row5 col3" >11.12273</td>
      <td id="T_8d0e4_row5_col4" class="data row5 col4" >22.32044</td>
      <td id="T_8d0e4_row5_col5" class="data row5 col5" >21.01218</td>
      <td id="T_8d0e4_row5_col6" class="data row5 col6" >16.03096</td>
      <td id="T_8d0e4_row5_col7" class="data row5 col7" >10.77066</td>
      <td id="T_8d0e4_row5_col8" class="data row5 col8" >6.111</td>
      <td id="T_8d0e4_row5_col9" class="data row5 col9" >3.01181</td>
      <td id="T_8d0e4_row5_col10" class="data row5 col10" >1.12416</td>
      <td id="T_8d0e4_row5_col11" class="data row5 col11" >0.15295</td>
    </tr>
    <tr>
      <th id="T_8d0e4_level0_row6" class="row_heading level0 row6" >mackjyers21</th>
      <td id="T_8d0e4_row6_col0" class="data row6 col0" >0.2977</td>
      <td id="T_8d0e4_row6_col1" class="data row6 col1" >0.97803</td>
      <td id="T_8d0e4_row6_col2" class="data row6 col2" >2.39929</td>
      <td id="T_8d0e4_row6_col3" class="data row6 col3" >5.29663</td>
      <td id="T_8d0e4_row6_col4" class="data row6 col4" >10.24433</td>
      <td id="T_8d0e4_row6_col5" class="data row6 col5" >15.74398</td>
      <td id="T_8d0e4_row6_col6" class="data row6 col6" >20.06172</td>
      <td id="T_8d0e4_row6_col7" class="data row6 col7" >21.36204</td>
      <td id="T_8d0e4_row6_col8" class="data row6 col8" >12.66054</td>
      <td id="T_8d0e4_row6_col9" class="data row6 col9" >6.88986</td>
      <td id="T_8d0e4_row6_col10" class="data row6 col10" >3.34023</td>
      <td id="T_8d0e4_row6_col11" class="data row6 col11" >0.72565</td>
    </tr>
    <tr>
      <th id="T_8d0e4_level0_row7" class="row_heading level0 row7" >burgertownthicnred</th>
      <td id="T_8d0e4_row7_col0" class="data row7 col0" >0.12441</td>
      <td id="T_8d0e4_row7_col1" class="data row7 col1" >0.50768</td>
      <td id="T_8d0e4_row7_col2" class="data row7 col2" >1.48201</td>
      <td id="T_8d0e4_row7_col3" class="data row7 col3" >3.74902</td>
      <td id="T_8d0e4_row7_col4" class="data row7 col4" >8.6338</td>
      <td id="T_8d0e4_row7_col5" class="data row7 col5" >15.94773</td>
      <td id="T_8d0e4_row7_col6" class="data row7 col6" >23.46878</td>
      <td id="T_8d0e4_row7_col7" class="data row7 col7" >22.12003</td>
      <td id="T_8d0e4_row7_col8" class="data row7 col8" >13.51781</td>
      <td id="T_8d0e4_row7_col9" class="data row7 col9" >7.05852</td>
      <td id="T_8d0e4_row7_col10" class="data row7 col10" >2.91124</td>
      <td id="T_8d0e4_row7_col11" class="data row7 col11" >0.47897</td>
    </tr>
    <tr>
      <th id="T_8d0e4_level0_row8" class="row_heading level0 row8" >shakylegs</th>
      <td id="T_8d0e4_row8_col0" class="data row8 col0" >0.01832</td>
      <td id="T_8d0e4_row8_col1" class="data row8 col1" >0.08321</td>
      <td id="T_8d0e4_row8_col2" class="data row8 col2" >0.27895</td>
      <td id="T_8d0e4_row8_col3" class="data row8 col3" >0.79198</td>
      <td id="T_8d0e4_row8_col4" class="data row8 col4" >2.04288</td>
      <td id="T_8d0e4_row8_col5" class="data row8 col5" >4.28686</td>
      <td id="T_8d0e4_row8_col6" class="data row8 col6" >8.18694</td>
      <td id="T_8d0e4_row8_col7" class="data row8 col7" >14.86333</td>
      <td id="T_8d0e4_row8_col8" class="data row8 col8" >26.69906</td>
      <td id="T_8d0e4_row8_col9" class="data row8 col9" >23.35301</td>
      <td id="T_8d0e4_row8_col10" class="data row8 col10" >15.1467</td>
      <td id="T_8d0e4_row8_col11" class="data row8 col11" >4.24876</td>
    </tr>
    <tr>
      <th id="T_8d0e4_level0_row9" class="row_heading level0 row9" >namebrant</th>
      <td id="T_8d0e4_row9_col0" class="data row9 col0" >0.0034</td>
      <td id="T_8d0e4_row9_col1" class="data row9 col1" >0.02944</td>
      <td id="T_8d0e4_row9_col2" class="data row9 col2" >0.13802</td>
      <td id="T_8d0e4_row9_col3" class="data row9 col3" >0.46325</td>
      <td id="T_8d0e4_row9_col4" class="data row9 col4" >1.36744</td>
      <td id="T_8d0e4_row9_col5" class="data row9 col5" >3.02059</td>
      <td id="T_8d0e4_row9_col6" class="data row9 col6" >5.91635</td>
      <td id="T_8d0e4_row9_col7" class="data row9 col7" >10.72327</td>
      <td id="T_8d0e4_row9_col8" class="data row9 col8" >19.10769</td>
      <td id="T_8d0e4_row9_col9" class="data row9 col9" >28.22535</td>
      <td id="T_8d0e4_row9_col10" class="data row9 col10" >23.15996</td>
      <td id="T_8d0e4_row9_col11" class="data row9 col11" >7.84524</td>
    </tr>
    <tr>
      <th id="T_8d0e4_level0_row10" class="row_heading level0 row10" >tonygordzilla22</th>
      <td id="T_8d0e4_row10_col0" class="data row10 col0" >0.00036</td>
      <td id="T_8d0e4_row10_col1" class="data row10 col1" >0.00403</td>
      <td id="T_8d0e4_row10_col2" class="data row10 col2" >0.02825</td>
      <td id="T_8d0e4_row10_col3" class="data row10 col3" >0.14</td>
      <td id="T_8d0e4_row10_col4" class="data row10 col4" >0.54992</td>
      <td id="T_8d0e4_row10_col5" class="data row10 col5" >1.51888</td>
      <td id="T_8d0e4_row10_col6" class="data row10 col6" >3.61161</td>
      <td id="T_8d0e4_row10_col7" class="data row10 col7" >7.36419</td>
      <td id="T_8d0e4_row10_col8" class="data row10 col8" >14.46341</td>
      <td id="T_8d0e4_row10_col9" class="data row10 col9" >24.25927</td>
      <td id="T_8d0e4_row10_col10" class="data row10 col10" >39.04713</td>
      <td id="T_8d0e4_row10_col11" class="data row10 col11" >9.01295</td>
    </tr>
    <tr>
      <th id="T_8d0e4_level0_row11" class="row_heading level0 row11" >black8yellownation</th>
      <td id="T_8d0e4_row11_col0" class="data row11 col0" >0.0</td>
      <td id="T_8d0e4_row11_col1" class="data row11 col1" >9e-05</td>
      <td id="T_8d0e4_row11_col2" class="data row11 col2" >0.00057</td>
      <td id="T_8d0e4_row11_col3" class="data row11 col3" >0.00427</td>
      <td id="T_8d0e4_row11_col4" class="data row11 col4" >0.02481</td>
      <td id="T_8d0e4_row11_col5" class="data row11 col5" >0.09428</td>
      <td id="T_8d0e4_row11_col6" class="data row11 col6" >0.26143</td>
      <td id="T_8d0e4_row11_col7" class="data row11 col7" >0.7381</td>
      <td id="T_8d0e4_row11_col8" class="data row11 col8" >1.90304</td>
      <td id="T_8d0e4_row11_col9" class="data row11 col9" >4.94787</td>
      <td id="T_8d0e4_row11_col10" class="data row11 col10" >14.57574</td>
      <td id="T_8d0e4_row11_col11" class="data row11 col11" >77.4498</td>
    </tr>
  </tbody>
</table>

### Playoff Chances

This table aggregates the previous one into a more readable format. Each column
is the percentage of simulations where each team placed better, equal, or worse
than their actual ranking for the season. The last column in the percentage of
simulations where they placed in the top six teams. 

Here was can really see who got lucky and unlucky with the schedule. 

* Pacc took first place, a 13% chance, but he had an 87% chance of placing worse
than that.
* Namebrant took last place, a 7.8% chance, but he had a 92.2% chance of placing 
better (better luck next year Brant).
* The playoff teams were about as expected except for burgertownthicnred 
sliding into the playoffs with a 30.5% chance and kicking therealfergus to the
losers bracket despite his 62.8% chance.

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Rank</th>
      <th>Username</th>
      <th>Better</th>
      <th>Equal</th>
      <th>Worse</th>
      <th>Playoff</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>pacc</td>
      <td>0.00</td>
      <td>13.01</td>
      <td>86.99</td>
      <td>96.59</td>
    </tr>
    <tr>
      <td>2</td>
      <td>thezirconisdragon</td>
      <td>20.75</td>
      <td>21.71</td>
      <td>57.54</td>
      <td>96.14</td>
    </tr>
    <tr>
      <td>3</td>
      <td>herbietime</td>
      <td>76.57</td>
      <td>12.63</td>
      <td>10.80</td>
      <td>99.49</td>
    </tr>
    <tr>
      <td>4</td>
      <td>alecwilson</td>
      <td>59.42</td>
      <td>20.02</td>
      <td>20.56</td>
      <td>96.24</td>
    </tr>
    <tr>
      <td>5</td>
      <td>empireyikesback</td>
      <td>23.28</td>
      <td>22.16</td>
      <td>54.56</td>
      <td>68.44</td>
    </tr>
    <tr>
      <td>6</td>
      <td>burgertownthicnred</td>
      <td>14.50</td>
      <td>15.95</td>
      <td>69.56</td>
      <td>30.44</td>
    </tr>
    <tr>
      <td>7</td>
      <td>therealfergus</td>
      <td>62.80</td>
      <td>16.03</td>
      <td>21.17</td>
      <td>62.80</td>
    </tr>
    <tr>
      <td>8</td>
      <td>mackjyers21</td>
      <td>55.02</td>
      <td>21.36</td>
      <td>23.62</td>
      <td>34.96</td>
    </tr>
    <tr>
      <td>9</td>
      <td>shakylegs</td>
      <td>30.55</td>
      <td>26.70</td>
      <td>42.75</td>
      <td>7.50</td>
    </tr>
    <tr>
      <td>10</td>
      <td>tonygordzilla22</td>
      <td>27.68</td>
      <td>24.26</td>
      <td>48.06</td>
      <td>2.24</td>
    </tr>
    <tr>
      <td>11</td>
      <td>black8yellownation</td>
      <td>7.97</td>
      <td>14.58</td>
      <td>77.45</td>
      <td>0.12</td>
    </tr>
    <tr>
      <td>12</td>
      <td>namebrant</td>
      <td>92.15</td>
      <td>7.85</td>
      <td>0.00</td>
      <td>5.02</td>
    </tr>
  </tbody>
</table>



For you visual minded guys, here's a chart of the previous table:

<iframe
  src="../output/2023Probabilities.html"
  width="850"
  height="850"
  frameborder="0"
></iframe>

## Some Interesting Rankings
 
Here are some interesting rankings from all ten million simulations. The columns
in these tables are given:

* The Chance >= column contains the percentage of simulations in which that team
placed greater than or equal to their given ranking. 
* The Playoff column contains the percentage of simulations in which that team
made the playoffs

#### Most Common Ranking 

The most common ranking order appeared 15,053 times:

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Rank</th>
      <th>Username</th>
      <th>Chance &gt;=</th>
      <th>Playoff</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>herbietime</td>
      <td>51.91110</td>
      <td>99.49</td>
    </tr>
    <tr>
      <td>2</td>
      <td>thezirconisdragon</td>
      <td>42.45852</td>
      <td>96.14</td>
    </tr>
    <tr>
      <td>3</td>
      <td>alecwilson</td>
      <td>59.42196</td>
      <td>96.24</td>
    </tr>
    <tr>
      <td>4</td>
      <td>pacc</td>
      <td>82.67119</td>
      <td>96.59</td>
    </tr>
    <tr>
      <td>5</td>
      <td>therealfergus</td>
      <td>41.78628</td>
      <td>62.80</td>
    </tr>
    <tr>
      <td>6</td>
      <td>empireyikesback</td>
      <td>68.44311</td>
      <td>68.44</td>
    </tr>
    <tr>
      <td>7</td>
      <td>burgertownthicnred</td>
      <td>53.91343</td>
      <td>30.44</td>
    </tr>
    <tr>
      <td>8</td>
      <td>mackjyers21</td>
      <td>76.38372</td>
      <td>34.96</td>
    </tr>
    <tr>
      <td>9</td>
      <td>shakylegs</td>
      <td>57.25153</td>
      <td>7.50</td>
    </tr>
    <tr>
      <td>10</td>
      <td>namebrant</td>
      <td>68.99480</td>
      <td>5.02</td>
    </tr>
    <tr>
      <td>11</td>
      <td>tonygordzilla22</td>
      <td>90.98705</td>
      <td>2.24</td>
    </tr>
    <tr>
      <td>12</td>
      <td>black8yellownation</td>
      <td>100.00000</td>
      <td>0.12</td>
    </tr>
  </tbody>
</table>

#### Unlikely Top 3

In this ranking, mackjeyers, burgertownthicnred, and shakylegs take the top
spots despite each having a less than one percent chance of doing so. 

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Rank</th>
      <th>Username</th>
      <th>Chance &gt;=</th>
      <th>Playoff</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>mackjyers21</td>
      <td>0.29770</td>
      <td>34.96</td>
    </tr>
    <tr>
      <td>2</td>
      <td>burgertownthicnred</td>
      <td>0.63209</td>
      <td>30.44</td>
    </tr>
    <tr>
      <td>3</td>
      <td>shakylegs</td>
      <td>0.38048</td>
      <td>7.50</td>
    </tr>
    <tr>
      <td>4</td>
      <td>herbietime</td>
      <td>95.58877</td>
      <td>99.49</td>
    </tr>
    <tr>
      <td>5</td>
      <td>alecwilson</td>
      <td>90.68135</td>
      <td>96.24</td>
    </tr>
    <tr>
      <td>6</td>
      <td>pacc</td>
      <td>96.58791</td>
      <td>96.59</td>
    </tr>
    <tr>
      <td>7</td>
      <td>thezirconisdragon</td>
      <td>98.25850</td>
      <td>96.14</td>
    </tr>
    <tr>
      <td>8</td>
      <td>therealfergus</td>
      <td>89.60008</td>
      <td>62.80</td>
    </tr>
    <tr>
      <td>9</td>
      <td>empireyikesback</td>
      <td>97.45993</td>
      <td>68.44</td>
    </tr>
    <tr>
      <td>10</td>
      <td>namebrant</td>
      <td>68.99480</td>
      <td>5.02</td>
    </tr>
    <tr>
      <td>11</td>
      <td>tonygordzilla22</td>
      <td>90.98705</td>
      <td>2.24</td>
    </tr>
    <tr>
      <td>12</td>
      <td>black8yellownation</td>
      <td>100.00000</td>
      <td>0.12</td>
    </tr>
  </tbody>
</table>

#### Lopsided Playoffs

Here, we have the bottom three teams in terms of playoff chances all making the
playoffs. 

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Rank</th>
      <th>Username</th>
      <th>Chance &gt;=</th>
      <th>Playoff</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>herbietime</td>
      <td>51.91110</td>
      <td>99.49</td>
    </tr>
    <tr>
      <td>2</td>
      <td>pacc</td>
      <td>36.62561</td>
      <td>96.59</td>
    </tr>
    <tr>
      <td>3</td>
      <td>thezirconisdragon</td>
      <td>63.62777</td>
      <td>96.14</td>
    </tr>
    <tr>
      <td>4</td>
      <td>namebrant</td>
      <td>0.63411</td>
      <td>5.02</td>
    </tr>
    <tr>
      <td>5</td>
      <td>tonygordzilla22</td>
      <td>0.72256</td>
      <td>2.24</td>
    </tr>
    <tr>
      <td>6</td>
      <td>black8yellownation</td>
      <td>0.12402</td>
      <td>0.12</td>
    </tr>
    <tr>
      <td>7</td>
      <td>alecwilson</td>
      <td>98.68242</td>
      <td>96.24</td>
    </tr>
    <tr>
      <td>8</td>
      <td>empireyikesback</td>
      <td>93.02522</td>
      <td>68.44</td>
    </tr>
    <tr>
      <td>9</td>
      <td>burgertownthicnred</td>
      <td>89.55127</td>
      <td>30.44</td>
    </tr>
    <tr>
      <td>10</td>
      <td>therealfergus</td>
      <td>98.72289</td>
      <td>62.80</td>
    </tr>
    <tr>
      <td>11</td>
      <td>mackjyers21</td>
      <td>99.27435</td>
      <td>34.96</td>
    </tr>
    <tr>
      <td>12</td>
      <td>shakylegs</td>
      <td>100.00000</td>
      <td>7.50</td>
    </tr>
  </tbody>
</table>

### End

We can see that no matter how good or bad your team is, you can still get
incredibly lucky or unlucky with the season schedule. Let me know what you guys 
think about this analysis and if you want to see anything else.