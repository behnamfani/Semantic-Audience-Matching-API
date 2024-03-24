import requests
import json

# Call the match endpoint of the running API
url = "http://127.0.0.1:8000/match"
payload = {'input_segments': ["segment1", "segment2"]}
response = requests.get(url, json=payload)
print(json.dumps(response.json(), indent=3))
