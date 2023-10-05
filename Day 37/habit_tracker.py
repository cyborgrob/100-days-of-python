import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users/<YOUR_USERNAME>/graphs/<YOUR_GRAPH>'
token = 'YOUR_TOKEN'
headers = {
    'X-USER-TOKEN': token,
}

# These body parameters are used to create the initial graph
# body = {
#     'id': 'YOUR_GRAPH_ID',
#     'name': 'Coding',
#     'unit': 'hours',
#     'type': 'float',
#     'color': 'ajisai',
#     'timezone': 'YOUR_TIMEZONE'
# }

# Creates today's date in string format, formatted for the API
today = datetime.today()
today_string = today.strftime('%Y%m%d')

body = {
    'date': today_string,
    'quantity': '1',
}

# Make a new pixel on the graph for today's date and quantity
# response = requests.post(url=pixela_endpoint, json=body, headers=headers)
# print(response.text)


# Create user using params
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# user_params = {
#     'token': 'YOUR_TOKEN',
#     'username': 'YOUR_USERNAME',
#     'agreeTermsOfService': 'yes',
#     'notMinor': 'yes'
# }
