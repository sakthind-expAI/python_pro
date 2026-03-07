"""
Unit tests for python_code.py

This module contains unit tests for the functions in python_code.py.
Run with: python -m unittest test_python_code.py
Sakthi Narayanan D
"""

import unittest
import re  # Add import for regex tests
import python_code as pc  # Import the module to test

class TestPythonCode(unittest.TestCase):

    def test_get_xml_counts(self):
        """Test XML parsing and counting."""
        url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
        count, total = pc.get_xml_counts(url)
        self.assertEqual(count, 50)  # Known count for this URL
        self.assertEqual(total, 2553)  # Known sum

    def test_regex_findall_numbers(self):
        """Test regex for finding numbers."""
        x = 'My 2 favorite nos are 19 and 42'
        result = re.findall(r'[0-9]+', x)
        self.assertEqual(result, ['2', '19', '42'])

    def test_regex_vowels(self):
        """Test regex for uppercase vowels."""
        x = 'My 2 favorite nos are 19 and 42'
        result = re.findall(r'[AEIOU]+', x)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()