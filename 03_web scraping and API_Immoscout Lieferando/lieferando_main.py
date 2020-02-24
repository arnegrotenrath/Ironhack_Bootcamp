#!/usr/bin/env python3

import pandas as pd
from library import lieferando as lf

# Define input/output file
input_file = "data/df_berlin_apts_merged_0.6.csv"
output_file = "data/20200124_is24_buyrent_plus_lieferando.csv"

# Input
df_real_estate = pd.read_csv(input_file, sep=";")

# Get unique lit of postcodes
df_postcode = df_real_estate.drop_duplicates(subset="postcode") 

# Scrap data from lieferando
df_n_restaurant = lf.get_n_restaurant(list(df_postcode["postcode"]))

# Merge main dataframe with activity cleaned
df_real_estate_n_rest = pd.merge(df_real_estate, df_n_restaurant[["postcode","n_restaurant"]], how="left", on="postcode")

# Output
df_real_estate_n_rest.to_csv(output_file, sep=";", index=False)