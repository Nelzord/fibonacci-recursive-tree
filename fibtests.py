import unittest
import fib

class TestAssign1(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib.fib(1), 1)

    def test_fib2(self):
        self.assertEqual(fib.fib(0), 0)

    def test_fib3(self):
        self.assertEqual(fib.fib(25), 75025)
        
    def test_fibfoo(self):
        self.assertEqual(fib.fibnoreclist(8), [1, 1, 2, 3, 5, 8, 13, 21])
if __name__ ==  "__main__":
        unittest.main()
