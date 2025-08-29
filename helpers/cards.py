import requests

def find_cards():

    API_KEY = 'your_api_key'

    headers = {'Authorization': f'Bearer {API_KEY}'}

    cards_url = 'https://api.clashroyale.com/v1/cards'

    cards_response = requests.get(cards_url, headers=headers)
    cards_json = cards_response.json()
    cards_dict = cards_json.get("items",[])

    filtered_cards = [
        {key: card[key] for key in ['name', 'id', 'elixirCost', 'rarity'] if key in card}
        for card in cards_dict]
    
    return filtered_cards


