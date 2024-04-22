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
response = requests.post(pixela_endpoint, json=user_params)
print(response.text)



graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

requests.post()


