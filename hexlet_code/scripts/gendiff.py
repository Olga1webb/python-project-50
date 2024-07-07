#!/usr/bin/env python3
import json
import argparse

def first_char(word):
	return word[4] if len(word) > 4 else ''


def generate_diff(file_path1, file_path2):
    result = ''
    list_result = list()
    output_result = '{\n'
    try:
        with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
            dict1 = json.load(file1)
            dict2 = json.load(file2)
    except FileNotFoundError as e:
        return f"Error: File not found - {e}"
    except json.JSONDecodeError as e:
        return f"Error: Invalid JSON - {e}"

    for a in dict1.keys():
        if a not in dict2.keys():
            result = f'  - {a}: {dict1[a]}'
            list_result.append(result)

        elif dict1[a] == dict2[a]:
            result = f'    {a}: {dict1[a]}'
            list_result.append(result)
            dict2.pop(a)

        elif dict1[a] != dict2[a]:
            result1 = f'  - {a}: {dict1[a]}'
            result2 = f'  + {a}: {dict2[a]}'
            list_result.append(result1)
            list_result.append(result2)
            dict2.pop(a)
    for b in dict2.keys():
        result = f'  + {b}: {dict2[b]}'
        list_result.append(result)

    sorted_result = sorted(list_result, key=first_char)
    for item in sorted_result:
    	output_result += item + '\n'
    return output_result + '}'


def parser_diff():
	parser = argparse.ArgumentParser(
			description="Compares two configuration files and shows a difference.")
	parser.add_argument("first_file")
	parser.add_argument("second_file")
	parser.add_argument('-f', '--format', help='set format of output') 
	return parser.parse_args()
	

def main():
	args = parser_diff()
	diff = generate_diff(args.first_file, args.second_file)
	print(diff)
	

if __name__ == '__main__':
    main()

