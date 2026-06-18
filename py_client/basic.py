import requests

endpoint = "https://mockhttp.org"

get_response = requests.get(endpoint)
print (get_response.text)
