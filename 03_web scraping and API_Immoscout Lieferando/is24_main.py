#!/usr/bin/env python3

import pandas as pd
from library import immoscout as im
from requests_oauthlib import OAuth1

import getpass

# +++ SETUP +++

# auth information obtained from IS24
client_key = 'immokb24_contentKey'
client_secret = getpass.getpass('Type your client secret: ')

base_url = 'https://rest.immobilienscout24.de/restapi/api/search/v1.0/search/region'

auth = OAuth1(client_key, client_secret)


# +++ DISPLAY OPTIONS +++

pd.options.display.max_columns = None
pd.options.display.max_rows = 2000
pd.options.display.max_colwidth = 200

# +++ CREATE DF +++





# CREATE CSV FILES

location = 'berlin'

# create dataframe
df_buy = im.create_df_all(base_url, location, im.di_locations, auth, type='apt_buy')

df_rent = im.create_df_all(base_url, location, im.di_locations, auth, type='apt_rent')

df_buy = im.df_transform(df_buy, 'apt_buy')

df_rent = im.df_transform(df_rent, 'apt_rent')

df_all = pd.concat([df_buy, df_rent], ignore_index=True)


df_buy.to_csv(f'Data/df_{location}_apts_buy_0.6.csv', sep=';')
df_rent.to_csv(f'Data/df_{location}_apts_rent_0.6.csv', sep=';')
df_all.to_csv(f'Data/df_{location}_apts_merged_0.6.csv', sep=';')




'''
# +++ TESTING +++ 

# let the user type the name of the city
supported_locations = ["deutschland", "essen", "berlin"]
input_location = ""
while input_location not in supported_locations:
    input_location = input(f'Type the name of the city here. Choose between {supported_locations}: ').lower() 
print("Generating Dataframe")

# test with first X pages
input_number_of_pages = int(input('How many pages?: '))

# enter type of data: rent or buy
input_type = input('Choose between "apt_buy" and "apt_rent": ')

# create test dataframe
df = im.test_create_df_all(base_url, input_location, im.di_locations, auth, input_number_of_pages, input_type)


# transform df
df = im.df_transform(df, input_type)


# +++ OUTPUT TEST DATAFRAME AS CSV +++

df.to_csv(f'data/is24_test_{input_location}_{input_type}_3.csv', sep=';') 

# print(df.head(20))
'''



