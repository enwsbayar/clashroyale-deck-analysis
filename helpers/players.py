from leaderboards import find_leaderboards
import requests

leaderboards = find_leaderboards()
leaderboards_length = len(leaderboards)

API_KEY = 'your_api_key'

headers = {'Authorization': f'Bearer {API_KEY}'}
playersList = []
for i in range(leaderboards_length):
  leaderboard_id = leaderboards[i]
  players_url = f'https://api.clashroyale.com/v1/leaderboard/{leaderboard_id}'
  players_response = requests.get(players_url, headers = headers)
  players_json = players_response.json()
  players_dict = players_json.get("items",[])

  filtered_players= [
          {key: l[key] for key in ['tag'] if key in l}
          for l in players_dict]

  player_tags = [i["tag"] for i in filtered_players]
  playersList.extend(player_tags)

with open("./data/players.txt", "w") as f:
    for player in playersList:
        f.write(f"{player}\n")


  
