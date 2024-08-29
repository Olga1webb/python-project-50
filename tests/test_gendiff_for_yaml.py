#!/usr/bin/env python3
from hexlet_code.gendiff_yml import generate_diff_yml
from hexlet_code.read_file import load_file

def test_generate_diff_yml_plain():
  expected_result = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""
  dict1 = load_file("file01_plain.yml")
  dict2 = load_file("file02_plain.yml")
  actual_result = generate_diff_yml(dict1, dict2)
  assert actual_result == expected_result

def test_generate_diff_yml():
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
  dict1 = load_file("file01.yml")
  dict2 = load_file("file02.yml")
  actual_result = generate_diff_yml(dict1, dict2)
  assert actual_result == expected_result
'''
def test_same_files_yml():
	expected_result = """{
    follow: False
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""
	actual_result = generate_diff_yml("file01_plain.yml", "file01_plain.yml")
	assert actual_result == expected_result

def test_one_empty_yml():
	expected_result = """{
  - follow: False
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}"""
	actual_result = generate_diff_yml("file01_plain.yml", "file00_copy.yml")
	assert actual_result == expected_result

def test_both_empty_yml():
	expected_result = """{

}"""
	actual_result = generate_diff_yml("file00.yml", "file00_copy.yml")
	assert actual_result == expected_result
'''