# Ironhack_04_Tableau_DB_analysis
Analysis of the german public transport on state level


# 0. Contributors
This work is inspired by [David Kriesels](http://www.dkriesel.com/start) great [Talk](https://media.ccc.de/v/36c3-10652-bahnmining_-_punktlichkeit_ist_eine_zier) "Bahnmining" during the 36C3.


# 1. Goal
During David's talk, he displayed the punctuality of trains at every train station in germany. 
One result was that the majority of unpunctual train arrivings occur in north, west and south germany.
The goal of this project is to gain a more detailed insight and maybe find an explanation why this issue isn't as pronounced in the east of germany.
The assumption is that a high population density has a negative effect on the punctuality, which is to be tested.

# 2. Data Gathering
Via the help of [Github Public datasets](https://github.com/awesomedata/awesome-public-datasets) a very valuable datasource was found. By selecting "Germany" one gets redirected to 
[destatis genesis](https://www-genesis.destatis.de/genesis/online) which is -if available- a rich source for various datasets.
Here, information on some key indicators of german train transport, namely the number of moved persons in total and combined with the covered distance is gathered. These information are 
ordered on a yearly time scale from 2004 to 2018 and by states. In another dataset, as well from destatis, information about the population of those states within the years of interest is found. Since the area of the states is static in the 
investigated period, they are manually identified from [Wikipedia](https://de.wikipedia.org/wiki/Liste_der_deutschen_Bundesl%C3%A4nder_nach_Fl%C3%A4che)

# 3. Cleaning and Analyzing data
The datasets are cleaned by removing a few non-useful lines and rows and aggregating the column for different types of companies, since we are not able to examine
on this level due to time constraints of the project. All in all, the quality of the data is quite well, hence only minor alterations e.g. on the datatypes need to 
be conducted bevore the sets can be wrangled for our special case. Since the focus of the analysis is on the total number of moved persons and their covered distance with respect to the
population and population density of a state, we merge the datasets into one with the desired information.

# 4. Presentation
In order to efficiently present the data, a number of statistics on a state level are displayed. Namely, the population density, the number of moved persons in total and per area as well as the 
number of trips per capita. A special kind of state in germany are the three city states Berlin, Bremen and Hamburg. Since their statistics differ quite a bit from the other 13 states, they are excluded in a 
number of visualizations since they distort the scale and make a comparison between the non-city states impossible.
Furthermore, the data is available broken down into the years 2004-2018. Some information about the progression of the different states regarding this topic can be derived from an analysis of a comparison of
different years.

# 5. Results
A number of observations can be derived from the visualization. As expected, the number of moved persons per area is extremely high in the three city states compared to the other ones. If they are included, it gets obvious
that Nordrhein-Westfalen and Hessen perform best in this category. The same holds for the number of trips per capita, even though the difference between the city states and the other ones is not as pronounced.
An answer to the thesis from the beginning -why are train stations in the east of germany show better punctuality of their trains- could be that in those states, the moved persons per area is quite low compared to the states in the other parts
of germany. Hence, ther should be more area available move comparatively low numbers of persons which should make it easier to build and maintain a train network.
