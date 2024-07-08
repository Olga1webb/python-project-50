#!/usr/bin/env python3
import yaml
import argparse

def parser_diff():
	parser = argparse.ArgumentParser(
			description="Compares two configuration files and shows a difference.")
	parser.add_argument("first_file")
	parser.add_argument("second_file")
	parser.add_argument('-f', '--format', help='set format of output') 
	return parser.parse_args()

def generate_diff_yml(file_path1, file_path2):
    result = ''
    list_result = []

    try:
        with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
            dict1 = yaml.safe_load(file1) or {}  # Заменяет None на пустой словарь
            dict2 = yaml.safe_load(file2) or {}  # Заменяет None на пустой словарь
    except FileNotFoundError as e:
        return f"Error: File not found - {e}"
    except yaml.YAMLError as e:
        return f"Error: Invalid YAML - {e}"

    
    all_keys = set(dict1.keys()) | set(dict2.keys())
    if all_keys:
        for key in sorted(all_keys):
            if key in dict1 and key in dict2:
                if dict1[key] == dict2[key]:
                    result = f'    {key}: {dict1[key]}'
                    list_result.append(result)

                else:
                    result_old = f'  - {key}: {dict1[key]}'
                    result_new = f'  + {key}: {dict2[key]}'
                    list_result.append(result_old)
                    list_result.append(result_new)

            elif key in dict1:
                result = f'  - {key}: {dict1[key]}'
                list_result.append(result)

            else:
                result = f'  + {key}: {dict2[key]}'
                list_result.append(result)

    return '{\n' + '\n'.join(list_result) + '\n}'

def main():
	args = parser_diff()
	diff = generate_diff_yml(args.first_file, args.second_file)
	print(diff)
	

if __name__ == '__main__':
    main()
