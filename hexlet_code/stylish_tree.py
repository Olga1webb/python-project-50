def stylish(dict_tree):
	indent_zero = '    '
	indent = '    '
	indent_plus = '  + '
	indent_minus = '  - '
	list_result = []

	for key in dict_tree:
		node = dict_tree[key]
		if node['category'] == 'unchanged':
			a = indent_zero + indent * node['nest']
			list_result.append(f'{a}{key}: {node["value"]}')
		elif node['category'] == 'removed':
			a = indent*node['nest'] + indent_minus
			list_result.append(f'{a}{key}: {node["value"]}')
		elif node['category'] == 'added':
			a = indent*node['nest'] + indent_plus
			list_result.append(f'{a}{key}: {node["value"]}')
		elif node['category'] == 'changed':
			a = indent*node['nest'] + indent_minus
			list_result.append(f'{a}{key}: {node["old_value"]}')
			b = indent*node['nest'] + indent_plus
			list_result.append(f'{b}{key}: {node["new_value"]}')
		elif node['category'] == 'nested':
			a = indent_zero + indent * node['nest']
			stylish_value = stylish(node['value'])
			list_result.append(f'{a}{key}: {stylish_value}')

	return '{\n' + '\n'.join(list_result) + '\n' + indent + '}'
			

