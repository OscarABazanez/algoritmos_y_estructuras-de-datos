import unittest
from index import reverse

class checar(unittest.TestCase):
    def test_reverse(self):
        b = reverse("15")
        c = reverse("-89")
        # hola mi nombre es {nombre} y tengo {edad} y me gusta la pizzas
        self.assertEqual(b, "51")
        self.assertEqual(c, "-98")

if __name__ == "__main__":
    unittest.main()