import requests

endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, data = {"query" : "This is the endpoint"})
print (get_response.text)
