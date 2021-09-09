import unittest
from index import capital

class Capital(unittest.TestCase):
    def test_capital(self):
        b = capital('a sHort centence')
        c = capital('hola MUNDO COMO ESTAS')
        self.assertEqual(b, "A Short Centence")
        self.assertEqual(c, 'Hola Mundo Como Estas')

if __name__ == "__main__":
    unittest.main()