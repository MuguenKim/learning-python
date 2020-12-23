import unittest
from binary_search import binary_search_recursive, binary_search


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.sequence = [2, 6, 7, 8, 9, 12, 20, 42]

    def test_regular(self):
        self.assertEqual(binary_search(8, self.sequence), 3)
        self.assertEqual(binary_search(20, self.sequence), 6)
        self.assertEqual(binary_search(2, self.sequence), 0)
        self.assertEqual(binary_search(42, self.sequence), 7)
        self.assertEqual(binary_search(100, self.sequence), None)

    def test_recursive(self):
        self.assertEqual(binary_search_recursive(
            8, 0, len(self.sequence)-1, self.sequence), 3)
        self.assertEqual(binary_search_recursive(
            20, 0, len(self.sequence)-1, self.sequence), 6)
        self.assertEqual(binary_search_recursive(
            2, 0, len(self.sequence)-1, self.sequence), 0)
        self.assertEqual(binary_search_recursive(
            42, 0, len(self.sequence)-1, self.sequence), 7)
        self.assertEqual(binary_search_recursive(
            100, 0, len(self.sequence)-1, self.sequence), None)
