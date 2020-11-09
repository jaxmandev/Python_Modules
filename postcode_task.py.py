import requests
import json

# arguement = input("Please enter your post code: ")
# url_target = live_response + arguement

# how to convert this datatype 'bytes' into dictionary
# hINT: python json library
# then iterate through the data and print RESULTS
# print the longitudinal and latitudinal coordinates
# create a function that returns the longitude and latitude of the given postcode
# use input to get the given postcode

# print(str(live_response.content))

def longi_lati():
    # asks user to input a postcode
    arg = input("Please enter your postcode: ")
    postcode = "http://api.postcodes.io/postcodes/" + arg

    # this gets the status code from the site
    # if not valid, the function ends
    response = requests.get(postcode)
    print(response.status_code)
    if not response.status_code == 200:
        return print("Sorry, not in database")
   
    # this receives the content from the API
    val_1 = response.content
    # i use json.loads() to turn the bytes into a dictionary
    dic = json.loads(val_1)

    # as required, I print out the latitude and longitude of the postcode
    print(f"latitude: {dic['result']['latitude']}")
    print(f"longitude: {dic['result']['longitude']}")

    # i put this in so people can choose when to see the rest of the results
    input("\nPress enter to see results")
    
    # this prints out the rest of the results that the API returns
    for key, value in dic['result'].items():
        print(f"{key} : {value}")

longi_lati()