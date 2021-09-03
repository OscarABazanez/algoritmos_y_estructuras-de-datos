import unittest
from index import reverse

class checar(unittest.TestCase):
    def test_reverse(self):
        b = reverse("Lola")
        # hola mi nombre es {nombre} y tengo {edad} y me gusta la pizzas
        self.assertEqual(b, "aloL")
        self.assertEqual(b, "Lola")

if __name__ == "__main__":
    unittest.main()