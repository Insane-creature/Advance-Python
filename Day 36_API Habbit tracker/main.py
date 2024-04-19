import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "ksdk23asjd345khks3l4",
    "username": "sonianshika",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(pixela_endpoint, json=user_params)
print(response.text)