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

# 2022 Simulated Schedules

## Introduction

For a full explanation of methodology see the [2023 Simulated Schedules](../../2023SimulatedSchedules/docs/2023_Schedule_Simulations.md)
page. 

I generated 10 million random season schedules then used the 2022 season point
outcomes each week to determine what the regular season standings would be for 
each schedule.

### Season Results

Here are the results of the 2022 Season

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
      <td>burgertownthicnred</td>
      <td>1856.59</td>
      <td>1599.04</td>
      <td>13-1</td>
    </tr>
    <tr>
      <td>2</td>
      <td>therealfergus</td>
      <td>2176.38</td>
      <td>1684.36</td>
      <td>10-4</td>
    </tr>
    <tr>
      <td>3</td>
      <td>herbietime</td>
      <td>2166.89</td>
      <td>1878.32</td>
      <td>9-5</td>
    </tr>
    <tr>
      <td>4</td>
      <td>thezirconisdragon</td>
      <td>1925.02</td>
      <td>1731.69</td>
      <td>8-6</td>
    </tr>
    <tr>
      <td>5</td>
      <td>mackjyers21</td>
      <td>1838.20</td>
      <td>1870.89</td>
      <td>8-6</td>
    </tr>
    <tr>
      <td>6</td>
      <td>namebrant</td>
      <td>1875.33</td>
      <td>1852.99</td>
      <td>7-7</td>
    </tr>
    <tr>
      <td>7</td>
      <td>empireyikesback</td>
      <td>1603.80</td>
      <td>1675.91</td>
      <td>7-7</td>
    </tr>
    <tr>
      <td>8</td>
      <td>shakylegs</td>
      <td>1820.44</td>
      <td>1773.26</td>
      <td>6-8</td>
    </tr>
    <tr>
      <td>9</td>
      <td>alecwilson</td>
      <td>1711.02</td>
      <td>1953.16</td>
      <td>5-9</td>
    </tr>
    <tr>
      <td>10</td>
      <td>black8yellownation</td>
      <td>1697.22</td>
      <td>1872.82</td>
      <td>4-10</td>
    </tr>
    <tr>
      <td>11</td>
      <td>tonygordzilla22</td>
      <td>1575.23</td>
      <td>1865.20</td>
      <td>4-10</td>
    </tr>
    <tr>
      <td>12</td>
      <td>pacc</td>
      <td>1546.14</td>
      <td>2034.62</td>
      <td>3-11</td>
    </tr>
  </tbody>
</table>

### Ranking Counts
These are the raw counts from the 10 million simulations. Some interesting notes:

* Every team except herbietime could have placed last, who's lowest ranking
in the simulations was 7th.
* Every team could have placed first

There could be schedules were herbietime placed lower than 7th, but they didn't 
occur in these 10 million simulated schedules.

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
      <th>therealfergus</th>
      <td>7051924</td>
      <td>1918803</td>
      <td>626791</td>
      <td>243497</td>
      <td>98729</td>
      <td>39456</td>
      <td>14863</td>
      <td>4442</td>
      <td>1246</td>
      <td>217</td>
      <td>31</td>
      <td>1</td>
    </tr>
    <tr>
      <th>herbietime</th>
      <td>2324007</td>
      <td>5870166</td>
      <td>1466564</td>
      <td>291928</td>
      <td>42931</td>
      <td>4270</td>
      <td>134</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>namebrant</th>
      <td>182179</td>
      <td>549583</td>
      <td>1763731</td>
      <td>2072461</td>
      <td>1714522</td>
      <td>1353389</td>
      <td>990934</td>
      <td>671285</td>
      <td>390579</td>
      <td>201265</td>
      <td>85076</td>
      <td>24996</td>
    </tr>
    <tr>
      <th>thezirconisdragon</th>
      <td>172367</td>
      <td>705490</td>
      <td>2946337</td>
      <td>2284685</td>
      <td>1591888</td>
      <td>1078057</td>
      <td>650100</td>
      <td>362141</td>
      <td>147320</td>
      <td>49836</td>
      <td>10448</td>
      <td>1331</td>
    </tr>
    <tr>
      <th>burgertownthicnred</th>
      <td>132582</td>
      <td>401293</td>
      <td>1322104</td>
      <td>1796774</td>
      <td>1912706</td>
      <td>1705152</td>
      <td>1277458</td>
      <td>830484</td>
      <td>419592</td>
      <td>157110</td>
      <td>39417</td>
      <td>5328</td>
    </tr>
    <tr>
      <th>mackjyers21</th>
      <td>95071</td>
      <td>365016</td>
      <td>1130730</td>
      <td>1751132</td>
      <td>2025363</td>
      <td>1891529</td>
      <td>1343868</td>
      <td>804767</td>
      <td>388339</td>
      <td>152176</td>
      <td>43879</td>
      <td>8130</td>
    </tr>
    <tr>
      <th>shakylegs</th>
      <td>24313</td>
      <td>106217</td>
      <td>386736</td>
      <td>801559</td>
      <td>1289289</td>
      <td>1799152</td>
      <td>2207580</td>
      <td>1670266</td>
      <td>983890</td>
      <td>479109</td>
      <td>195368</td>
      <td>56521</td>
    </tr>
    <tr>
      <th>black8yellownation</th>
      <td>14324</td>
      <td>64955</td>
      <td>250486</td>
      <td>481362</td>
      <td>755281</td>
      <td>1061767</td>
      <td>1504236</td>
      <td>2038612</td>
      <td>2165606</td>
      <td>1097009</td>
      <td>442847</td>
      <td>123515</td>
    </tr>
    <tr>
      <th>alecwilson</th>
      <td>3060</td>
      <td>16875</td>
      <td>89890</td>
      <td>217731</td>
      <td>424854</td>
      <td>751722</td>
      <td>1320777</td>
      <td>2214308</td>
      <td>2477538</td>
      <td>1489315</td>
      <td>729290</td>
      <td>264640</td>
    </tr>
    <tr>
      <th>tonygordzilla22</th>
      <td>134</td>
      <td>891</td>
      <td>6361</td>
      <td>18135</td>
      <td>39613</td>
      <td>78827</td>
      <td>163152</td>
      <td>324104</td>
      <td>705850</td>
      <td>1572148</td>
      <td>3061888</td>
      <td>4028897</td>
    </tr>
    <tr>
      <th>pacc</th>
      <td>22</td>
      <td>283</td>
      <td>3626</td>
      <td>13947</td>
      <td>35539</td>
      <td>80436</td>
      <td>178717</td>
      <td>365826</td>
      <td>796348</td>
      <td>1623371</td>
      <td>2936226</td>
      <td>3965659</td>
    </tr>
    <tr>
      <th>empireyikesback</th>
      <td>17</td>
      <td>428</td>
      <td>6644</td>
      <td>26789</td>
      <td>69285</td>
      <td>156243</td>
      <td>348181</td>
      <td>713765</td>
      <td>1523692</td>
      <td>3178444</td>
      <td>2455530</td>
      <td>1520982</td>
    </tr>
  </tbody>
</table>


### Ranking Percentage

This is the same table as above, however, now it shows as a percentage. I've
also highlighted the ranking that each team actually had in the 2023 season.
Here we can really start to see that the 2022 schedule worked well for some
players: burgertownthicnred and empireyikesback.

* The first column is each team's chance of placing first
* The last column is each team's chance of placing last

<style type="text/css">
#T_5993b_row0_col1, #T_5993b_row1_col2, #T_5993b_row2_col5, #T_5993b_row3_col3, #T_5993b_row4_col0, #T_5993b_row5_col4, #T_5993b_row6_col7, #T_5993b_row7_col9, #T_5993b_row8_col8, #T_5993b_row9_col10, #T_5993b_row10_col11, #T_5993b_row11_col6 {
  color: red;
}
</style>
<table id="T_5993b">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T_5993b_level0_col0" class="col_heading level0 col0" >1</th>
      <th id="T_5993b_level0_col1" class="col_heading level0 col1" >2</th>
      <th id="T_5993b_level0_col2" class="col_heading level0 col2" >3</th>
      <th id="T_5993b_level0_col3" class="col_heading level0 col3" >4</th>
      <th id="T_5993b_level0_col4" class="col_heading level0 col4" >5</th>
      <th id="T_5993b_level0_col5" class="col_heading level0 col5" >6</th>
      <th id="T_5993b_level0_col6" class="col_heading level0 col6" >7</th>
      <th id="T_5993b_level0_col7" class="col_heading level0 col7" >8</th>
      <th id="T_5993b_level0_col8" class="col_heading level0 col8" >9</th>
      <th id="T_5993b_level0_col9" class="col_heading level0 col9" >10</th>
      <th id="T_5993b_level0_col10" class="col_heading level0 col10" >11</th>
      <th id="T_5993b_level0_col11" class="col_heading level0 col11" >12</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_5993b_level0_row0" class="row_heading level0 row0" >therealfergus</th>
      <td id="T_5993b_row0_col0" class="data row0 col0" >70.51924</td>
      <td id="T_5993b_row0_col1" class="data row0 col1" >19.18803</td>
      <td id="T_5993b_row0_col2" class="data row0 col2" >6.26791</td>
      <td id="T_5993b_row0_col3" class="data row0 col3" >2.43497</td>
      <td id="T_5993b_row0_col4" class="data row0 col4" >0.98729</td>
      <td id="T_5993b_row0_col5" class="data row0 col5" >0.39456</td>
      <td id="T_5993b_row0_col6" class="data row0 col6" >0.14863</td>
      <td id="T_5993b_row0_col7" class="data row0 col7" >0.04442</td>
      <td id="T_5993b_row0_col8" class="data row0 col8" >0.01246</td>
      <td id="T_5993b_row0_col9" class="data row0 col9" >0.00217</td>
      <td id="T_5993b_row0_col10" class="data row0 col10" >0.00031</td>
      <td id="T_5993b_row0_col11" class="data row0 col11" >1e-05</td>
    </tr>
    <tr>
      <th id="T_5993b_level0_row1" class="row_heading level0 row1" >herbietime</th>
      <td id="T_5993b_row1_col0" class="data row1 col0" >23.24007</td>
      <td id="T_5993b_row1_col1" class="data row1 col1" >58.70166</td>
      <td id="T_5993b_row1_col2" class="data row1 col2" >14.66564</td>
      <td id="T_5993b_row1_col3" class="data row1 col3" >2.91928</td>
      <td id="T_5993b_row1_col4" class="data row1 col4" >0.42931</td>
      <td id="T_5993b_row1_col5" class="data row1 col5" >0.0427</td>
      <td id="T_5993b_row1_col6" class="data row1 col6" >0.00134</td>
      <td id="T_5993b_row1_col7" class="data row1 col7" >0.0</td>
      <td id="T_5993b_row1_col8" class="data row1 col8" >0.0</td>
      <td id="T_5993b_row1_col9" class="data row1 col9" >0.0</td>
      <td id="T_5993b_row1_col10" class="data row1 col10" >0.0</td>
      <td id="T_5993b_row1_col11" class="data row1 col11" >0.0</td>
    </tr>
    <tr>
      <th id="T_5993b_level0_row2" class="row_heading level0 row2" >namebrant</th>
      <td id="T_5993b_row2_col0" class="data row2 col0" >1.82179</td>
      <td id="T_5993b_row2_col1" class="data row2 col1" >5.49583</td>
      <td id="T_5993b_row2_col2" class="data row2 col2" >17.63731</td>
      <td id="T_5993b_row2_col3" class="data row2 col3" >20.72461</td>
      <td id="T_5993b_row2_col4" class="data row2 col4" >17.14522</td>
      <td id="T_5993b_row2_col5" class="data row2 col5" >13.53389</td>
      <td id="T_5993b_row2_col6" class="data row2 col6" >9.90934</td>
      <td id="T_5993b_row2_col7" class="data row2 col7" >6.71285</td>
      <td id="T_5993b_row2_col8" class="data row2 col8" >3.90579</td>
      <td id="T_5993b_row2_col9" class="data row2 col9" >2.01265</td>
      <td id="T_5993b_row2_col10" class="data row2 col10" >0.85076</td>
      <td id="T_5993b_row2_col11" class="data row2 col11" >0.24996</td>
    </tr>
    <tr>
      <th id="T_5993b_level0_row3" class="row_heading level0 row3" >thezirconisdragon</th>
      <td id="T_5993b_row3_col0" class="data row3 col0" >1.72367</td>
      <td id="T_5993b_row3_col1" class="data row3 col1" >7.0549</td>
      <td id="T_5993b_row3_col2" class="data row3 col2" >29.46337</td>
      <td id="T_5993b_row3_col3" class="data row3 col3" >22.84685</td>
      <td id="T_5993b_row3_col4" class="data row3 col4" >15.91888</td>
      <td id="T_5993b_row3_col5" class="data row3 col5" >10.78057</td>
      <td id="T_5993b_row3_col6" class="data row3 col6" >6.501</td>
      <td id="T_5993b_row3_col7" class="data row3 col7" >3.62141</td>
      <td id="T_5993b_row3_col8" class="data row3 col8" >1.4732</td>
      <td id="T_5993b_row3_col9" class="data row3 col9" >0.49836</td>
      <td id="T_5993b_row3_col10" class="data row3 col10" >0.10448</td>
      <td id="T_5993b_row3_col11" class="data row3 col11" >0.01331</td>
    </tr>
    <tr>
      <th id="T_5993b_level0_row4" class="row_heading level0 row4" >burgertownthicnred</th>
      <td id="T_5993b_row4_col0" class="data row4 col0" >1.32582</td>
      <td id="T_5993b_row4_col1" class="data row4 col1" >4.01293</td>
      <td id="T_5993b_row4_col2" class="data row4 col2" >13.22104</td>
      <td id="T_5993b_row4_col3" class="data row4 col3" >17.96774</td>
      <td id="T_5993b_row4_col4" class="data row4 col4" >19.12706</td>
      <td id="T_5993b_row4_col5" class="data row4 col5" >17.05152</td>
      <td id="T_5993b_row4_col6" class="data row4 col6" >12.77458</td>
      <td id="T_5993b_row4_col7" class="data row4 col7" >8.30484</td>
      <td id="T_5993b_row4_col8" class="data row4 col8" >4.19592</td>
      <td id="T_5993b_row4_col9" class="data row4 col9" >1.5711</td>
      <td id="T_5993b_row4_col10" class="data row4 col10" >0.39417</td>
      <td id="T_5993b_row4_col11" class="data row4 col11" >0.05328</td>
    </tr>
    <tr>
      <th id="T_5993b_level0_row5" class="row_heading level0 row5" >mackjyers21</th>
      <td id="T_5993b_row5_col0" class="data row5 col0" >0.95071</td>
      <td id="T_5993b_row5_col1" class="data row5 col1" >3.65016</td>
      <td id="T_5993b_row5_col2" class="data row5 col2" >11.3073</td>
      <td id="T_5993b_row5_col3" class="data row5 col3" >17.51132</td>
      <td id="T_5993b_row5_col4" class="data row5 col4" >20.25363</td>
      <td id="T_5993b_row5_col5" class="data row5 col5" >18.91529</td>
      <td id="T_5993b_row5_col6" class="data row5 col6" >13.43868</td>
      <td id="T_5993b_row5_col7" class="data row5 col7" >8.04767</td>
      <td id="T_5993b_row5_col8" class="data row5 col8" >3.88339</td>
      <td id="T_5993b_row5_col9" class="data row5 col9" >1.52176</td>
      <td id="T_5993b_row5_col10" class="data row5 col10" >0.43879</td>
      <td id="T_5993b_row5_col11" class="data row5 col11" >0.0813</td>
    </tr>
    <tr>
      <th id="T_5993b_level0_row6" class="row_heading level0 row6" >shakylegs</th>
      <td id="T_5993b_row6_col0" class="data row6 col0" >0.24313</td>
      <td id="T_5993b_row6_col1" class="data row6 col1" >1.06217</td>
      <td id="T_5993b_row6_col2" class="data row6 col2" >3.86736</td>
      <td id="T_5993b_row6_col3" class="data row6 col3" >8.01559</td>
      <td id="T_5993b_row6_col4" class="data row6 col4" >12.89289</td>
      <td id="T_5993b_row6_col5" class="data row6 col5" >17.99152</td>
      <td id="T_5993b_row6_col6" class="data row6 col6" >22.0758</td>
      <td id="T_5993b_row6_col7" class="data row6 col7" >16.70266</td>
      <td id="T_5993b_row6_col8" class="data row6 col8" >9.8389</td>
      <td id="T_5993b_row6_col9" class="data row6 col9" >4.79109</td>
      <td id="T_5993b_row6_col10" class="data row6 col10" >1.95368</td>
      <td id="T_5993b_row6_col11" class="data row6 col11" >0.56521</td>
    </tr>
    <tr>
      <th id="T_5993b_level0_row7" class="row_heading level0 row7" >black8yellownation</th>
      <td id="T_5993b_row7_col0" class="data row7 col0" >0.14324</td>
      <td id="T_5993b_row7_col1" class="data row7 col1" >0.64955</td>
      <td id="T_5993b_row7_col2" class="data row7 col2" >2.50486</td>
      <td id="T_5993b_row7_col3" class="data row7 col3" >4.81362</td>
      <td id="T_5993b_row7_col4" class="data row7 col4" >7.55281</td>
      <td id="T_5993b_row7_col5" class="data row7 col5" >10.61767</td>
      <td id="T_5993b_row7_col6" class="data row7 col6" >15.04236</td>
      <td id="T_5993b_row7_col7" class="data row7 col7" >20.38612</td>
      <td id="T_5993b_row7_col8" class="data row7 col8" >21.65606</td>
      <td id="T_5993b_row7_col9" class="data row7 col9" >10.97009</td>
      <td id="T_5993b_row7_col10" class="data row7 col10" >4.42847</td>
      <td id="T_5993b_row7_col11" class="data row7 col11" >1.23515</td>
    </tr>
    <tr>
      <th id="T_5993b_level0_row8" class="row_heading level0 row8" >alecwilson</th>
      <td id="T_5993b_row8_col0" class="data row8 col0" >0.0306</td>
      <td id="T_5993b_row8_col1" class="data row8 col1" >0.16875</td>
      <td id="T_5993b_row8_col2" class="data row8 col2" >0.8989</td>
      <td id="T_5993b_row8_col3" class="data row8 col3" >2.17731</td>
      <td id="T_5993b_row8_col4" class="data row8 col4" >4.24854</td>
      <td id="T_5993b_row8_col5" class="data row8 col5" >7.51722</td>
      <td id="T_5993b_row8_col6" class="data row8 col6" >13.20777</td>
      <td id="T_5993b_row8_col7" class="data row8 col7" >22.14308</td>
      <td id="T_5993b_row8_col8" class="data row8 col8" >24.77538</td>
      <td id="T_5993b_row8_col9" class="data row8 col9" >14.89315</td>
      <td id="T_5993b_row8_col10" class="data row8 col10" >7.2929</td>
      <td id="T_5993b_row8_col11" class="data row8 col11" >2.6464</td>
    </tr>
    <tr>
      <th id="T_5993b_level0_row9" class="row_heading level0 row9" >tonygordzilla22</th>
      <td id="T_5993b_row9_col0" class="data row9 col0" >0.00134</td>
      <td id="T_5993b_row9_col1" class="data row9 col1" >0.00891</td>
      <td id="T_5993b_row9_col2" class="data row9 col2" >0.06361</td>
      <td id="T_5993b_row9_col3" class="data row9 col3" >0.18135</td>
      <td id="T_5993b_row9_col4" class="data row9 col4" >0.39613</td>
      <td id="T_5993b_row9_col5" class="data row9 col5" >0.78827</td>
      <td id="T_5993b_row9_col6" class="data row9 col6" >1.63152</td>
      <td id="T_5993b_row9_col7" class="data row9 col7" >3.24104</td>
      <td id="T_5993b_row9_col8" class="data row9 col8" >7.0585</td>
      <td id="T_5993b_row9_col9" class="data row9 col9" >15.72148</td>
      <td id="T_5993b_row9_col10" class="data row9 col10" >30.61888</td>
      <td id="T_5993b_row9_col11" class="data row9 col11" >40.28897</td>
    </tr>
    <tr>
      <th id="T_5993b_level0_row10" class="row_heading level0 row10" >pacc</th>
      <td id="T_5993b_row10_col0" class="data row10 col0" >0.00022</td>
      <td id="T_5993b_row10_col1" class="data row10 col1" >0.00283</td>
      <td id="T_5993b_row10_col2" class="data row10 col2" >0.03626</td>
      <td id="T_5993b_row10_col3" class="data row10 col3" >0.13947</td>
      <td id="T_5993b_row10_col4" class="data row10 col4" >0.35539</td>
      <td id="T_5993b_row10_col5" class="data row10 col5" >0.80436</td>
      <td id="T_5993b_row10_col6" class="data row10 col6" >1.78717</td>
      <td id="T_5993b_row10_col7" class="data row10 col7" >3.65826</td>
      <td id="T_5993b_row10_col8" class="data row10 col8" >7.96348</td>
      <td id="T_5993b_row10_col9" class="data row10 col9" >16.23371</td>
      <td id="T_5993b_row10_col10" class="data row10 col10" >29.36226</td>
      <td id="T_5993b_row10_col11" class="data row10 col11" >39.65659</td>
    </tr>
    <tr>
      <th id="T_5993b_level0_row11" class="row_heading level0 row11" >empireyikesback</th>
      <td id="T_5993b_row11_col0" class="data row11 col0" >0.00017</td>
      <td id="T_5993b_row11_col1" class="data row11 col1" >0.00428</td>
      <td id="T_5993b_row11_col2" class="data row11 col2" >0.06644</td>
      <td id="T_5993b_row11_col3" class="data row11 col3" >0.26789</td>
      <td id="T_5993b_row11_col4" class="data row11 col4" >0.69285</td>
      <td id="T_5993b_row11_col5" class="data row11 col5" >1.56243</td>
      <td id="T_5993b_row11_col6" class="data row11 col6" >3.48181</td>
      <td id="T_5993b_row11_col7" class="data row11 col7" >7.13765</td>
      <td id="T_5993b_row11_col8" class="data row11 col8" >15.23692</td>
      <td id="T_5993b_row11_col9" class="data row11 col9" >31.78444</td>
      <td id="T_5993b_row11_col10" class="data row11 col10" >24.5553</td>
      <td id="T_5993b_row11_col11" class="data row11 col11" >15.20982</td>
    </tr>
  </tbody>
</table>

### Playoff Chances

Aggregating the previous table gives us a better picture.

* Burgertownthicnred took 1st place, with only a 1.3% chance, and had a 98.7%
chance of placing worse.
* Empireyikesback took 7th and had a 93.9% chance of placing worse.
* Blackandyellownation took 10th and had a 83.4% chance of placing better.
* Herbietime took 3rd and had an 81.9% chance of placing better.

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
      <td>burgertownthicnred</td>
      <td>0.00</td>
      <td>1.33</td>
      <td>98.67</td>
      <td>72.71</td>
    </tr>
    <tr>
      <td>2</td>
      <td>therealfergus</td>
      <td>70.52</td>
      <td>19.19</td>
      <td>10.29</td>
      <td>99.79</td>
    </tr>
    <tr>
      <td>3</td>
      <td>herbietime</td>
      <td>81.94</td>
      <td>14.67</td>
      <td>3.39</td>
      <td>100.00</td>
    </tr>
    <tr>
      <td>4</td>
      <td>thezirconisdragon</td>
      <td>38.24</td>
      <td>22.85</td>
      <td>38.91</td>
      <td>87.79</td>
    </tr>
    <tr>
      <td>5</td>
      <td>mackjyers21</td>
      <td>33.42</td>
      <td>20.25</td>
      <td>46.33</td>
      <td>72.59</td>
    </tr>
    <tr>
      <td>6</td>
      <td>namebrant</td>
      <td>62.82</td>
      <td>13.53</td>
      <td>23.64</td>
      <td>76.36</td>
    </tr>
    <tr>
      <td>7</td>
      <td>empireyikesback</td>
      <td>2.59</td>
      <td>3.48</td>
      <td>93.92</td>
      <td>2.59</td>
    </tr>
    <tr>
      <td>8</td>
      <td>shakylegs</td>
      <td>66.15</td>
      <td>16.70</td>
      <td>17.15</td>
      <td>44.07</td>
    </tr>
    <tr>
      <td>9</td>
      <td>alecwilson</td>
      <td>50.39</td>
      <td>24.78</td>
      <td>24.83</td>
      <td>15.04</td>
    </tr>
    <tr>
      <td>10</td>
      <td>black8yellownation</td>
      <td>83.37</td>
      <td>10.97</td>
      <td>5.66</td>
      <td>26.28</td>
    </tr>
    <tr>
      <td>11</td>
      <td>tonygordzilla22</td>
      <td>29.09</td>
      <td>30.62</td>
      <td>40.29</td>
      <td>1.44</td>
    </tr>
    <tr>
      <td>12</td>
      <td>pacc</td>
      <td>60.34</td>
      <td>39.66</td>
      <td>0.00</td>
      <td>1.34</td>
    </tr>
  </tbody>
</table>

For you visual minded guys, here's a chart of the previous table:

<iframe
  src="../output/2022Probabilities.html"
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

The most common ranking order appeared 16,515 times:

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
      <td>therealfergus</td>
      <td>70.51924</td>
      <td>99.79</td>
    </tr>
    <tr>
      <td>2</td>
      <td>herbietime</td>
      <td>81.94173</td>
      <td>100.00</td>
    </tr>
    <tr>
      <td>3</td>
      <td>thezirconisdragon</td>
      <td>38.24194</td>
      <td>87.79</td>
    </tr>
    <tr>
      <td>4</td>
      <td>namebrant</td>
      <td>45.67954</td>
      <td>76.36</td>
    </tr>
    <tr>
      <td>5</td>
      <td>burgertownthicnred</td>
      <td>55.65459</td>
      <td>72.71</td>
    </tr>
    <tr>
      <td>6</td>
      <td>mackjyers21</td>
      <td>72.58841</td>
      <td>72.59</td>
    </tr>
    <tr>
      <td>7</td>
      <td>shakylegs</td>
      <td>66.14846</td>
      <td>44.07</td>
    </tr>
    <tr>
      <td>8</td>
      <td>alecwilson</td>
      <td>50.39217</td>
      <td>15.04</td>
    </tr>
    <tr>
      <td>9</td>
      <td>black8yellownation</td>
      <td>83.36629</td>
      <td>26.28</td>
    </tr>
    <tr>
      <td>10</td>
      <td>empireyikesback</td>
      <td>60.23488</td>
      <td>2.59</td>
    </tr>
    <tr>
      <td>11</td>
      <td>pacc</td>
      <td>60.34341</td>
      <td>1.34</td>
    </tr>
    <tr>
      <td>12</td>
      <td>tonygordzilla22</td>
      <td>100.00000</td>
      <td>1.44</td>
    </tr>
  </tbody>
</table>

#### Unlikely Top 3

In this ranking, burgertownthicnred, shakylegs, and pacc all beat the odds to 
take the tops spots.

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
      <td>burgertownthicnred</td>
      <td>1.32582</td>
      <td>72.71</td>
    </tr>
    <tr>
      <td>2</td>
      <td>shakylegs</td>
      <td>1.30530</td>
      <td>44.07</td>
    </tr>
    <tr>
      <td>3</td>
      <td>pacc</td>
      <td>0.03931</td>
      <td>1.34</td>
    </tr>
    <tr>
      <td>4</td>
      <td>therealfergus</td>
      <td>98.41015</td>
      <td>99.79</td>
    </tr>
    <tr>
      <td>5</td>
      <td>herbietime</td>
      <td>99.95596</td>
      <td>100.00</td>
    </tr>
    <tr>
      <td>6</td>
      <td>thezirconisdragon</td>
      <td>87.78824</td>
      <td>87.79</td>
    </tr>
    <tr>
      <td>7</td>
      <td>mackjyers21</td>
      <td>86.02709</td>
      <td>72.59</td>
    </tr>
    <tr>
      <td>8</td>
      <td>alecwilson</td>
      <td>50.39217</td>
      <td>15.04</td>
    </tr>
    <tr>
      <td>9</td>
      <td>black8yellownation</td>
      <td>83.36629</td>
      <td>26.28</td>
    </tr>
    <tr>
      <td>10</td>
      <td>namebrant</td>
      <td>98.89928</td>
      <td>76.36</td>
    </tr>
    <tr>
      <td>11</td>
      <td>empireyikesback</td>
      <td>84.79018</td>
      <td>2.59</td>
    </tr>
    <tr>
      <td>12</td>
      <td>tonygordzilla22</td>
      <td>100.00000</td>
      <td>1.44</td>
    </tr>
  </tbody>
</table>

#### Lopsided Playoffs

Here, we have the bottom three teams and the bottom 5th team in terms of 
playoff chance all making the playoffs.

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
      <td>23.24007</td>
      <td>100.00</td>
    </tr>
    <tr>
      <td>2</td>
      <td>therealfergus</td>
      <td>89.70727</td>
      <td>99.79</td>
    </tr>
    <tr>
      <td>3</td>
      <td>black8yellownation</td>
      <td>3.29765</td>
      <td>26.28</td>
    </tr>
    <tr>
      <td>4</td>
      <td>empireyikesback</td>
      <td>0.33878</td>
      <td>2.59</td>
    </tr>
    <tr>
      <td>5</td>
      <td>tonygordzilla22</td>
      <td>0.65134</td>
      <td>1.44</td>
    </tr>
    <tr>
      <td>6</td>
      <td>pacc</td>
      <td>1.33853</td>
      <td>1.34</td>
    </tr>
    <tr>
      <td>7</td>
      <td>namebrant</td>
      <td>86.26799</td>
      <td>76.36</td>
    </tr>
    <tr>
      <td>8</td>
      <td>alecwilson</td>
      <td>50.39217</td>
      <td>15.04</td>
    </tr>
    <tr>
      <td>9</td>
      <td>thezirconisdragon</td>
      <td>99.38385</td>
      <td>87.79</td>
    </tr>
    <tr>
      <td>10</td>
      <td>burgertownthicnred</td>
      <td>99.55255</td>
      <td>72.71</td>
    </tr>
    <tr>
      <td>11</td>
      <td>mackjyers21</td>
      <td>99.91870</td>
      <td>72.59</td>
    </tr>
    <tr>
      <td>12</td>
      <td>shakylegs</td>
      <td>100.00000</td>
      <td>44.07</td>
    </tr>
  </tbody>
</table>

### End

Another showing of how just about anything can happen in the season with 
different schedules.