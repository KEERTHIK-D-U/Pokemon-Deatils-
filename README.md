# Pokémon Info Fetcher

This is a Python project that connects to the [PokeAPI](https://pokeapi.co/) to fetch and display information about Pokémon.  
It retrieves details like the Pokémon's name, ID, weight, height, and abilities based on user input.

## Features
- Connects to a public API using Python's `requests` library.
- Takes Pokémon name as input from the user.
- Displays:
  - Name
  - ID
  - Weight
  - Height
  - Abilities

## Requirements
- Python 3.x
- `requests` library

You can install the required package using:
pip install requests
How to Run
Open a terminal.

Run the Python file:

bash
Copy
Edit
python yourfilename.py
Enter the name of the Pokémon when prompted.

Example
vbnet
Copy
Edit
Enter the Pokemon name you want info on: pikachu

Name: Pikachu
Id: 25
Weight: 60
Height: 4
Abilities: static, lightning-rod

## API Source
Data is fetched from: https://pokeapi.co/
