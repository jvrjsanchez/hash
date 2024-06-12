# My Approach and Design Choices

In this project, I've implemented a hash table in Python. If you're not familiar, hash tables are useful data structures that map keys to values. They're good for quick access, insertion, and deletion of key-value pairs. I used this hash table to count word frequencies in a book (as a txt file).

Here's a bit about the choices I made during the implementation:

- **Hash Function**: I decided to use the `djb2` hash function. It's a popular choice because it gives a good distribution of hash values for a wide variety of inputs.

- **Collision Resolution**: Collisions happen when two keys hash to the same index. To handle this, I used a method called chaining. It keeps a list of all key-value pairs that hash to the same index.

- **Key Deletion**: I used the `del` keyword to remove a key-value pair from the table. If the key isn't found, it raises a `KeyError`.

- **Table Inspection**: I implemented the `__str__` method to return a string representation of the hash table. I found that it is good for debugging and inspection.

- **Iteration**: I created an `items` method that's a generator. It yields all key-value pairs in the hash table, which I use for iterating over all items in the table.

# Analyzing Time and Space Complexity

- **Access**: Generally, accessing a key-value pair in a hash table is a constant time operation, O(1). But in the worst-case scenario (like when all keys hash to the same index), it can degrade to O(n), where n is the number of keys.

- **Insertion and Deletion**: These are usually constant time operations, O(1). But again, in the worst-case scenario, they can degrade to O(n).

- **Space**: The space complexity of a hash table is O(n), where n is the number of key-value pairs. This is because each key-value pair needs its own place in the table.
