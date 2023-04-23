import requests
import random

LOCAL_DEV = False
# Define the API endpoint
if LOCAL_DEV:
    api_url = "http://localhost:5000/players"
else:
    api_url = "https://minesweeper-server.herokuapp.com/players"

# Add 5 test entries
test_players = []
for i in range(5):
    name = f"Test Player {i + 1}"
    score = random.randint(1, 100)
    payload = {"name": name, "score": score}
    response = requests.post(api_url, json=payload)
    print(response.json())
    test_players.append(response.json())

# Get all entries
response = requests.get(api_url)
players = response.json()["players"]
print("All players:")
for player in players:
    print(player)

# Remove the test entries
for player in test_players:
    player_id = player["id"]
    response = requests.delete(f"{api_url}/{player_id}")
    print(response.json())
