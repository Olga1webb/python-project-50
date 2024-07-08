#!/usr/bin/env python3
from hexlet_code.scripts.gendiff_yml import generate_diff_yml

def test_generate_diff_yml():
	expected_result = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""
	actual_result = generate_diff("file01.yml", "file02.yml")
	assert actual_result == expected_result

def test_same_files():
	expected_result = """{
    follow: False
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""
	actual_result = generate_diff("file01.yml", "file01.yml")
	assert actual_result == expected_result

def test_one_empty():
	expected_result = """{
  - follow: False
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}"""
	actual_result = generate_diff("file01.yml", "file00_copy.yml")
	assert actual_result == expected_result

def test_both_empty():
	expected_result = """{

}"""
	actual_result = generate_diff("file00.yml", "file00_copy.yml")
	assert actual_result == expected_result