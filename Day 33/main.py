import requests
from datetime import datetime
import smtplib

# Set your latitude and longitude here, as well as UTC offset if applicable (see below)
MY_LAT = 60
MY_LNG = -60
UTC_OFFSET = -4


def is_iss_overhead():
    # Gets ISS position and saves lat and long into variables
    resp = requests.get(url='http://api.open-notify.org/iss-now.json')
    resp.raise_for_status()
    data = resp.json()
    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])

    # Checks if ISS lat and long are in the vicinity of your own lat and long. Returns True/False
    if (MY_LAT - 10) < iss_latitude < (MY_LAT + 10):
        if (MY_LNG - 10) < iss_longitude < (MY_LNG + 10):
            return True
        else:
            return False
    else:
        return False


def is_nighttime():
    params = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    # Uses your lat/long to check if it's currently nighttime
    resp = requests.get(url='https://api.sunrise-sunset.org/json', params=params)
    resp.raise_for_status()

    # This very simply adjusts UTC time to local time by adding my local offset (-4). For my situation this will
    # likely work nearly all the time, as it's very unlikely for sunrise to occur before midnight or sunset to occur
    # after midnight. But depending on your time zone you may need to introduce a conditional such that if the result
    # is negative or greater than 24, adjustments should be made
    sunrise = int(resp.json()['results']['sunrise'].split('T')[1].split(":")[0]) + UTC_OFFSET
    sunset = int(resp.json()['results']['sunset'].split('T')[1].split(":")[0]) + UTC_OFFSET
    now = datetime.now()

    # If current time is outside daytime hours (eg, it's nighttime), returns True
    if now.hour > sunset or now.hour < sunrise:
        return True
    else:
        return False


# Checks if it's both nighttime and the ISS is overhead. If it is, sends an email. Note: Can simply use the same email
# instead of having a separate from/to email
if is_iss_overhead() and is_nighttime():
    from_email = 'YOUR_FROM_EMAIL'
    password = 'YOUR_PASSWORD'
    to_email = 'YOUR_TO_EMAIL'

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(from_addr=from_email, to_addrs=to_email,
                            msg="Subject: The ISS is Overhead!\n\nHurry up and run outside to look!")
