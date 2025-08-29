import requests

def find_leaderboards():

  API_KEY = 'your_api_key'

  headers = {'Authorization': f'Bearer {API_KEY}'}

  leaderboards_url = 'https://api.clashroyale.com/v1/leaderboards'

  leaderboards_response = requests.get(leaderboards_url, headers=headers)
  leaderboards_json = leaderboards_response.json()
  leaderboards_dict = leaderboards_json.get("items",[])

  filtered_leaderboards = [
          {key: l[key] for key in ['id'] if key in l}
          for l in leaderboards_dict]

  ids = [i["id"] for i in filtered_leaderboards]
  return ids
