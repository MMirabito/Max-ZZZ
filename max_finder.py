#!/usr/bin/env python3
"""
Max-ZZZ: A simple utility for finding maximum values.
"""

def find_max_number(*args):
    """Find the maximum number from given arguments."""
    if not args:
        raise ValueError("At least one number must be provided")
    return max(args)

def find_max_in_list(numbers):
    """Find the maximum number in a list."""
    if not numbers:
        raise ValueError("List cannot be empty")
    return max(numbers)

def find_max_string_length(strings):
    """Find the string with maximum length."""
    if not strings:
        raise ValueError("List cannot be empty")
    return max(strings, key=len)

def main():
    """Main function to demonstrate the max finder functionality."""
    print("Max-ZZZ: Maximum Value Finder")
    print("=" * 30)
    
    # Example with numbers
    numbers = [3, 7, 2, 9, 1, 5]
    print(f"Numbers: {numbers}")
    print(f"Maximum: {find_max_in_list(numbers)}")
    print()
    
    # Example with strings by length
    words = ["hello", "world", "maximum", "zzz"]
    print(f"Words: {words}")
    print(f"Longest word: '{find_max_string_length(words)}'")
    print()
    
    # Example with arguments
    result = find_max_number(10, 25, 15, 30, 5)
    print(f"Max of (10, 25, 15, 30, 5): {result}")

if __name__ == "__main__":
    main()