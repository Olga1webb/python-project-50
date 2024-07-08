#!/usr/bin/env python3
from hexlet_code.scripts.gendiff import generate_diff


def test_generate_diff():
	expected_result = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""
	actual_result = generate_diff("file1.json", "file2.json")
	assert actual_result == expected_result

def test_same_files():
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
	assert actual_result == expected_result
