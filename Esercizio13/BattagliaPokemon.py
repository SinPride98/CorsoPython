#combattimenti tra pokemon nel fie json
import json
from random import choice
import pandas as pd

CRITICO = 2 #moltiplicatore critico

def carica_pokemon(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def calcola_danno(attaccante, difensore):
    attacco = int(attaccante['Attack'])
    difesa = int(difensore['Defense'])
    velocita = int(attaccante['Speed'])
    velocita_difensore =int(difensore['Speed'])
    
    


    # Calcolo del moltiplicatore di tipo
    df= pd.read_csv('Esercizio13/tabella_tipi_completa.csv', index_col=0)
    tipo_attaccante = attaccante['Type 1']
    tipo_difensore = difensore['Type 1']
    if tipo_attaccante in df.index and tipo_difensore in df.columns:
        moltiplicatore_tipo = df.loc[tipo_attaccante, tipo_difensore]
        attacco *= moltiplicatore_tipo
        if moltiplicatore_tipo > 1:
            print("È super efficace!")
        elif moltiplicatore_tipo < 1 and moltiplicatore_tipo > 0:
            print("Non è molto efficace...")
        elif moltiplicatore_tipo == 0:
            print("Non ha effetto...")
    else:
        print("Tipo non riconosciuto, nessun bonus di tipo applicato.")

    # Calcolo del critico
    if velocita > velocita_difensore and choice([True, False, False, False, False, False, False, False, False, False]):
        attacco*= CRITICO
        print(f"Colpo critico di {attaccante['Name']}!")
    elif velocita <= velocita_difensore and choice([True, False, False, False, False, False, False, False, False, False]):
        attacco = 0
        print(f"Colpo evitato da {difensore['Name']}!")
    
    danno_base = (attacco ) - (difesa )
    danno_base = max(danno_base, 0)  # Il danno minimo è 1
    return int(danno_base)




def battaglia(pokemon1, pokemon2):
    vitaPokemon1 = int(pokemon1['HP'])
    vitaPokemon2= int(pokemon2['HP'])
    print(f"Inizia la battaglia tra {pokemon1['Name']} e {pokemon2['Name']}!")
    while vitaPokemon1 > 0 and vitaPokemon2 > 0:
        danno_a_pokemon2 = calcola_danno(pokemon1, pokemon2)
        vitaPokemon2 -= danno_a_pokemon2
        print(f"{pokemon1['Name']} attacca {pokemon2['Name']} e infligge {danno_a_pokemon2} danni. {pokemon2['Name']} ha ora {max(vitaPokemon2, 0)} HP.")
        if vitaPokemon2 <= 0:
            print(f"{pokemon2['Name']} è stato sconfitto! {pokemon1['Name']} vince!")
            break

        danno_a_pokemon1 = calcola_danno(pokemon2, pokemon1)
        vitaPokemon1 -= danno_a_pokemon1
        print(f"{pokemon2['Name']} attacca {pokemon1['Name']} e infligge {danno_a_pokemon1} danni. {pokemon1['Name']} ha ora {max(vitaPokemon1, 0)} HP.")
        if vitaPokemon1 <= 0:
            print(f"{pokemon1['Name']} è stato sconfitto! {pokemon2['Name']} vince!")
            break
    print("La battaglia è finita.")

if __name__ == "__main__":
    pokemon_data = carica_pokemon('Esercizio13/pokemon.json')
    #print(list(pokemon_data))
    pokemon = choice(list(pokemon_data))
    pokemon1 = pokemon_data[pokemon]
    pokemon = choice(list(pokemon_data))
    pokemon2 = pokemon_data[pokemon]
    print(f"Pokémon scelti: {pokemon1} e {pokemon2}")
    while pokemon1 == pokemon2:
        pokemon2 = choice(list(pokemon_data.keys()))
    if int(pokemon1['Speed']) > int(pokemon2['Speed']):
        battaglia(pokemon1, pokemon2)
    else:
        battaglia(pokemon2, pokemon1)




