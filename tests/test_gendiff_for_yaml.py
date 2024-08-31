#!/usr/bin/env python3
import yaml
from hexlet_code.gendiff_yml import generate_diff_yml

def test_generate_diff_yml_plain():
  expected_result = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
  with open("file01_plain.yml", 'r') as file:
    dict1 = yaml.safe_load(file) or {}
  with open("file02_plain.yml", 'r') as file:
    dict2 = yaml.safe_load(file) or {}
  actual_result = generate_diff_yml(dict1, dict2)
  assert actual_result == expected_result

def test_generate_diff_yml():
  expected_result = """{
    common: {
      + follow: false
      + group1: {
          + baz: bars
          + foo: bar
          + nest: str
        }
      + group3: {
          + deep: {
              + id: {
                  + number: 45
                }
            }
          + fee: 100500
        }
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
          + key5: value5
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
  - group1: {
      - baz: bas
      - foo: bar
      - nest: {
          - key: value
        }
    }
  - group2: {
      - abc: 12345
      - deep: {
          - id: 45
        }
    }
}"""
  with open("file01.yml", 'r') as file:
    dict1 = yaml.safe_load(file) or {}
  with open("file02.yml", 'r') as file:
    dict2 = yaml.safe_load(file) or {}
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