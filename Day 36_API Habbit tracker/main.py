import requests

USERNAME = "sonianshika"
TOKEN = "ksdk23asjd345khks3l4"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cylic graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

response = requests.post(url=graph_endpoint, json=graph_config)
print(response.text)


