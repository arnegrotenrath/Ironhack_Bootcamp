########################################
##### FUNCTIONS FOR IMMOSCOUT DATA #####
########################################

# +++ IMPORT LIBRARIES +++

import pandas as pd
import numpy as np
import requests

# for XML parsing
from xml.etree import ElementTree


# +++ CONFIGURE PARAMETERS FOR DIFFERENT REQUESTS +++

# Real Estate objects to buy in ...

# Germany
params_de = {
    'realestatetype':'apartmentbuy',
    'geocodes': 1276
}

# Essen
params_essen = {
    'realestatetype':'apartmentbuy',
    'geocodes': 1276010015
}

# Berlin
params_bln = {
    'realestatetype':'apartmentbuy',
    'geocodes': 1276003001
}

# Hamburg
params_ham = {
    'realestatetype':'apartmentbuy',
    'geocodes': 1276006001
}


# +++ VARIABLES +++

# dictionary containing the geocodeIds for various predefined locations
di_locations = {
    'deutschland': 1276,
    'berlin': 1276003001,
    'essen': 1276010015,
    'hamburg': 1276006001
}


# +++ FUNCTIONS +++

'''
# Define function to get information from a root into a dictionary
def get_buy_data(root):
    # define lists for each field that will be extracted
    lst_realEstateId = []
    lst_titles = []
    lst_cities = []
    lst_quarters = []
    lst_postcode = []
    lst_street = []
    lst_houseNo = []
    lst_lat = []
    lst_long = []
    lst_privateOffer = []
    lst_mktType = []
    lst_courtage = []
    lst_prices = []
    lst_livingSpace = []
    lst_rooms = []
    lst_rentScope = []
    lst_num_pages = []

    # loop through the real estate entries and save information into lists
    for child in root[1]:
        lst_realEstateId.append(child.find('realEstateId').text) if not child.find(
            'realEstateId') is None else lst_realEstateId.append(np.NaN)
        lst_titles.append(child[3].find('title').text) if not child[3].find('title') is None else lst_titles.append(
            np.NaN)
        lst_cities.append(child[3][1].find('city').text) if not child[3][1].find('city') is None else lst_titles.append(
            np.NaN)
        lst_quarters.append(child[3][1].find('quarter').text) if not child[3][1].find(
            'quarter') is None else lst_quarters.append(np.NaN)
        lst_postcode.append(child[3][1].find('postcode').text) if not child[3][1].find(
            'postcode') is None else lst_postcode.append(np.NaN)
        lst_street.append(child[3][1].find('street').text) if not child[3][1].find(
            'street') is None else lst_street.append(np.NaN)
        lst_houseNo.append(child[3][1].find('houseNumber').text) if not child[3][1].find(
            'houseNumber') is None else lst_houseNo.append(np.NaN)
        lst_lat.append(child[3][1].find('wgs84Coordinate').find('latitude').text) if not child[3][1].find(
            'wgs84Coordinate') is None else lst_lat.append(np.NaN)
        lst_long.append(child[3][1].find('wgs84Coordinate').find('longitude').text) if not child[3][1].find(
            'wgs84Coordinate') is None else lst_long.append(np.NaN)
        lst_privateOffer.append(child[3].find('privateOffer').text) if not child[3].find(
            'privateOffer') is None else lst_privateOffer.append(np.NaN)
        lst_mktType.append(child[3].find('price').find('marketingType').text) if not child[3].find('price').find(
            'marketingType') is None else lst_mktType.append(np.NaN)
        lst_courtage.append(child[3].find('courtage').find('hasCourtage').text) if not child[3].find('courtage').find(
            'hasCourtage') is None else lst_courtage.append(np.NaN)
        lst_prices.append(child[3].find('price')[0].text) if not child[3].find('price')[
                                                                     0] is None else lst_prices.append(np.NaN)
        lst_livingSpace.append(child[3].find('livingSpace').text) if not child[3].find(
            'livingSpace') is None else lst_livingSpace.append(np.NaN)
        lst_rooms.append(child[3].find('numberOfRooms').text) if not child[3].find(
            'numberOfRooms') is None else lst_rooms.append(np.NaN)
        lst_num_pages.append(root[0].find('pageNumber').text) if not root[0].find(
            'pageNumber') is None else lst_num_pages.append(np.NaN)

        # there is no rentScope for apartments to buy, so fill it with NaN
        lst_rentScope.append(np.NaN)

    # create dictionary from lists above
    dict_lsts = {'id': lst_realEstateId,
                 'title': lst_titles,
                 'city': lst_cities,
                 'quarter': lst_quarters,
                 'postcode': lst_postcode,
                 'street': lst_street,
                 'houseNo': lst_houseNo,
                 'price': lst_prices,
                 'qm': lst_livingSpace,
                 'n_room': lst_rooms,
                 'latitude': lst_lat,
                 'longitude': lst_long,
                 'privateOffer': lst_privateOffer,
                 'marketingType': lst_mktType,
                 'hasCourtage': lst_courtage,
                 'rentScope': lst_rentScope,
                 'n_page_is24': lst_num_pages
                 }

    return dict_lsts
'''


# Define function to get information from a root into a dictionary
def get_xml_data(root, type_='apt_buy'):
    # define lists for each field that will be extracted
    lst_realEstateId = []
    lst_titles = []
    lst_cities = []
    lst_quarters = []
    lst_postcode = []
    lst_street = []
    lst_houseNo = []
    lst_lat = []
    lst_long = []
    lst_privateOffer = []
    lst_mktType = []
    lst_courtage = []
    lst_prices = []
    lst_purchase_prices = []
    lst_rent_cold = []
    lst_rent_warm = []
    lst_livingSpace = []
    lst_rooms = []
    lst_rentScope = []
    lst_num_pages = []

    # loop through the real estate entries and save information into lists
    for child in root[1]:
        lst_realEstateId.append(child.find('realEstateId').text) if not child.find(
            'realEstateId') is None else lst_realEstateId.append(np.NaN)
        lst_titles.append(child[3].find('title').text) if not child[3].find('title') is None else lst_titles.append(
            np.NaN)
        lst_cities.append(child[3][1].find('city').text) if not child[3][1].find('city') is None else lst_titles.append(
            np.NaN)
        lst_quarters.append(child[3][1].find('quarter').text) if not child[3][1].find(
            'quarter') is None else lst_quarters.append(np.NaN)
        lst_postcode.append(child[3][1].find('postcode').text) if not child[3][1].find(
            'postcode') is None else lst_postcode.append(np.NaN)
        lst_street.append(child[3][1].find('street').text) if not child[3][1].find(
            'street') is None else lst_street.append(np.NaN)
        lst_houseNo.append(child[3][1].find('houseNumber').text) if not child[3][1].find(
            'houseNumber') is None else lst_houseNo.append(np.NaN)
        lst_lat.append(child[3][1].find('wgs84Coordinate').find('latitude').text) if not child[3][1].find(
            'wgs84Coordinate') is None else lst_lat.append(np.NaN)
        lst_long.append(child[3][1].find('wgs84Coordinate').find('longitude').text) if not child[3][1].find(
            'wgs84Coordinate') is None else lst_long.append(np.NaN)
        lst_privateOffer.append(child[3].find('privateOffer').text) if not child[3].find(
            'privateOffer') is None else lst_privateOffer.append(np.NaN)
        lst_mktType.append(child[3].find('price').find('marketingType').text) if not child[3].find('price').find(
            'marketingType') is None else lst_mktType.append(np.NaN)
        lst_courtage.append(child[3].find('courtage').find('hasCourtage').text) if not child[3].find(
            'courtage') is None else lst_courtage.append(np.NaN)
        lst_prices.append(child[3].find('price')[0].text) if not child[3].find('price')[
                                                                     0] is None else lst_prices.append(np.NaN)
        lst_livingSpace.append(child[3].find('livingSpace').text) if not child[3].find(
            'livingSpace') is None else lst_livingSpace.append(np.NaN)
        lst_rooms.append(child[3].find('numberOfRooms').text) if not child[3].find(
            'numberOfRooms') is None else lst_rooms.append(np.NaN)
        # lst_rent_warm.append(child[3].find('calculatedPrice').find('value').text) if not child[3].find('calculatedPrice') is None else lst_rent_warm.append(np.NaN)
        # lst_rentScope.append(child[3].find('calculatedPrice').find('rentScope').text) if not child[3].find('calculatedPrice') is None else lst_rentScope.append(np.NaN)
        lst_num_pages.append(root[0].find('pageNumber').text) if not root[0].find(
            'pageNumber') is None else lst_num_pages.append(np.NaN)

    if type_ == 'apt_buy':
        lst_purchase_prices = lst_prices
        lst_rent_cold = [np.NaN] * len(lst_realEstateId)
    elif type_ == 'apt_rent':
        lst_rent_cold = lst_prices
        lst_purchase_prices = [np.NaN] * len(lst_realEstateId)
    else:
        print('error in get_xml_data, check the "type" parameter!')

    # create dictionary from lists above
    dict_lsts = {'id': lst_realEstateId,
                 'title': lst_titles,
                 'city': lst_cities,
                 'quarter': lst_quarters,
                 'postcode': lst_postcode,
                 'street': lst_street,
                 'houseNo': lst_houseNo,
                 'purchase_price': lst_purchase_prices,
                 'rent_cold': lst_rent_cold,
                 'qm': lst_livingSpace,
                 'n_room': lst_rooms,
                 'latitude': lst_lat,
                 'longitude': lst_long,
                 'privateOffer': lst_privateOffer,
                 'marketingType': lst_mktType,
                 'hasCourtage': lst_courtage,
                 # 'rent_warm': lst_rent_warm,
                 # 'rentScope': lst_rentScope,
                 'n_page_is24': lst_num_pages
                 }

    return dict_lsts


def df_from_url(url, params, auth, type='apt_buy'):
    # send the get request using global auth information and provided url and params
    resp = requests.get(url, auth=auth, params=params)

    # get XML response into the root of an ElementTree
    root = ElementTree.fromstring(resp.content)

    # call get_xml_data function to store information into a dataframe

    df = pd.DataFrame(get_xml_data(root, type))

    return df


# Function to get the number of pages based on a URL
def num_pages_from_url(url, params, auth):
    # send the get request using global auth information and provided url and params
    resp = requests.get(url, auth=auth, params=params)

    # get XML response into the root of an ElementTree
    root = ElementTree.fromstring(resp.content)

    # navigate to the number of pages and get the text
    num_pages = int(root[0].find('numberOfPages').text)

    return num_pages


# function to create entire dataframe of real estate data for a specific location
def create_df_all(url, location, di_locations, auth, type='apt_buy'):

    di_type = {
        'apt_buy': 'apartmentbuy',
        'apt_rent': 'apartmentrent'
    }

    params_loc = {
        'realestatetype': di_type[type],  # default: 'apartmentbuy',
        'geocodes': di_locations[location]
    }

    df_location = df_from_url(url, params_loc, auth, type)

    for i in range(2, num_pages_from_url(url, params_loc, auth) + 1):
        params_loc_loop = {
            'realestatetype': di_type[type],  # default: 'apartmentbuy',
            'geocodes': di_locations[location],
            'pagenumber': i
        }
        df_location = df_location.append(df_from_url(url, params_loc_loop, auth, type))

    return df_location.reset_index(drop=True)


# function to calculate price per qm based on the columns 'price' and 'qm'
def calc_purchase_price_per_qm(df):
    df['purchase_price'] = pd.to_numeric(df['purchase_price'])
    df['qm'] = pd.to_numeric(df['qm'])
    df['n_room'] = pd.to_numeric(df['n_room'])
    df['n_page_is24'] = pd.to_numeric(df['n_page_is24'])
    df['purchase_price_per_qm'] = np.where(df['qm'] != 0, round(df['purchase_price'] / df['qm'], 1), np.NaN)

    return df


# function to calculate price per qm based on the columns 'price' and 'qm'
def calc_rent_cold_per_qm(df):
    df['rent_cold'] = pd.to_numeric(df['rent_cold'])
    df['qm'] = pd.to_numeric(df['qm'])
    df['n_room'] = pd.to_numeric(df['n_room'])
    df['n_page_is24'] = pd.to_numeric(df['n_page_is24'])
    df['rent_cold_per_qm'] = np.where(df['qm'] != 0, round(df['rent_cold'] / df['qm'], 1), np.NaN)

    return df


# function to transform some characters for successful csv export
def transform_title(df):
    df['title'] = df['title'].str.replace(';', ',')
    df['title'] = df['title'].str.replace('\r', ' ')

    return df


# function that calls different transformation functions
def df_transform(df, type_):
    transform_title(df)
    if type_ == 'apt_buy':
        calc_purchase_price_per_qm(df)
    elif type_ == 'apt_rent':
        calc_rent_cold_per_qm(df)
    else:
        print('error: df_transform')

    return df


# +++ FUNCTIONS FOR TESTING PURPOSES +++

# function to create entire dataframe of real estate data for a specific location - FOR A SPECIFIC NUMBER OF PAGES
def test_create_df_all(url, location, di_locations, auth, num_pages=5, type='apt_buy'):

    di_type = {
        'apt_buy': 'apartmentbuy',
        'apt_rent': 'apartmentrent'
    }

    params_loc = {
        'realestatetype': di_type[type],  # default: 'apartmentbuy',
        'geocodes': di_locations[location]
    }

    df_location = df_from_url(url, params_loc, auth, type)

    for i in range(2, num_pages + 1):
        params_loc_loop = {
            'realestatetype': di_type[type],  # default: 'apartmentbuy',
            'geocodes': di_locations[location],
            'pagenumber': i
        }
        df_location = df_location.append(df_from_url(url, params_loc_loop, auth, type))

    return df_location.reset_index(drop=True)


# EOF
