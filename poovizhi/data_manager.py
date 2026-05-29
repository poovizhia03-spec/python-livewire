import json
import os

def load_data(filename, default_data):
    """
    Loads data from a given JSON file.
    If the file doesn't exist, it creates one with the provided default_data.
    """
    if not os.path.exists(filename):
        save_data(filename, default_data)
        return default_data
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        
        print(f"Warning: Could not read {filename}. Using default empty data.")
        return default_data

def save_data(filename, data):
    """
    Saves data to a given JSON file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"Error saving data to {filename}: {e}")
