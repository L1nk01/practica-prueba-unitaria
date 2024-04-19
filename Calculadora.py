import math

class Calculadora:
    def suma(self, a, b):
        resultado = int(a) + int(b)
        return resultado

    def resta(self, a, b):
        resultado = int(a) - int(b)
        return resultado

    def multiplicacion(self, a, b):
        resultado = int(a) * int(b)
        return resultado

    def division(self, a, b):
        resultado = int(a) / int(b)
        return resultado
    
    def raiz_cuadrada(self, a):
        resultado = math.sqrt(a)
        return resultado