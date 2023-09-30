import requests
import datetime
import os

# 'MY_API_KEY' is my API stored as an environment variable within PyCharm. Can be accessed/changed by editing Run
# Configuration in the top right
api_key = os.environ.get('MY_API_KEY')
url = 'https://api.openweathermap.org/data/2.8/onecall'
lat = 65.464565
lon = -25.619961

params = {
    'lat': lat,
    'lon': lon,
    'appid': api_key,
    'units': 'imperial',
    'exclude': ['current,minutely,daily,alerts'],
}

resp = requests.get(url=url, params=params)
resp.raise_for_status()

data = resp.json()
# Uses a slice to get the info for the next 24 or 12 hours, advised to bring umbrella if rain in forecast
for hour in data['hourly'][:24]:
    uts_time = hour['dt']
    local_time = datetime.datetime.fromtimestamp(uts_time)
    print(hour['temp'], local_time)

for hour in data['hourly'][:12]:
    if hour['weather'][0]['id'] < 700:
        print("Bring an umbrella.")
        break
