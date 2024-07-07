import csv
import json
from collections import defaultdict

def csv_to_json(csv_file_path, json_file_path):
    # Create a dictionary to hold the decks
    decks = defaultdict(list)
    
    # Open the CSV file for reading
    with open(csv_file_path, mode='r', newline='') as csv_file:
        # Read the CSV data
        csv_reader = csv.DictReader(csv_file)
        
        # Process each row in the CSV
        for row in csv_reader:
            # Extract card information
            card_name = row['card_name']
            card_set = row['card_set']
            card_number = int(row['card_number'])
            
            # Add card to the appropriate deck
            decks[card_set].append({
                "card_name": card_name,
                "card_set": card_set,
                "card_number": card_number,
            })
    
    # Open the JSON file for writing
    with open(json_file_path, mode='w') as json_file:
        # Write decks to JSON file
        json.dump(decks, json_file, indent=4)

# Define the file paths
csv_file_path = 'MonopolyGoCards.csv'
json_file_path = 'MonopolyGoCards.json'

# Convert CSV to JSON
csv_to_json(csv_file_path, json_file_path)

print(f"CSV data from '{csv_file_path}' has been converted to JSON and saved to '{json_file_path}'")
