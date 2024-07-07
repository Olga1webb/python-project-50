#!/usr/bin/env python3
from hexlet_code.scripts.gendiff import generate_diff

expected_result = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""
def test_generate_diff():
	actual_result = generate_diff("file1.json", "file2.json")
	assert actual_result == expected_result