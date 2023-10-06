import os
import requests
import datetime

# Info for authorization and payloads
APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')
GENDER = 'male'
WEIGHT_KG = 75.75
HEIGHT_CM = 180.0
AGE = 34
DATE = datetime.datetime.now().strftime('%#m/%#d/%Y')
TIME = datetime.datetime.now().strftime('%#I:%M %p')
TOKEN = os.environ.get('TOKEN')
BEARER = os.environ.get('BEARER')

# API endpoints and input text
nutrients_url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
exercise_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
tracker_url = os.environ.get('TRACKER_URL')
exercise_text = input("What exercise(s) did you do? ")

# Headers for trackapi
exercise_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': '0',
    'Content-Type': 'application/json'
}

# Payload for trackapi. Trackapi converts real human language/input into an exercise and calories burned
exercise_payload = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

# POST request made to trackapi
exercise_resp = requests.post(url=exercise_url, json=exercise_payload, headers=exercise_headers)
exercises = exercise_resp.json()

# For each exercise in the response (if there are multiple), parses out the data and uploads info to spreadsheet using sheety
for exercise in exercises['exercises']:
    workout = exercise['name']
    duration = exercise['duration_min']
    calories = exercise['nf_calories']

    # Headers for sheety
    tracker_headers = {
        'Authorization': f'Bearer {BEARER}',
    }

    # Payload for sheety
    tracker_payload = {
        'sheet1': {
            'date': DATE,
            'time': TIME,
            'exercise': workout,
            'duration': duration,
            'calories': calories,
        }
    }

    sheety_response = requests.post(url=tracker_url, json=tracker_payload, headers=tracker_headers)
    print(sheety_response.text)