
def djb2(key):
    """
    Args:
        key (str): The key to hash.
    Returns:
        int: The hash value.
    """
    hash_value = 5381
    for char in key:
        # "<<" bitwise left shift operator. It shifts the bits of its left-hand operand to the left by the number of positions specified by its right-hand operand.
        # "ord()" returns the Unicode code point for a given character.
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
    # '&' is used for bitwise operations, 'and' is for logical.
    return hash_value & 0xFFFFFFFF


class MyHashTable:
    def __init__(self, size=10):
        self.size = size
        self.count = 0
        self.table = [[] for _ in range(size)]

    def insert(self, key, value):
        if self.count / self.size > 0.75:
            self.resize()

        hash_value = self._hash(key)
        idx = hash_value % len(self.table)

        for pair in self.table[idx]:
            if pair[0] == key:
                pair[1] = value
                return
            # not found, add it.
        self.table[idx].append([key, value])
        self.count += 1

   # '_' means the method is meant to for internal use.
    def _resize(self):
        new_table = [[] for _ in range(self.size * 2)]
        for i in range(self.size):
            for key, value in self.table[i]:
                hash_value = self._hash(key)
                idx = hash_value % len(new_table)
                new_table[idx].append([key, value])
        self.size *= 2
        self.table = new_table

    def get_value(self, key):
        hash_value = self._hash(key)
        idx = hash_value % len(self.table)

        for pair in self.table[idx]:
            if pair[0] == key:
                return pair[1]

        raise KeyError(key)

    def delete(self, key):
        hash_value = self._hash(key)
        idx = hash_value % len(self.table)

        for i, pair in enumerate(self.table[idx]):
            if pair[0] == key:
                del self.table[idx][i]
                return

        raise KeyError(key)

    def _hash(self, key):
        return djb2(key)

    # method for inspecting table.
    def __str__(self):
        return str(self.table)

    # method for returning key-value pairs.
    def items(self):
        for bucket in self.table:
            for pair in bucket:
                yield pair
