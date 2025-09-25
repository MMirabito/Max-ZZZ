# Max-ZZZ

A simple Python utility for finding maximum values in various data types.

## Features

- Find maximum number from multiple arguments
- Find maximum number in a list
- Find string with maximum length
- Command-line interface for easy usage

## Usage

### As a Python module

```python
from max_finder import find_max_number, find_max_in_list, find_max_string_length

# Find max from numbers
result = find_max_number(1, 5, 3, 9, 2)
print(result)  # Output: 9

# Find max in list
numbers = [10, 20, 5, 30]
result = find_max_in_list(numbers)
print(result)  # Output: 30

# Find longest string
words = ["hello", "world", "maximum"]
result = find_max_string_length(words)
print(result)  # Output: "maximum"
```

### Command line

```bash
python max_finder.py
```

This will run a demonstration showing the different maximum-finding capabilities.

## Requirements

- Python 3.6 or higher

## Installation

Simply clone this repository:

```bash
git clone https://github.com/MMirabito/Max-ZZZ.git
cd Max-ZZZ
```

## License

This project is open source and available under the MIT License.