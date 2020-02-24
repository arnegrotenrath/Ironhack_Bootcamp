from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

def get_n_restaurant(postcodes, postcode_out=None):

    postcode_in = postcodes.copy()

    if postcode_out is None:
        
        postcode_out = []
        global browser
        browser = webdriver.Firefox()
        
    if len(postcode_in) > 0:

        browser.get("https://www.lieferando.de/en/order-takeaway-berlin-"+ str(postcode_in[0]))

        page = BeautifulSoup(browser.page_source,"html.parser")

        restaurant_amount = (page
                            .body
                            .header
                            .find("span", class_="restaurant-amount")
                            )
        
        try:
            postcode_out.append({"postcode" : postcode_in.pop(0),"n_restaurant" : int(restaurant_amount.contents[0])})
        except:
            postcode_in.pop(0)
            

                    
        return get_n_restaurant(postcode_in, postcode_out)


    browser.close()

    return pd.DataFrame(postcode_out)


def get_restaurant_data(postcodes,restaurant_data=None):
    
    postcode_in = postcodes.copy()

    if restaurant_data is None:
        
        restaurant_data = []
        global browser
        browser = webdriver.Firefox()

    if len(postcode_in) > 0:
        
        browser = webdriver.Firefox()        
        browser.get("https://www.lieferando.de/en/order-takeaway-berlin-"+ str(postcode_in[0]))

        try:
            
            restaurants = browser.execute_script('return restaurants')
            
            for restaurant in restaurants:
                restaurant_postcode = postcode_in[0]
                restaurant_name = str(restaurant[4]).strip()
                restaurant_stars = str(restaurant[29][0]).strip()
                restaurant_ratings = str(restaurant[29][1]).strip()
                restaurant_min_price = str(restaurant[10]).strip()
                restaurant_category = [category.strip() for category in  restaurant[30]["categories"].split(",")]
                restaurant_lat = str(restaurant[16]).strip()
                restaurant_lon = str(restaurant[17]).strip()

                restaurant_row = {
                                    "postcode"  : restaurant_postcode,
                                    "name"      : restaurant_name,
                                    "stars"     : restaurant_stars,
                                    "ratings"   : restaurant_ratings,
                                    "min_price" : restaurant_min_price,
                                    "categories": restaurant_category,
                                    "latitude"  : restaurant_lat,
                                    "longitude" : restaurant_lon
                                }
                                
                restaurant_data.append(restaurant_row)

            postcode_in.pop(0)
            return get_restaurant_data(postcode_in,restaurant_data)

        except:
            postcode_in.pop(0)
            return get_restaurant_data(postcode_in,restaurant_data)

    browser.close()

    return pd.DataFrame(restaurant_data)