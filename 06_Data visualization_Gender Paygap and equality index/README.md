# ironhack_project6_paygap

# 0. Contributors
This work was conducted within the ironhack project "Visualizing Real World Data" by Arne Grotenrath, Maximilian Albrecht and Valérie Stroh.

# 1. Goal
The goal of this 3-day mini-project was to practice creating and interpreting different types of visualizations using real world data.
Thematically we wanted to gain more data-driven insights about the gender-pay-gap across different countries. Especially we wanted to focus on variables that could be an explanation for the gap between the earnings of men an women. For that reason we examined the wages in the US Tech area and took a look at the relationship between the gender-pay-gap and the [gender-equality-index](https://eige.europa.eu/gender-equality-index/about), which indicates gender equality in states within the European Union. 

# 2. Data Gathering
Data on the gender-pay-gap and the gini-coefficient, which indicates the wealth distribution of a country, was derived from the [OECD Database](https://data.oecd.org/earnwage/gender-wage-gap.htm). We have decided to extract the data for all the OECD member countries with annual observations from 2005-2017, in order to achieve the most consistent results. The Organisation for Economic Co-operation and Development (OECD) is an intergovernmental economic organisation with 36 member countries, founded in 1961 to stimulate economic progress and world trade. 
Also we used data from [EUROSTAT](https://ec.europa.eu/eurostat/web/products-datasets/-/isoc_sks_itsps) to show the share of women in Tech-Jobs- referred to as ICT (Information and Communication Technology sector). Due to time constraints we omitted the gini-cofficient and ICT from the presentation.

[Data](https://data.europa.eu/euodp/de/data/dataset/gender-equality-index/resource/1937ea33-7be1-486f-9126-7b60f087d4e4) about the gender-equality-index is found for the years 2005, 2010, 2012, 2015 and 2017 for the 28 european states.

The data is then stored in csv files in the /data folder.

# 3. Cleaning and Analyzing data

Since the data was in general in a very good shape, not much effort was needed to clean the datasets. A bigger issue with the data in this realm is the nature of the gender-pay-gap. Since a number of institutions on different levels, e.g. national, european or global, use their own interpretation of the gender-pay-gap, different sources used varying methods to calculate the pay cap which makes them difficult to compare. 

# 4. Presentation
A few main findings of the project are summarized within a short presentation with help of Tabelau. Its outcome is stored in /presentation

# 5. Result
One insight into the gender-pay-gap realm is that it is surprisingly difficult to compare different datsets. 
One needs to keep in mind, that only the unadjusted pay-gap was examined. Its counterpart, the adjusted one, accounts for e.g. different working hours or specialisations between men and women, and is hence calculated in a different manner regarding which factors are included.
It comes as a surprise that even the unadjusted gap differs due to for example varying calculations regarding the timeframe (hourly vs. monthly vs. yearly wage).

Nevertheless, it was possible to derive some insights. A deeper understanding of the pay-gap in the tech sector, in different countries and the very weak and even slightly positive correlation with the gender-equality-index are the main ones.
