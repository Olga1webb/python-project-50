'''def build_tree(dict_value):
    dict_tree_unchanged = {}
    for i in dict_value:
        if isinstance(dict_value[i], dict):
            dict_tree_unchanged[i] = {
                'value': nested_value_unchanged
                ''
            }'''



def build_diff_tree(dict1, dict2, depth=0):
    dict_tree = {}
    all_keys = dict1.keys() | dict2.keys() #объединяем ключи обоих словарей
    for key in sorted(all_keys):
        if key in dict1 and key in dict2: #если ключ в обоих словарях
            if dict1[key] == dict2[key]: #и если значения по ключам равны
                dict_tree[key] = {
                    'value': dict1[key],
                    'category': 'unchanged', 
                    'nest': depth
                }

            elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict): #и значения по обоим – словари
                nested_value = build_diff_tree(dict1[key], dict2[key], depth+1) #сравнить подсловари
                dict_tree[key] = {
                    'value': nested_value, 
                    'category': 'nested', #присвоить ключу тип нестед
                    'nest': depth
                } 

            else: #если это не словари и не равны, обозначаем разницу
                dict_tree[key] = {
                    'old_value': dict1[key], 
                    'new_value': dict2[key], 
                    'category': 'changed', 
                    'nest': depth
                }

        elif key in dict1:
            ''' if isinstance(dict1[key], dict):
                depth +=1
                for i in dict1[key]:
                    dict_tree[key] = {
                        'value': dict1[key][i], 
                        'category': 'unchanged', #присвоить ключу тип нестед
                        'nest': depth
                    } 
            else:'''
            dict_tree[key] = {
                'value': dict1[key],
                'category': 'removed',
                'nest': depth
            }
        else:
            dict_tree[key] = {
                'value': dict2[key],
                'category': 'added',
                'nest': depth
            }
    return dict_tree


