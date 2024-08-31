def to_json_format(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    return value

def generate_diff(dict1, dict2, depth=0):
    indent = '    ' * depth
    list_result = []
    all_keys = set(dict1.keys()) | set(dict2.keys())
    
    for key in sorted(all_keys):
        if key in dict1 and key in dict2:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                nested_diff = generate_diff(dict1[key], dict2[key], depth + 1)
                list_result.append(f'{indent}    {key}: {nested_diff}')
            elif dict1[key] == dict2[key]:
                value = to_json_format(dict1[key])
                list_result.append(f'{indent}    {key}: {value}')
            else:
                old_value = to_json_format(dict1[key])
                new_value = to_json_format(dict2[key])
                list_result.append(f'{indent}  - {key}: {old_value}')
                list_result.append(f'{indent}  + {key}: {new_value}')

        elif key in dict1:
            old_value = to_json_format(dict1[key])
            if isinstance(dict1[key], dict):
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


'''
{
    common: {
      + follow: False
        setting1: Value 1
      - setting2: 200
      - setting3: True
      + setting3: None
      + setting4: blah blah
      + setting5: {'key5': 'value5'}
        setting6: {
            doge: {
              - wow: 
              + wow: so much
}
            key: value
          + ops: vops
}
}
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {'key': 'value'}
      + nest: str
}
  - group2: {'abc': 12345, 'deep': {'id': 45}}
  + group3: {'deep': {'id': {'number': 45}}, 'fee': 100500}
}

{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}
'''