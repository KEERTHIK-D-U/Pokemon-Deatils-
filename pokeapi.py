# How to connect to api in Python
# to use the request we have to include the request model
# use pip install requests

import requests

base_url = "https://pokeapi.co/api/v2/"  # PokeAPI base URL

def get_poke_info(name):
    url = f"{base_url}pokemon/{name}"
    response = requests.get(url)
    # print(response)

    if response.status_code == 200:
        # print("Data Retrieved")
        pokemon_data = response.json()  # storing the data in a dict
        return pokemon_data
    else:
        print(f"Failed to get the data. Status = {response.status_code}")
        return None  

pokemon_name = input("Enter the Pokemon name you want info on: ").lower()
pokemon_info = get_poke_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"Id: {pokemon_info['id']}")
    print(f"Weight: {pokemon_info['weight']}")
    print(f"Height: {pokemon_info['height']}")
    abilities = [a['ability']['name'] for a in pokemon_info['abilities']]
    print(f"Abilities: {', '.join(abilities)}")
