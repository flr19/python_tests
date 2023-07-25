import unittest
import fibonacci

class TestFib(unittest.TestCase):

    def test_fib(self):
        result = fibonacci.fibonacci(5)
        print(result)
        self.assertEqual(result,3)
        self.assertEqual(fibonacci.fibonacci(1),0)
        self.assertEqual(fibonacci.fibonacci(2),1)
        self.assertRaises(ValueError,fibonacci.fibonacci,-1)

if __name__=='__main__':
    unittest.main()
