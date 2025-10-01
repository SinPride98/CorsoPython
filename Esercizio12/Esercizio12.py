#convertire un file csv in un file json
import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    # create a dictionary
    data = {}
    
    # open csv file for reading
    with open(csv_file_path, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csv_reader = csv.DictReader(csvf)
        
        # convert each row into a dictionary and add it to data
        for rows in csv_reader:
            key = rows['Name']  # assuming 'id' is the unique identifier for each row
            data[key] = rows
    
    # open json file for writing
    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        # convert dictionary to json and write to file
        jsonf.write(json.dumps(data, indent=4))

def json_to_csv(json_file_path, csv_file_path):
    # create a dictionary
    prova={}   
    with open(json_file_path, encoding='utf-8') as jsonf:
        # load json file data using json library's load method
        data = json.load(jsonf)

    first_key = next(iter(data))
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvf:
        # create the csv writer object
        csv_writer = csv.DictWriter(csvf, fieldnames=list(data[first_key].keys()))
        csv_writer.writeheader()
        csv_writer.writerows(data.values())

scelta=int(input("Premi 1 per convertire da csv a json, 2 per convertire da json a csv: "))
if scelta==1:
    csv_to_json(r"C:\Users\Michael-PC\Desktop\Progetti\CorsoPython\Esercizio12\pokemon.csv", r"C:\Users\Michael-PC\Desktop\Progetti\CorsoPython\Esercizio12\pokemon.json")
elif scelta==2:
    json_to_csv(r"C:\Users\Michael-PC\Desktop\Progetti\CorsoPython\Esercizio12\pokemon.json", r"C:\Users\Michael-PC\Desktop\Progetti\CorsoPython\Esercizio12\pokemon_from_json.csv")