import json
import yaml


def load_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data

def load_file_yml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file) or {}
        return data
