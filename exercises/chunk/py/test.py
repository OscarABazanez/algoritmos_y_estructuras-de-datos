import unittest
from index import chunk

class checar(unittest.TestCase):
    def test_chunk(self):
        b = chunk([1, 2, 3, 4], 2)
        c = chunk([1, 2, 3, 4, 5], 2)
        # hola mi nombre es {nombre} y tengo {edad} y me gusta la pizzas
        self.assertEqual(b, [[1, 2], [3, 4]])
        self.assertEqual(c, [[1, 2], [3, 4], [5]])

if __name__ == "__main__":
    unittest.main()