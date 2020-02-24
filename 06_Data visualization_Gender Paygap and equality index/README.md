# ironhack_project6_paygap

# 0. Contributors
This work was conducted within the ironhack data-thieves project week by Paschoal Morelli, Can Paul Bineytioglu and Arne Grotenrath.


# 1. Goal
During this project, the gathering of data from online sources, their cleaning, analyzation and combination in order to gain insight into their correlation is trained.

The question arose, if there is a correlation between the price of real estate and the number of restaurants one can order food from.
In order to answer this, the API of Immobilienscout24.de was used. Additionally, the technique of web-scraping was applied to derive data from lieferando.de

Due to the brief period of this project of just a couple of days, only a fraction of the available data was analyzed: To ensure a managable workload, only real estate from berlin was taken into account. Here, seperate analysis were conducted on real estate to buy and to rent. Moreover, real estate were clustered into bins with the same postal code.

Idea AG: Explain the basic idea of the gpg: show a bar graph of the unadjusted pay gap, maybe the formula on a very basic example. Then, split the bar graph into slices each accounting for a part of the unadjusted pay gap. Afterwards, explain that we didn't even made it to this subtopic.

# 2. Data Gathering
Data on the gender-wage-gap and the gini-coefficient was derived from the [OECD Database](https://data.oecd.org/earnwage/gender-wage-gap.htm). We have decided to extract the data for all the OECD member countries with annual observations from 2005-2017, in order to achieve the most consistent results.The Organisation for Economic Co-operation and Development (OECD) is an intergovernmental economic organisation with 36 member countries, founded in 1961 to stimulate economic progress and world trade. 
Also we used data from [EUROSTAT](https://ec.europa.eu/eurostat/web/products-datasets/-/isoc_sks_itsps) to show the share of women in Tech-Jobs- referred to as ICT (Information and Communication Technology sector).

The data is then stored in csv files in the /data folder.

# 3. Cleaning and Analyzing data
exploratory_analysis_BUY_v0.4.ipynb and exploratory_analysis_rent_v0.4.ipynb are used to wrangle the already combined data from the two sources. A presentation of the results is focused on the mean of prices of real estate to buy or to rent vs. the number of restaurants one can order from. It needs to be kept in mind, that the analysis is focused on real estate grouped by their postal code. A much more detailed analysis could be done with help of the underlying libraries with a more prolonged time frame.
Furthermore, the analysis only processed data from the city of berlin. Additional cities or all real estate in germany can in theory be analyzed and compared with the provided methods.


# 4. Presentation
The project is summarized within a short presentation with help of presentation.ipynb. Its outcome is stored in /presentation

# 5. Result
As supposed, the number of restaurants delivering to real estate within a postal code in berlin correlates with the buy or rent price. a possible explanation could be the proximity to the city center, where real estate prices are in general higher compared to the outskirts.
