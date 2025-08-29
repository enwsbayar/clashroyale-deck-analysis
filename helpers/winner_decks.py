import requests
import time

with open("./data/players.txt", "r") as f:
    players = [(line.strip()) for line in f]

winner_decks = []

API_KEY = 'your_api_key'  
headers = {'Authorization': f'Bearer {API_KEY}'}

start_time = time.time()

for player in players:
    player_tag = player.replace("#", "%23")
    battlelogs_url = f'https://api.clashroyale.com/v1/players/{player_tag}/battlelog'
    response = requests.get(battlelogs_url, headers=headers)
    time.sleep(2)
    if response.status_code != 200:
        print(f"{player} no data: {response.status_code}")
        continue

    try:
        battlelogs = response.json()
    except ValueError:
        print(f"{player} JSON error")
        continue

    if not isinstance(battlelogs, list):
        print(f"{player} not battlelogs list")
        continue

    for battlelog in battlelogs:
        if battlelog.get("type") not in ["classic", "PvP", "pathOfLegend"]:
            continue
        try:
            team_crowns = battlelog['team'][0]['crowns']
            opponent_crowns = battlelog['opponent'][0]['crowns']
        except (KeyError, IndexError, TypeError):
            continue

        if team_crowns > opponent_crowns:
            winner_cards = [card['id'] for card in battlelog['team'][0]['cards']]
        elif opponent_crowns > team_crowns:
            winner_cards = [card['id'] for card in battlelog['opponent'][0]['cards']]
        else:
            winner_cards = []

        if winner_cards:
            winner_decks.append(winner_cards[:8])

            if len(winner_decks) % 1000 == 0:
                elapsed = time.time() - start_time
                minutes, seconds = divmod(int(elapsed), 60)
                print(f"{len(winner_decks)}/{len(players)*len(battlelogs)} decks collected, elapsed time: {minutes}m {seconds}s")

        with open("./data/winner_decks.txt", "w") as f:
            for deck in winner_decks:
                f.write(f"{deck}\n")

        with open("./data/winner_cards.txt", "w") as f:
            for deck in winner_decks:
                for card in deck:
                    f.write(f"{card}\n")
