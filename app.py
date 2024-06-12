from hash_class import MyHashTable
import os
import re
# Reference slides: https://docs.google.com/presentation/d/14N_E4uZL6XqT4bejTkRYDq7sps-hBxN8VQTGXJCpGxg/edit#slide=id.p

# 1. Implement a hash function.
# - def hashcode(arg: string) -> int

# 2. Implement a hash table with chaining
# - insert(key, value)
# - lookup(key) -> value
# - delete(key)
# __len__ () => int
# - resize(int)
# - items() -> list or generator of [key, value] pairs

# 3. Use hash table to count word frequencies in a book.

# djb2 hash function implementation.

book_path = os.path.join(os.path.dirname(__file__), './books/miller-girl.txt')


def process_data(file):
    if not os.path.isfile(file):
        raise FileNotFoundError("File not found")

    if not os.path.isabs(file):
        raise ValueError(f"{file} is not an absolute path.")

    with open(file, 'r') as f:
        data = f.read()
        # remove punctuations with regex
        data = re.sub(r'[^\w\s]', '', data)
        data = data.lower()
        return data


def frequency_counter(table_items_fn):
    items = list(table_items_fn())
    items.sort(key=lambda pair: pair[1], reverse=True)
    print("Top 10 words: \t\n")
    print("{:<15} {:<10}".format('Word', 'Frequency'))
    print('-' * 25)
    for word, frequency in items[:10]:
        print("{:<15} {:<10}".format(word, frequency))


def main():
    hash_table = MyHashTable(30000)
    words = process_data(book_path).split()
    for word in words:
        try:
            hash_table.insert(word, hash_table.get_value(word) + 1)
        except KeyError:  # if the word is not found, add it.
            hash_table.insert(word, 1)

    frequency_counter(hash_table.items)


if __name__ == "__main__":
    main()
