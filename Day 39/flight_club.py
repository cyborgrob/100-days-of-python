import requests
import datetime

SHEETY_URL = 'YOUR_SHEETY_URL'

KIWI_SEARCH_URL = 'https://api.tequila.kiwi.com/v2/search'
KIWI_LOCATIONS_URL = 'https://api.tequila.kiwi.com/locations/query'
KIWI_API_KEY = 'YOUR_KIWI_API_KEY'
KIWI_HEADERS = {
    'apikey': KIWI_API_KEY,
}


# This function will update the IATA codes of your desired destination cities (if they're not there already). First
# pulls info from Flight Deals sheet using Sheety endpoint/get method. Converts response into variable 'data'. Then
# goes through the data and for each city name, calls the Kiwi API to find its city/airport IATA code. It then calls
# the Sheety API again to put the IATA code into the sheet in the proper position.
def update_destination_codes():
    sheety_fun_resp = requests.get(url=SHEETY_URL)
    sheety_fun_resp.raise_for_status()
    sheety_data = sheety_fun_resp.json()

    for city in sheety_data['prices']:
        kiwi_iata_params = {
            'term': city['city'],
            'location_types': 'city',
        }

        kiwi_resp = requests.get(url=KIWI_LOCATIONS_URL, headers=KIWI_HEADERS, params=kiwi_iata_params)
        kiwi_data = kiwi_resp.json()
        city_code = kiwi_data['locations'][0]['code']

        body = {
            'price': {
                'iataCode': city_code,
            }
        }
        sheety_fun_resp = requests.put(url=SHEETY_URL + f"/{city['id']}", json=body)
        print(sheety_fun_resp.text)


# Get sheet data
sheety_resp = requests.get(url=SHEETY_URL)
sheety_resp.raise_for_status()
data = sheety_resp.json()
sheet_data = data['prices']

# Creates list from sheet data. Includes city name, IATA code, and the max price willing to pay
city_and_price_list = [[item['city'], item['iataCode'], item['lowestPrice']] for item in sheet_data]

# Creating date string variables
now = datetime.datetime.today()
tom_delta = datetime.timedelta(days=1)
six_month_delta = datetime.timedelta(days=180)
TOMORROW = (now + tom_delta).strftime("%d/%m/%Y")
SIX_MONTHS = (now + six_month_delta).strftime("%d/%m/%Y")

# Your flight info
MY_CITY = 'YOUR_IATA_CODE'
MIN_NIGHTS = 3
MAX_NIGHTS = 20

# For each city in your sheet, will check to see if there are any roundtrip flights to that city under your max
# price. If there are, will print to the console (can also be configured to send email, SMS, etc). If there aren't,
# will print "nothing found" for that city.
for destination in city_and_price_list:
    kiwi_params = {
        'fly_from': MY_CITY,
        'fly_to': destination[1],
        'date_from': TOMORROW,
        'date_to': SIX_MONTHS,
        'nights_in_dst_from': MIN_NIGHTS,
        'nights_in_dst_to': MAX_NIGHTS,
        'curr': 'USD',
        'limit': 1,
        'price_to': destination[2],
        'max_stopovers': 3,
    }

    kiwi_resp = requests.get(url=KIWI_SEARCH_URL, headers=KIWI_HEADERS, params=kiwi_params)
    kiwi_resp.raise_for_status()
    data = kiwi_resp.json()
    if data['data']:
        fare = data['data'][0]['fare']['adults']
        local_departure = data['data'][0]['local_departure']
        destination_departure = data['data'][0]['route'][1]['local_departure']
        print(destination[0] + ': $' + str(fare))
        print(f"Flight leaves {MY_CITY} at on {local_departure} and flies back on {destination_departure}.\n")

    else:
        print(destination[0] + ": nothing found\n")
