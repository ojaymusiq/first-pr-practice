import unittest

from greet import greet


class GreetTest(unittest.TestCase):
    def test_greets_by_name(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_strips_surrounding_whitespace(self):
        self.assertEqual(greet("  Ada  "), "Hello, Ada!")

    def test_empty_name_greets_stranger(self):
        self.assertEqual(greet(""), "Hello, stranger!")
        self.assertEqual(greet("   "), "Hello, stranger!")


if __name__ == "__main__":
    unittest.main()
