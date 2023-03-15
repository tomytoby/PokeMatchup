import requests

def get_pokemon(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    if not response.ok:
        return None
    pokemon_info = response.json()
    return pokemon_info

def get_pokemon_type(pokemon_name):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    if response.status_code == 200:
        pokemon_info = response.json()
        pokemon_type = pokemon_info['types'][0]['type']['name'].lower()
        return pokemon_type
    else:
        return None

def get_pokemon_sprite(pokemon):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
    if response.status_code == 200:
        return response.json()['sprites']['front_default']
    else:
        return None

def get_pokemon_fun_fact(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    if not response.ok:
        return f"Could not retrieve fun fact for {pokemon_name}"
    pokemon_fact = response.json()
    height = pokemon_fact['height'] / 3.048
    weight = pokemon_fact['weight'] / 4.536
    return f"Fun fact: {pokemon_name.capitalize()} is {height:.1f} feet tall and weighs {weight:.1f} pounds!"

def type_matchup(pokemon1, pokemon2):
    try:
        pokemon1_type = get_pokemon_type(pokemon1)
        pokemon2_type = get_pokemon_type(pokemon2)

        damage_response = requests.get(f'https://pokeapi.co/api/v2/type/{pokemon1_type}')
        damage_relations = damage_response.json()['damage_relations']

        pokemon1_sprite = get_pokemon_sprite(pokemon1)
        pokemon2_sprite = get_pokemon_sprite(pokemon2)

        pokemon1 = pokemon1.capitalize()
        pokemon2 = pokemon2.capitalize()

        for key, value in damage_relations.items():
            if pokemon2_type in [v['name'] for v in value]:
                if key == 'no_damage_to':
                    return f"{pokemon1} is not effective against {pokemon2}.", pokemon1_sprite, pokemon2_sprite
                elif key == 'half_damage_to':
                    return f"{pokemon1} is not very effective against {pokemon2}.", pokemon1_sprite, pokemon2_sprite
                elif key == 'double_damage_to':
                    return f"{pokemon1} is very effective against {pokemon2}!", pokemon1_sprite, pokemon2_sprite
        return f"{pokemon1} is somewhat effective against {pokemon2}.", pokemon1_sprite, pokemon2_sprite
    except:
        return None, None, None