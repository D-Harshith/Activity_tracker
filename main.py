import requests
from datetime import datetime

# Check url: https://pixe.la/v1/users/harshith/graphs/graph1.html
USER_NAME = "harshith"
TOKEN = "l1d2m3c4r5g6r7b8"
GRAPH_ID = "graph1"

# Creating a user.
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Meditation graph",
    "unit": "Sec",
    "type": "float",
    "color": "sora"
}

header = {
    "X-USER-TOKEN": TOKEN
}
# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=header)
# print(graph_response.text)
inp = input("Add today's work?Y/N ").upper()
if inp == "Y":
    data = int(input("What is the activity time?: "))*60
    today = datetime.now()
    pixel_params = {
        "date": today.strftime("%Y%m%d"),
        "quantity": str(data)
    }

    pixel_url = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

    pixel_response = requests.post(url=pixel_url, json=pixel_params, headers=header)
    print(pixel_response.text)

string = input("Update a pixel?Y/N ").upper()
if string == "Y":
    # Pixel update
    date = input("Enter a date:(YYYYMMDD) ")
    put_url = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{date}"
    qty = float(input("Enter the quantity: "))*60

    put_params = {
        "quantity": f"{qty}"
    }

    pixel_update = requests.put(url=put_url, json=put_params, headers=header)
    print(pixel_update.text)
