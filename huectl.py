import requests
import argparse
import json

""" Todo
- Get the internal ip from this link, automatically: https://discovery.meethue.com/
"""

parser = argparse.ArgumentParser(description='Control your huelights from the cli')

# Add arguments
parser.add_argument('--ip', type=str, help='IP of your bridge')
parser.add_argument('--user', type=str, help='Your user token')
parser.add_argument('--light', type=str, help='ID of the light you want to control')
parser.add_argument('--on', type=str, help='Turn on a light')
parser.add_argument('--off', type=str, help='Turn off a light')
parser.add_argument('--brightness', type=str, help='Set the brightness of a light') # todo: implement

# Parse the arguments
args = parser.parse_args()

if args.ip and args.user:
    bridgeIP = args.ip
    userToken = args.user
    
    url = f"http://{bridgeIP}/api/{userToken}"
else:
    print("Specify the bridge ip and user token with --ip and --user arguments")

# METHODS #

def controlLight(data, lightNumber):
    headers = {'Content-Type': 'application/json'}

    # Convert the data dictionary to a JSON string
    json_data = json.dumps(data)
   
    # Make the PUT request
    path = f"/lights/{lightNumber}/state"
    response = requests.put(url + path, data=json_data, headers=headers)
    
    # Check the status code and the response
    status(response)

# Utils #
def status(response):
    """Return the status for the response"""
    if response.status_code == 200:
        print('GET request was successful')
        print('Response data:', response.json())
    else:
        print(f'Error: {response.status_code}')
        print('Response text:', response.text)

# Main #
if args.light:
    if args.on:
        data = {'on': True}
        controlLight(data, args.light)
    elif args.off:
        data = {'on': False}
        controlLight(data, args.light)
    else:
        print("Specify light state with --on or --off argument  ")
