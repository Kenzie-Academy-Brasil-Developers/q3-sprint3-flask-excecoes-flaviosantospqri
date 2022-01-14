
from inspect import Attribute
import json
import os
from ujson import dump, load


FOLDER_DIRECTORY = os.getenv('FOLDER_DIRECTORY')
data = []

if not os.path.isdir(FOLDER_DIRECTORY):
    os.mkdir(FOLDER_DIRECTORY)

def load_json_file(filepath: str):
    try:
        with open(filepath, 'r') as json_file:
            return load(json_file)
    except FileNotFoundError:
        with open(filepath, 'w') as json_file:
            return dump(data, json_file, indent=4)



def write_json_file(filepath: str, payload: dict):
    data.append(payload)
    with open(filepath, 'w') as json_file:
            dump(data, json_file, indent=2)

    return payload
