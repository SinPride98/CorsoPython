#combattimenti tra pokemon nel fie json
import json
from random import choice

CD = 0.5 #coefficiente di difesa
CA= 0.5 #coefficiente di attacco
CRITICO = 2 #moltiplicatore critico

def carica_pokemon(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def calcola_danno(attaccante, difensore):
    attacco = attaccante['Attack']
    difesa = difensore['Defense']
    velocita = attaccante['Speed']
    velocita_difensore = difensore['Speed']

    danno_base = (attacco * CA) - (difesa * CD)
    danno_base = max(danno_base, 1)  # Il danno minimo è 1

    # Calcolo del critico
    if velocita > velocita_difensore and choice([True, False, False, False, False, False, False, False, False, False]):
        danno_base *= CRITICO
        print(f"Colpo critico di {attaccante['nome']}!")
    elif velocita <= velocita_difensore and choice([True, False, False, False, False, False, False, False, False, False]):
        danno_base = 0
        print(f"Colpo evitato da {difensore['nome']}!")
    
    return int(danno_base)





