def generate_diff(file_path1, file_path2):
    result = ''
    list_result = []
    all_keys = set(dict1.keys()) | set(dict2.keys())
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
