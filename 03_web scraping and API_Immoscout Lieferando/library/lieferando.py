### Purpose of lieferando library
### Extract data about restaurants from lieferando.de
### Functions: 
###     get_n_restaurants: get number of restaurants near by a postcode list
###         Call and output format: 
###             get_n_restaurants(postcodes list[]) -> pd.DataFrame(postcodes,number of restaurants)
###     get_restaurant_data: get a set of data about restaurants near by a postcode list 
###         Call and output format: 
###             get_n_restaurants(postcodes list[]) -> pd.DataFrame(postcode,stars,ratings,min_price,categories,latitude,longitude)
###
###
###


# Import libraries for scrapping, parser dynamic html and variables inside JavaScripts

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# This function works with recursive iteractions, look the return sintaxe to better understand
# Input: list of postcodes 
def get_n_restaurant(postcodes: list, postcode_out: list=None) -> pd.DataFrame:

    # Copy values from postcodes to prevent changes in the original variable
    postcode_in = postcodes.copy()

    # Create an empty list at first iteraction and initialize browser for process dynamic webpages 
    if postcode_out is None:
        
        postcode_out = []
        global browser
    
    browser = webdriver.PhantomJS()
    browser.implicitly_wait(3)

    # Validate if the postcode list is empty, if true this means that the iteractions is done
    if len(postcode_in) > 0:

        # Get target webpage 
        browser.get("https://www.lieferando.de/en/order-takeaway-berlin-"+ str(postcode_in[0]))

        # Translate get response with html.parser to access html tags
        page = BeautifulSoup(browser.page_source,"html.parser")

        browser.close()

        # Extract the number of restaurants 
        restaurant_amount = (page
                            .body
                            .header
                            .find("span", class_="restaurant-amount")
                            )
        
        # Try append the number of restaurants for the current postcode iteraction to postcodes output list
        # Pop "remove" the first element of the input list that represents the current iteraction 
        try:
            postcode_out.append({"postcode" : postcode_in[0],"n_restaurant" : int(restaurant_amount.contents[0])})
            print(len(postcode_in))
        except:
            # If any exception happen, just keep to the next postcode
            # Pop "remove" the first element of the input list that represents the current iteraction
            print("error!")
        
        postcode_in.pop(0)    

        # Return call recursively the get_n_restaurant function to iteract with the next postcode                    
        return get_n_restaurant(postcode_in, postcode_out)

    # transform output postcode list into pd:DataFrame and return
    return pd.DataFrame(postcode_out)

# This function works with recursive iteractions, look the return sintaxe to better understand
# Input: list of postcodes 
def get_restaurant_data(postcodes: list,restaurant_data: list=None) -> pd.DataFrame:
    
    # Copy values from postcodes to prevent changes in the original variable
    postcode_in = postcodes.copy()

    # Create an empty list at first iteraction and initialize browser for process dynamic webpages
    if restaurant_data is None:
        
        restaurant_data = []
        global browser
    
    browser = webdriver.PhantomJS()
    browser.implicitly_wait(3)

    # Validate if the postcode list is empty, if true this means that the iteractions is done
    if len(postcode_in) > 0:
        
        # Get target webpage 
        browser = webdriver.PhantomJS()        
        browser.get("https://www.lieferando.de/en/order-takeaway-berlin-"+ str(postcode_in[0]))

        # Try execute script inside of website, this script returns one variable with list of lists that contains the restaurants data 
        try:
            
            restaurants = browser.execute_script('return restaurants')

            # Close de webdriver
            browser.close()
            
            # Iteract to extract relevant data
            for restaurant in restaurants:
                restaurant_postcode = postcode_in[0]
                restaurant_name = str(restaurant[4]).strip()
                restaurant_stars = str(restaurant[29][0]).strip()
                restaurant_ratings = str(restaurant[29][1]).strip()
                restaurant_min_price = str(restaurant[10]).strip()
                restaurant_category = [category.strip() for category in  restaurant[30]["categories"].split(",")]
                restaurant_lat = str(restaurant[16]).strip()
                restaurant_lon = str(restaurant[17]).strip()

                # Put the extrated data inside a dictionary
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
                # Add the dictionary inside a list   
                restaurant_data.append(restaurant_row)

            print(len(postcode_in))

            # Pop "remove" the first element of the input list that represents the current iteraction
            postcode_in.pop(0)
            # Return call recursively the get_restaurant_data function to iteract with the next postcode
            return get_restaurant_data(postcode_in,restaurant_data)

        except:
            print("error!")
            # Pop "remove" the first element of the input list that represents the current iteraction
            postcode_in.pop(0)
            # Return call recursively the get_restaurant_data function to iteract with the next postcode
            return get_restaurant_data(postcode_in,restaurant_data)

    # transform list restaurant_data  into pd:DataFrame and return
    return pd.DataFrame(restaurant_data)