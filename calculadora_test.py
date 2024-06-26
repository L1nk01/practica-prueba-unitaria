import unittest
from Calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calculadora = Calculadora()

    def test_suma(self):
        self.assertEqual(self.calculadora.suma(2, 3), 5)

    def test_resta(self):
        self.assertEqual(self.calculadora.resta(5, 2), 3)

    def test_multiplicacion(self):
        self.assertEqual(self.calculadora.multiplicacion(4, 6), 24)

    def test_division(self):
        self.assertEqual(self.calculadora.division(10, 2), 5.0)

    def test_raiz_cuadrada(self):
        self.assertEqual(self.calculadora.raiz_cuadrada(9), 3)

if __name__ == '__main__':
    unittest.main()