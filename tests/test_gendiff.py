#!/usr/bin/env python3
from hexlet_code.gendiff import generate_diff


def test_generate_diff_plain():
  expected_result = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""
  dict1 = load_file("file1_plain.json")
  dict2 = load_file("file2_plain.json")
  actual_result = generate_diff("dict1, dict2")
  assert actual_result == expected_result

def test_generate_diff():
  expected_result = """{
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
}"""
  dict1 = load_file("file1.json")
  dict2 = load_file("file2.json")
  actual_result = generate_diff(dict1, dict2)
  assert actual_result == expected_result
'''def test_same_files():
	expected_result = """{
    follow: False
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""
	actual_result = generate_diff("file1.json", "file1.json")
	assert actual_result == expected_result

def test_one_empty():
	expected_result = """{
  - follow: False
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}"""
	actual_result = generate_diff("file1.json", "file0.json")
	assert actual_result == expected_result

def test_both_empty():
	expected_result = """{

}"""
	actual_result = generate_diff("file0_copy.json", "file0.json")
	assert actual_result == expected_result'''
