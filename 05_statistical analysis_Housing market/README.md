# 05_statistical-analysis-project

# 1. Goal

The goal of this project is the practice statistical analysis using the iterative data analysis process


# 2. Data Gathering
A Kaggle dataset on [Housing Prices](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data) is used for this project

# 3. Cleaning
The dataset is cleaned of columns with too more than 10 % missing values. Additionally, rows with NaN values were dropped. This was possible, since the total amount of those rows was just a 
small fraction of the complete dataset. In order to make the data more easily to interpret the values containing information in squared feet were transformed into m².

# 4. Analyzing Data
Not all columns were interesting for a statistical analysis due to various reasons: Some are non-integer or had just a minor fraction of the values with differing values, like the pool area column.
In the end, the SalePrice was compared to the columns 
  * LotArea
  * OverallQual
  * OverallCond
  * YearBuilt
  * YearRemodAdd
  * Fireplaces
  * GarageArea

were further analyzed via an initial plot to get an idea of the correlation between the Saleprice and the named values. A more detailed analysis via linear regression was conducted on the correlation between the area of the real estate and the Price.
It was found that every additional m² of land was lead to a price increase of just 0.003 Dollars.
