import json

def load_file(file_path):
	with open(file_path, 'r') as file:
		dict = json.load(file)
		return dict

def load_file_yml(file_path):
    with open(file_path, 'r') as file:
        dict = yaml.safe_load(file) or {}
		return dict