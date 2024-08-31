def generate_diff(dict1, dict2, depth=0):
    indent = '    ' * depth
    result = ''
    list_result = []
    all_keys = set(dict1.keys()) | set(dict2.keys())
    for key in sorted(all_keys):
        if key in dict1 and key in dict2:
            if type(dict1[key]) == dict and type(dict2[key]) == dict:
                nested_diff = generate_diff(dict1[key], dict2[key], depth + 1)
                result = f'{indent}    {key}: {nested_diff}'
                list_result.append(result)
            elif dict1[key] == dict2[key]:
                result = f'{indent}    {key}: {dict1[key]}'
                list_result.append(result)
            else:
                result_old = f'{indent}  - {key}: {dict1[key]}'
                result_new = f'{indent}  + {key}: {dict2[key]}'
                list_result.append(result_old)
                list_result.append(result_new)

        elif key in dict1:
            result = f'{indent}  - {key}: {dict1[key]}'
            list_result.append(result)

        else:
            result = f'{indent}  + {key}: {dict2[key]}'
            list_result.append(result)

    return '{\n' + '\n'.join(list_result) + '\n' + indent +'}'

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