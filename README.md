# Hash Table Implementation in Python

## Project Description

This project uses a custom hash table to count word frequencies in a book.

## Table of Contents 📖

- [📋 Prerequisites](#prerequisites)
- [🔧 Setup](#setup)
- [🚀 Usage](#usage)
  - [💻 Windows](#windows)
  - [🍏/🐧 MacOS/Linux](#macoslinux)
- [⚙️ Functionality](#functionality)
- [🧪 Tests](#tests)
- [📚 References](#references)
- [🖋️ Citation](#citation)

## Prerequisites

- Python 3.x
- Good knowledge of hash tables and their operations.

## Setup

1. Clone the repository:

   ```
   git clone git@github.com:Tim-Quattrochi/py-word-counter.git
   ```

2. Navigate to the project directory:
   ```
   cd py-word-counter
   ```

## Usage

I recommend using a virtual environment to run this program. To create a virtual environment, run the following command:

### Windows

```cmd
python -m venv venv
```

To activate the virtual environment, run the following command:

```cmd
venv\Scripts\activate
```

Run the `app.py` script to start the program:

```cmd
python app.py
```

### MacOS/Linux

```bash
python3 -m venv venv
```

To activate the virtual environment, run the following command:

```bash
source venv/bin/activate
```

Run the `app.py` script to start the program:

```bash
python3 app.py
```

## Functionality

The program implements a hash table with chaining and uses it to count word frequencies in a book. The hash table supports the following operations:

- `insert(key, value)`: Inserts a key-value pair into the hash table.
- `lookup(key)`: Returns the value associated with the given key.
- `delete(key)`: Removes the key-value pair associated with the given key from the hash table.
- `__len__()`: Returns the number of key-value pairs in the hash table.
- `resize(int)`: Resizes the hash table to the given size.
- `items()`: Returns a list or generator of all key-value pairs in the hash table.

## Tests

I am using the `unittest` module to test the hash table implementation. To run the tests, use the following command:

```bash
python3 -m unittest test_hash_table.py
```

## References

- [Hash Table Slides](https://docs.google.com/presentation/d/14N_E4uZL6XqT4bejTkRYDq7sps-hBxN8VQTGXJCpGxg/edit#slide=id.p)

- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)

- [reading txt files in python](https://www.geeksforgeeks.org/reading-writing-text-files-python/)

### Citation

---

Book used as dataset:

> Gray, J. (1920). The other Miller girl. New York: Chas. Scribners Sons. [Link](https://www.gutenberg.org/cache/epub/73780/pg73780.txt)

---

[⬆️ Back to Top](#hash-table-implementation-in-python)
