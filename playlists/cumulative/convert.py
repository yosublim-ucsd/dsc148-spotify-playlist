import json
import csv
import os

def json_to_csv(json_file):
    csv_file = json_file.replace(".json", ".csv")
    
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Ensure the JSON is a list of dictionaries
    if isinstance(data, list):
        keys = data[0].keys() if data else []
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        print(f"Converted {json_file} to {csv_file}")
    else:
        print(f"Skipping {json_file}: Not a list of objects")

# Convert all JSON files in the current directory
for file in os.listdir():
    if file.endswith(".json"):
        json_to_csv(file)
