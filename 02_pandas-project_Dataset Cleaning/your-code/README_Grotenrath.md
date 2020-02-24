Pandas Project - Data Cleaning

Process:

0 Copy dataset in order to clean it

1 First Look at the dataset

2 Check the number of rows and columns, get an overview

3 Check for empty and not-useful columns
3.1 Dropping empty columns
3.2 Dropping non-useful columns
3.2.1 The column "original order" just counts the number of incidents. Since the incidents are ordered by date, this column contains the same value as the index of the row and can be dropped.
3.2.2 Case Number.1 and Case Number.2
3.2.3 Additional, but not evaluable information in columns "pdf", "href formula", "href" and "name"

4 Renaming columns: "Sex " to "Sex", "Species " to "Species"

5 Aggregating associated values
5.1 For column "Type"
5.2 For column "Fatal"
5.3 Compare Case Number, Date and Year


In order to clean the dataset, a first overview is essential. By deleting empty or mostly empty columns and those with little or no extractable value, the low hanging fruits are picked.

The most difficult, yet valuable work is done in the last phase, when similar values are aggregated. Here, solid progress was made in the column "Case Number". By transforming the values in that column, the columns "Date" and "Year" became obsolete and could be dropped. Unfortunately, the conducted attempts to undergo the same transformation in the column "Species" were not as successful. By gaining further experienced in aggregating even more varying values, a greater insight into datasets can be achieved.