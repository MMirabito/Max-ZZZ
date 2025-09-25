#!/usr/bin/env python3
"""
Tests for max_finder module.
"""

import unittest
from max_finder import find_max_number, find_max_in_list, find_max_string_length


class TestMaxFinder(unittest.TestCase):
    
    def test_find_max_number(self):
        """Test finding maximum from multiple arguments."""
        self.assertEqual(find_max_number(1, 5, 3), 5)
        self.assertEqual(find_max_number(10), 10)
        self.assertEqual(find_max_number(-1, -5, -3), -1)
        
    def test_find_max_number_empty(self):
        """Test that empty arguments raise ValueError."""
        with self.assertRaises(ValueError):
            find_max_number()
    
    def test_find_max_in_list(self):
        """Test finding maximum in a list."""
        self.assertEqual(find_max_in_list([1, 5, 3, 9, 2]), 9)
        self.assertEqual(find_max_in_list([10]), 10)
        self.assertEqual(find_max_in_list([-1, -5, -3]), -1)
    
    def test_find_max_in_list_empty(self):
        """Test that empty list raises ValueError."""
        with self.assertRaises(ValueError):
            find_max_in_list([])
    
    def test_find_max_string_length(self):
        """Test finding string with maximum length."""
        self.assertEqual(find_max_string_length(["a", "hello", "hi"]), "hello")
        self.assertEqual(find_max_string_length(["test"]), "test")
        self.assertEqual(find_max_string_length(["abc", "def", "ghi"]), "abc")  # First occurrence
    
    def test_find_max_string_length_empty(self):
        """Test that empty list raises ValueError."""
        with self.assertRaises(ValueError):
            find_max_string_length([])


if __name__ == "__main__":
    unittest.main()