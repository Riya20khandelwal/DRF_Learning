import requests

# endpoint = "https://httpbin.org/status/200/"
endpoint ="https://httpbin.org/anything"
# endpoint = "http://127.0.0.1:8000/"
endpoint = "http://localhost:8000/"

# get_response = requests.get(endpoint)  # HTTP Request
get_response = requests.get(endpoint, json={"query":"Hello World"})
# get_response = requests.get(endpoint, data={"query":"Hello World"})
print(get_response.text)    # Print raw text response

# print(get_response.json()) 
#  HTTP  Request -> HTML
# REST API HTTP Request -> JSON


# print(get_response.json()) 
print(get_response.status_code)