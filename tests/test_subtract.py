import unittest

from calc import subtract


class SubtractTest(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_negative_result(self):
        self.assertEqual(subtract(3, 5), -2)

    def test_subtract_negative_input(self):
        self.assertEqual(subtract(-4, 2), -6)
        self.assertEqual(subtract(4, -2), 6)


if __name__ == "__main__":
    unittest.main()
