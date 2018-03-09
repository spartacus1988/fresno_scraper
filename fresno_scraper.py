print("helloffefe")

import json


#data = {"bed":3,"miniBubbleType":1}

data = {"bed":3,"miniBubbleType":1,"image":"https://photos.zillowstatic.com/p_a/ISyfyo1ab0swkw1000000000.jpg","sqft":1641,"label":"$285K","isPropertyTypeVacantLand":False,"datasize":9,"title":"$285K","bath":2.5,"homeInfo":{"zpid": 2094098289,"streetAddress": "Canvas 2 Plan, Belterra","zipcode": "93727","city": "Fresno","state": "CA","latitude": 36.774371,"longitude": -119.681827,"price": 284950.0,"dateSold": 0,"bathrooms": 2.5,"bedrooms": 3.0,"livingArea": 1641.0,"yearBuilt": 2018,"lotSize": -1.0,"homeType": "SINGLE_FAMILY","homeStatus": "FOR_SALE","photoCount": 22,"imageLink": "https://photos.zillowstatic.com/p_g/ISyfyo1ab0swkw1000000000.jpg","daysOnZillow": 2,"isFeatured": True,"shouldHighlight": False,"brokerId": 15556,"contactPhone": "5594408398","group_type": "BUILDER_COMMUNITY","grouping_id": 771532,"grouping_name": "Belterra","zestimate": 298720,"listing_sub_type": {"is_newHome": True,"is_openHouse": True},"priceReduction": "","priceSuffix": "+","isUnmappable": False,"title": "Canvas 2 Plan","mediumImageLink": "https://photos.zillowstatic.com/p_c/ISyfyo1ab0swkw1000000000.jpg","isPreforeclosureAuction": False,"homeStatusForHDP": "FOR_SALE","priceForHDP": 284950.0,"festimate": 268848,"isListingOwnedByCurrentSignedInAgent": False,"timeOnZillow": 1520284560000,"isListingClaimedByCurrentSignedInUser": False,"hiResImageLink": "https://photos.zillowstatic.com/p_f/ISyfyo1ab0swkw1000000000.jpg","watchImageLink": "https://photos.zillowstatic.com/p_j/ISyfyo1ab0swkw1000000000.jpg","contactPhoneExtension": "","tvImageLink": "https://photos.zillowstatic.com/p_m/ISyfyo1ab0swkw1000000000.jpg","tvCollectionImageLink": "https://photos.zillowstatic.com/p_l/ISyfyo1ab0swkw1000000000.jpg","tvHighResImageLink": "https://photos.zillowstatic.com/p_n/ISyfyo1ab0swkw1000000000.jpg","zillowHasRightsToImages": False,"newConstructionType": "BUILDER_PLAN","desktopWebHdpImageLink": "https://photos.zillowstatic.com/p_h/ISyfyo1ab0swkw1000000000.jpg","hideZestimate": False,"isPremierBuilder": True}}


print(len(str(data)))

#data = {"bed":3,"miniBubbleType":1,"image":"https:\\/\\/photos.zillowstatic.com\\/p_a\\/ISyfyo1ab0swkw1000000000.jpg","sqft":1641,"label":"$285K","isPropertyTypeVacantLand":false,"datasize":9,"title":"$285K","bath":2.5,"homeInfo":{"zpid": 2094098289,"streetAddress": "Canvas 2 Plan, Belterra","zipcode": "93727","city": "Fresno","state": "CA","latitude": 36.774371,"longitude": \-119.681827,"price": 284950.0,"dateSold": 0,"bathrooms": 2.5,"bedrooms": 3.0,"livingArea": 1641.0,"yearBuilt": 2018,"lotSize": \-1.0,"homeType": "SINGLE_FAMILY","homeStatus": "FOR_SALE","photoCount": 22,"imageLink": "https://photos.zillowstatic.com/p_g/ISyfyo1ab0swkw1000000000.jpg","daysOnZillow": 2,"isFeatured": true,"shouldHighlight": false,"brokerId": 15556,"contactPhone": "5594408398","group_type": "BUILDER_COMMUNITY","grouping_id": 771532,"grouping_name": "Belterra","zestimate": 298720,"listing_sub_type": {"is_newHome": true,"is_openHouse": true},"priceReduction": "","priceSuffix": "+","isUnmappable": false,"title": "Canvas 2 Plan","mediumImageLink": "https://photos.zillowstatic.com/p_c/ISyfyo1ab0swkw1000000000.jpg","isPreforeclosureAuction": false,"homeStatusForHDP": "FOR_SALE","priceForHDP": 284950.0,"festimate": 268848,"isListingOwnedByCurrentSignedInAgent": false,"timeOnZillow": 1520284560000,"isListingClaimedByCurrentSignedInUser": false,"hiResImageLink": "https://photos.zillowstatic.com/p_f/ISyfyo1ab0swkw1000000000.jpg","watchImageLink": "https://photos.zillowstatic.com/p_j/ISyfyo1ab0swkw1000000000.jpg","contactPhoneExtension": "","tvImageLink": "https://photos.zillowstatic.com/p_m/ISyfyo1ab0swkw1000000000.jpg","tvCollectionImageLink": "https://photos.zillowstatic.com/p_l/ISyfyo1ab0swkw1000000000.jpg","tvHighResImageLink": "https://photos.zillowstatic.com/p_n/ISyfyo1ab0swkw1000000000.jpg","zillowHasRightsToImages": false,"newConstructionType": "BUILDER_PLAN","desktopWebHdpImageLink": "https://photos.zillowstatic.com/p_h/ISyfyo1ab0swkw1000000000.jpg","hideZestimate": false,"isPremierBuilder": true}}

#print(str(data))

#str(data).replace('\\', '')

data = str(data)

data = data[1:]
print(data)

data = data[:-1]


print(data)



data = str(data).split(',')

result = None

for item in data:
    newitem = item.split(':')
    for res in newitem:
        print(res)
        #print(len(res))
        #if res == " 'zestimate'":
        if "zestimate" in res:

            result = newitem
            break

if result is None:
    result = "N/A"



print(result)

print(result[1])




#print(str(data))



#data = {"bed":3,"miniBubbleType":1,"image":"https://photos.zillowstatic.com/p_a/ISyfyo1ab0swkw1000000000.jpg","sqft":1641,"label":"$285K","isPropertyTypeVacantLand":False,"datasize":9,"title":"$285K","bath":2.5,"homeInfo":{"zpid": 2094098289,"streetAddress": "Canvas 2 Plan, Belterra","zipcode": "93727","city": "Fresno","state": "CA","latitude": 36.774371,"longitude": -119.681827,"price": 284950.0,"dateSold": 0,"bathrooms": 2.5,"bedrooms": 3.0,"livingArea": 1641.0,"yearBuilt": 2018,"lotSize": -1.0,"homeType": "SINGLE_FAMILY","homeStatus": "FOR_SALE","photoCount": 22,"imageLink": "https://photos.zillowstatic.com/p_g/ISyfyo1ab0swkw1000000000.jpg","daysOnZillow": 2,"isFeatured": True,"shouldHighlight": False,"brokerId": 15556,"contactPhone": "5594408398","group_type": "BUILDER_COMMUNITY","grouping_id": 771532,"grouping_name": "Belterra","zestimate": 298720,"listing_sub_type": {"is_newHome": True,"is_openHouse": True},"priceReduction": "","priceSuffix": "+","isUnmappable": False,"title": "Canvas 2 Plan","mediumImageLink": "https://photos.zillowstatic.com/p_c/ISyfyo1ab0swkw1000000000.jpg","isPreforeclosureAuction": False,"homeStatusForHDP": "FOR_SALE","priceForHDP": 284950.0,"festimate": 268848,"isListingOwnedByCurrentSignedInAgent": False,"timeOnZillow": 1520284560000,"isListingClaimedByCurrentSignedInUser": False,"hiResImageLink": "https://photos.zillowstatic.com/p_f/ISyfyo1ab0swkw1000000000.jpg","watchImageLink": "https://photos.zillowstatic.com/p_j/ISyfyo1ab0swkw1000000000.jpg","contactPhoneExtension": "","tvImageLink": "https://photos.zillowstatic.com/p_m/ISyfyo1ab0swkw1000000000.jpg","tvCollectionImageLink": "https://photos.zillowstatic.com/p_l/ISyfyo1ab0swkw1000000000.jpg","tvHighResImageLink": "https://photos.zillowstatic.com/p_n/ISyfyo1ab0swkw1000000000.jpg","zillowHasRightsToImages": False,"newConstructionType": "BUILDER_PLAN","desktopWebHdpImageLink": "https://photos.zillowstatic.com/p_h/ISyfyo1ab0swkw1000000000.jpg","hideZestimate": False,"isPremierBuilder": True}}
#
#
# print(str(type(data)))
#
# data = json.dumps(data)


#data = str({"bed":3,"miniBubbleType":1})

#{"bed":3,"miniBubbleType":1,"image":"https:\\/\\/photos.zillowstatic.com\\/p_a\\/ISyfyo1ab0swkw1000000000.jpg","sqft":1641,"label":"$285K","isPropertyTypeVacantLand":false,"datasize":9,"title":"$285K","bath":2.5,"homeInfo":{"zpid": 2094098289,"streetAddress": "Canvas 2 Plan, Belterra","zipcode": "93727","city": "Fresno","state": "CA","latitude": 36.774371,"longitude": \-119.681827,"price": 284950.0,"dateSold": 0,"bathrooms": 2.5,"bedrooms": 3.0,"livingArea": 1641.0,"yearBuilt": 2018,"lotSize": \-1.0,"homeType": "SINGLE_FAMILY","homeStatus": "FOR_SALE","photoCount": 22,"imageLink": "https://photos.zillowstatic.com/p_g/ISyfyo1ab0swkw1000000000.jpg","daysOnZillow": 2,"isFeatured": true,"shouldHighlight": false,"brokerId": 15556,"contactPhone": "5594408398","group_type": "BUILDER_COMMUNITY","grouping_id": 771532,"grouping_name": "Belterra","zestimate": 298720,"listing_sub_type": {"is_newHome": true,"is_openHouse": true},"priceReduction": "","priceSuffix": "+","isUnmappable": false,"title": "Canvas 2 Plan","mediumImageLink": "https://photos.zillowstatic.com/p_c/ISyfyo1ab0swkw1000000000.jpg","isPreforeclosureAuction": false,"homeStatusForHDP": "FOR_SALE","priceForHDP": 284950.0,"festimate": 268848,"isListingOwnedByCurrentSignedInAgent": false,"timeOnZillow": 1520284560000,"isListingClaimedByCurrentSignedInUser": false,"hiResImageLink": "https://photos.zillowstatic.com/p_f/ISyfyo1ab0swkw1000000000.jpg","watchImageLink": "https://photos.zillowstatic.com/p_j/ISyfyo1ab0swkw1000000000.jpg","contactPhoneExtension": "","tvImageLink": "https://photos.zillowstatic.com/p_m/ISyfyo1ab0swkw1000000000.jpg","tvCollectionImageLink": "https://photos.zillowstatic.com/p_l/ISyfyo1ab0swkw1000000000.jpg","tvHighResImageLink": "https://photos.zillowstatic.com/p_n/ISyfyo1ab0swkw1000000000.jpg","zillowHasRightsToImages": false,"newConstructionType": "BUILDER_PLAN","desktopWebHdpImageLink": "https://photos.zillowstatic.com/p_h/ISyfyo1ab0swkw1000000000.jpg","hideZestimate": false,"isPremierBuilder": true}}


#print(str(type(data)))









# data = json.loads(data)
#
#
#
# print(data)
# print(str(type(data)))
# print(data["bed"])





#{"bed":3,"miniBubbleType":1,"image":"https:\\/\\/photos.zillowstatic.com\\/p_a\\/ISyfyo1ab0swkw1000000000.jpg","sqft":1641,"label":"$285K","isPropertyTypeVacantLand":false,"datasize":9,"title":"$285K","bath":2.5,"homeInfo":{"zpid": 2094098289,"streetAddress": "Canvas 2 Plan, Belterra","zipcode": "93727","city": "Fresno","state": "CA","latitude": 36.774371,"longitude": \-119.681827,"price": 284950.0,"dateSold": 0,"bathrooms": 2.5,"bedrooms": 3.0,"livingArea": 1641.0,"yearBuilt": 2018,"lotSize": \-1.0,"homeType": "SINGLE_FAMILY","homeStatus": "FOR_SALE","photoCount": 22,"imageLink": "https://photos.zillowstatic.com/p_g/ISyfyo1ab0swkw1000000000.jpg","daysOnZillow": 2,"isFeatured": true,"shouldHighlight": false,"brokerId": 15556,"contactPhone": "5594408398","group_type": "BUILDER_COMMUNITY","grouping_id": 771532,"grouping_name": "Belterra","zestimate": 298720,"listing_sub_type": {"is_newHome": true,"is_openHouse": true},"priceReduction": "","priceSuffix": "+","isUnmappable": false,"title": "Canvas 2 Plan","mediumImageLink": "https://photos.zillowstatic.com/p_c/ISyfyo1ab0swkw1000000000.jpg","isPreforeclosureAuction": false,"homeStatusForHDP": "FOR_SALE","priceForHDP": 284950.0,"festimate": 268848,"isListingOwnedByCurrentSignedInAgent": false,"timeOnZillow": 1520284560000,"isListingClaimedByCurrentSignedInUser": false,"hiResImageLink": "https://photos.zillowstatic.com/p_f/ISyfyo1ab0swkw1000000000.jpg","watchImageLink": "https://photos.zillowstatic.com/p_j/ISyfyo1ab0swkw1000000000.jpg","contactPhoneExtension": "","tvImageLink": "https://photos.zillowstatic.com/p_m/ISyfyo1ab0swkw1000000000.jpg","tvCollectionImageLink": "https://photos.zillowstatic.com/p_l/ISyfyo1ab0swkw1000000000.jpg","tvHighResImageLink": "https://photos.zillowstatic.com/p_n/ISyfyo1ab0swkw1000000000.jpg","zillowHasRightsToImages": false,"newConstructionType": "BUILDER_PLAN","desktopWebHdpImageLink": "https://photos.zillowstatic.com/p_h/ISyfyo1ab0swkw1000000000.jpg","hideZestimate": false,"isPremierBuilder": true}}





import time
import pandas as pd
from bs4 import BeautifulSoup
import zillow_functions as zl


st = zl.zipcodes_list(st_items = ["93727"])


# Initialize the webdriver.
driver = zl.init_driver('/usr/local/share/chromedriver')

# Go to www.zillow.com/homes
zl.navigate_to_website(driver, "http://www.zillow.com/homes")


# Click the "buy" button.
zl.click_buy_button(driver)


# Get total number of search terms.
num_search_terms = len(st)


# Initialize list obj that will house all scraped data.
output_data = []



# Start the scraping.
for idx, term in enumerate(st):
    # Enter search term and execute search.
    if zl.enter_search_term(driver, term):
        print("Entering search term %s of %s" %
              (str(idx + 1), str(num_search_terms)))
    else:
        print("Search term %s failed, moving on to next search term\n***" %
              str(idx + 1))
        continue

    # Check to see if any results were returned from the search.
    # If there were none, move onto the next search.
    if zl.test_for_no_results(driver):
        print("Search %s returned zero results. Moving on to next search\n***" %
              str(term))
        continue

    # Pull the html for each page of search results. Zillow caps results at
    # 20 pages, each page can contain 26 home listings, thus the cap on home
    # listings per search is 520.
    raw_data = zl.get_html(driver)
    print("%s pages of listings found" % str(len(raw_data)))

    # Take the extracted HTML and split it up by individual home listings.
    listings = zl.get_listings(raw_data)
    print("%s home listings scraped\n***" % str(len(listings)))

    # For each home listing, extract the 11 variables that will populate that
    # specific observation within the output dataframe.
    for home in listings:
        soup = BeautifulSoup(home, "lxml")
        new_obs = []

        print("soup_is: " + str(soup))


        # List that contains number of beds, baths, and total sqft (and
        # sometimes price as well).
        card_info = zl.get_card_info(soup)

        # Street Address
        new_obs.append(zl.get_street_address(soup))

        # City
        new_obs.append(zl.get_city(soup))

        # State
        new_obs.append(zl.get_state(soup))

        # Zipcode
        new_obs.append(zl.get_zipcode(soup))

        # Price
        new_obs.append(zl.get_price(soup, card_info))

        # Sqft
        new_obs.append(zl.get_sqft(card_info))

        # Bedrooms
        new_obs.append(zl.get_bedrooms(card_info))

        # Bathrooms
        new_obs.append(zl.get_bathrooms(card_info))

        # Days on the Market/Zillow
        new_obs.append(zl.get_days_on_market(soup))

        # Sale Type (House for Sale, New Construction, Foreclosure, etc.)
        new_obs.append(zl.get_sale_type(soup))

        # URL for each house listing
        new_obs.append(zl.get_url(soup))





        # Append new_obs to list output_data.
        output_data.append(new_obs)
        #break

# Close the webdriver connection.
zl.close_connection(driver)




# Write data to data frame, then to CSV file.
file_name = "%s_%s.csv" % (str(time.strftime("%Y-%m-%d")),
                           str(time.strftime("%H%M%S")))
columns = ["address", "city", "state", "zip", "price", "sqft", "bedrooms",
           "bathrooms", "days_on_zillow", "sale_type", "url", "zestimate", "Build_in", "Community_Name"]
pd.DataFrame(output_data, columns = columns).to_csv(file_name, index = False)
