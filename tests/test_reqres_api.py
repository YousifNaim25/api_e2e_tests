import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"

Response = requests.get(BASE_URL)
print("Status Code:", Response.status_code)
print("Response Body:", Response.json())

for user in Response.json():
    print("User ID:", user['id'], "Name:", user['name'])