import json
import requests

url = "http://rhymescapes.net/fll_get_data/1"
response = requests.get(url)

if response.status_code == 200:
    responseJson = json.dumps(response.json(), indent=4)
    print(responseJson)
else:
    print(f"Error: {response.status_code}")

