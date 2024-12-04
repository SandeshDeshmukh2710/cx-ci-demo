import unittest
from app import add, sub, multiply, divide  # Replace `calculator` with the actual filename of your script

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4, 5), 9)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_sub(self):
        self.assertEqual(sub(10, 5), 5)
        self.assertEqual(sub(0, 5), -5)
        self.assertEqual(sub(5, 5), 0)

    def test_multiply(self):
        self.assertEqual(multiply(10, 10), 100)
        self.assertEqual(multiply(0, 10), 0)
        self.assertEqual(multiply(-2, 5), -10)

    def test_divide(self):
        self.assertEqual(divide(100, 5), 20)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(0, 5), 0)
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)  # Tests division by zero

if __name__ == "__main__":
    unittest.main()
