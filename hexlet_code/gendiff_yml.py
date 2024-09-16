def to_yaml_format(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    return value


def generate_diff_yml(dict1, dict2, depth=0):
    indent = '    ' * depth
    list_result = []
    all_keys = set(dict1.keys()) | set(dict2.keys())

    for key in sorted(all_keys):
        if key in dict1 and key in dict2:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                nested_diff = generate_diff_yml(dict1[key], dict2[key], depth + 1)
                list_result.append(f'{indent}    {key}: {nested_diff}')
            elif dict1[key] == dict2[key]:
                value = to_yaml_format(dict1[key])
                list_result.append(f'{indent}    {key}: {value}')
            else:
                old_value = to_yaml_format(dict1[key])
                new_value = to_yaml_format(dict2[key])
                list_result.append(f'{indent}  - {key}: {old_value}')
                list_result.append(f'{indent}  + {key}: {new_value}')

        elif key in dict1:
            old_value = to_yaml_format(dict1[key])
            if isinstance(dict1[key], dict):
                nested_diff = generate_diff_yml(dict1[key], {}, depth + 1)
                list_result.append(f'{indent}  - {key}: {nested_diff}')
            else:
                list_result.append(f'{indent}  - {key}: {old_value}')
        else:
            new_value = to_yaml_format(dict2[key])
            if isinstance(dict2[key], dict):
                nested_diff = generate_diff_yml({}, dict2[key], depth + 1)
                list_result.append(f'{indent}  + {key}: {nested_diff}')
            else:
                list_result.append(f'{indent}  + {key}: {new_value}')

    return '{\n' + '\n'.join(list_result) + '\n' + indent + '}'


'''def generate_diff_yml(dict1, dict2):
    result = ''
    list_result = []

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

    return '{\n' + '\n'.join(list_result) + '\n}'''
