import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(10, -2), 8)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)
        self.assertEqual(self.calc.subtract(-2, 2), -4)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(8, 2), 16)
        self.assertEqual(self.calc.multiply(3, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(9, 2), 4)
        self.assertEqual(self.calc.divide(43, 12), 3)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(6,4),2)
        self.assertEqual(self.calc.modulo(70,9),7)
        self.assertEqual(self.calc.modulo(20,5),0)

    # Add the following test methods to the TestCalculator class:

    def main(self):
        self.test_add()
        self.test_subtract()
        self.test_multiply()
        self.test_divide()


if __name__ == '__main__':
    unittest.main()