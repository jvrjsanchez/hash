import unittest
from unittest.mock import patch
from hash_class import MyHashTable


class TestMyHashTable(unittest.TestCase):
    def test_insert_and_get_value(self):

        hash_table = MyHashTable()

        # insert
        hash_table.insert("hello world", 5)
        hash_table.insert("python", 10)
        hash_table.insert("tensorflow", 15)

        # assertions
        self.assertEqual(hash_table.get_value("hello world"), 5)
        self.assertEqual(hash_table.get_value("python"), 10)
        self.assertEqual(hash_table.get_value("tensorflow"), 15)

    def test_size(self):
        # test default size
        self.assertEqual(MyHashTable().size, 10)

        hash_table = MyHashTable(30000)
        self.assertEqual(hash_table.size, 30000)

    def test_collision(self):
        with patch.object(MyHashTable, '_hash', return_value=0):

            hash_table = MyHashTable(10)

        # insert
            hash_table.insert("hello world", 5)
            hash_table.insert("python", 10)

        # assertions
            self.assertEqual(hash_table.get_value("hello world"), 5)
            self.assertEqual(hash_table.get_value("python"), 10)


if __name__ == '__main__':
    unittest.main()
