def to_json_format(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    return value


def generate_diff(dict1, dict2, depth=0):
    indent = '    ' * depth
    list_result = []
    all_keys = dict1.keys() | dict2.keys() #объединяем ключи обоих словарей

    for key in sorted(all_keys): #для каждого из ключей
        if key in dict1 and key in dict2: #если ключ в обоих словарях
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict): #и значения обоих ключей – словари
                nested_diff = generate_diff(dict1[key], dict2[key], depth + 1) #ищем разницу словарей, добавляем 1 уровень для оформления
                list_result.append(f'{indent}    {key}: {nested_diff}') #добавляем строку в итоговый список, исп-я получившийся отступ
            elif dict1[key] == dict2[key]: #если же значения по ключам равны
                value = to_json_format(dict1[key]) #редактируем вывод
                list_result.append(f'{indent}    {key}: {value}') #добавляем строку в итоговый список, исп-я получившийся отступ
            else: #если это не словари и не равны, обозначаем разницу
                old_value = to_json_format(dict1[key])
                new_value = to_json_format(dict2[key])
                list_result.append(f'{indent}  - {key}: {old_value}')
                list_result.append(f'{indent}  + {key}: {new_value}')

        elif key in dict1: #если ключ только в первом словаре
            old_value = to_json_format(dict1[key])
            if isinstance(dict1[key], dict): #если значение по ключу – словарь
                nested_diff = generate_diff(dict1[key], {}, depth + 1)
                list_result.append(f'{indent}  - {key}: {nested_diff}')
            else:
                list_result.append(f'{indent}  - {key}: {old_value}')
        else:
            new_value = to_json_format(dict2[key])
            if isinstance(dict2[key], dict):
                nested_diff = generate_diff({}, dict2[key], depth + 1)
                list_result.append(f'{indent}  + {key}: {nested_diff}')
            else:
                list_result.append(f'{indent}  + {key}: {new_value}')

    return '{\n' + '\n'.join(list_result) + '\n' + indent + '}'
