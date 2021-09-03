import unittest
from index import palindrome

class checar(unittest.TestCase):
    def test_palindrome(self):
        a = palindrome("abba")
        b = palindrome("aza")
        self.assertTrue(a)
        self.assertTrue(b)

if __name__ == "__main__":
    unittest.main()