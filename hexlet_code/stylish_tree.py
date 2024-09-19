def format_value(v): #если значение по ключу явл словарем, то запускаем рекурсивно оформление
	if isinstance(v, dict):
		return stylish(v)
	else:
		return v
'''

def stylish(dict_tree):
	indent_zero = '    '
	indent = '    '
	indent_plus = '  + '
	indent_minus = '  - '
	list_result = []

	for key in dict_tree: #для каждого элемента словаря
		node = dict_tree[key] #обозначаем значение по ключу как нод
		if node['category'] == 'unchanged': #если значение в категории анченжд
			a = indent_zero + indent * node['nest'] #значение строки стандартный отступ плюс остступ соотв глубине
			#updated_value = format_value(node["value"]) #проверка, не является ли словарем
			#list_result.append(f'{a}{key}: {updated_value}')
			list_result.append(f'{a}{key}: {node["value"]}')
		elif node['category'] == 'removed':
			a = indent*node['nest'] + indent_minus
			updated_value = format_value(node["value"])
			list_result.append(f'{a}{key}: {updated_value}')
			
		elif node['category'] == 'added':
			a = indent*node['nest'] + indent_plus
			updated_value = format_value(node["value"])
			list_result.append(f'{a}{key}: {node["value"]}')
		elif node['category'] == 'changed':
			a = indent*node['nest'] + indent_minus
			updated_value_old = format_value(node["old_value"])
			list_result.append(f'{a}{key}: {updated_value_old}')
			b = indent*node['nest'] + indent_plus
			updated_value_new = format_value(node["new_value"])
			list_result.append(f'{b}{key}: {updated_value_new}')
		elif node['category'] == 'nested': #если есть вложенные словари
			a = indent_zero + indent * node['nest'] #отступ
			stylish_value = stylish(node['value']) #оформляем вложенные словари
			list_result.append(f'{a}{key}: {stylish_value}') #добавляем строку с отступом

	return '{\n' + '\n'.join(list_result) + '\n' + indent + '}'
	'''
def stylish(dict_tree):
    indent_zero = '    '
    indent = '    '
    indent_plus = '  + '
    indent_minus = '  - '
    list_result = []

    for key in dict_tree:
        node = dict_tree[key]
        if not isinstance(node, dict):
            raise TypeError(f'Expected dict at key "{key}", got {type(node).__name__} instead.')

        if node['category'] == 'unchanged':
            a = indent_zero + indent * node['nest']
            list_result.append(f'{a}{key}: {node["value"]}')
        elif node['category'] == 'removed':
            a = indent * node['nest'] + indent_minus
            updated_value = format_value(node["value"])
            list_result.append(f'{a}{key}: {updated_value}')
        elif node['category'] == 'added':
            a = indent * node['nest'] + indent_plus
            updated_value = format_value(node["value"])
            list_result.append(f'{a}{key}: {updated_value}')
        elif node['category'] == 'changed':
            a = indent * node['nest'] + indent_minus
            updated_value_old = format_value(node["old_value"])
            list_result.append(f'{a}{key}: {updated_value_old}')
            b = indent * node['nest'] + indent_plus
            updated_value_new = format_value(node["new_value"])
            list_result.append(f'{b}{key}: {updated_value_new}')
        elif node['category'] == 'nested':
            a = indent_zero + indent * node['nest']
            if isinstance(node['value'], dict):
                stylish_value = stylish(node['value'])
                list_result.append(f'{a}{key}: {stylish_value}')
            else:
                list_result.append(f'{a}{key}: {node["value"]}')

    return '{\n' + '\n'.join(list_result) + '\n' + indent + '}'


			

