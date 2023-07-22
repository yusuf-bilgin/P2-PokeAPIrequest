import requests
import time

def get_pokemons():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/")
    if response.status_code == 200:
        print("Status: OK")
        time.sleep(2)
        return response.json()


def get_a_pokemon(u_input):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + u_input)
    if response.status_code == 200:
        print("Status: OK")
        time.sleep(2)
        return response.json()


pokemons_response = get_pokemons()


if pokemons_response:
    print("List of Pokémon Names:")
    # Print the name of pokemons
    for pokemon in pokemons_response['results']:
        print(pokemon['name'])

    u_input = input("Enter your Pokémon name: ")
    feature_response = get_a_pokemon(u_input)
    
    found = False
    # traversal in the list - pokemons_response['results'][pokemon]
    for pokemon in pokemons_response['results']:
        # traversal in the dictonary - pokemons_response['results'][pokemon]['name']
        if pokemon['name'] == u_input:
            found = True
            print("____Abilities____")
            
            for feature in feature_response['abilities']:
                print(feature['ability']['name'])
            
            print(f"Base experience: {feature_response['base_experience']}")

    if not found:
        print("Your Pokémon is not in the list.")
