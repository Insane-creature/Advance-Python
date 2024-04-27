import requests

USERNAME = "sonianshika"
TOKEN = "ksdk23asjd345khks3l4"
graphID = "graph1"

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
    "id": graphID,
    "name": "Cylic graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
 
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graphID}"
pixel_data = {
    "data": "20240427",
    "quantity": "5.3",

}

response1 = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response1.text)