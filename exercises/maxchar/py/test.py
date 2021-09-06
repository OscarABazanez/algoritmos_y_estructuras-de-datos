import unittest
from index import reverse

class checar(unittest.TestCase):
    def test_reverse(self):
        b = reverse("abcccccccd")
        c = reverse("apple 1231111")
        # hola mi nombre es {nombre} y tengo {edad} y me gusta la pizzas
        self.assertEqual(b, "c")
        self.assertEqual(c, "1")

if __name__ == "__main__":
    unittest.main()