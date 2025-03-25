'''
Crie uma classe abstrata chamada FormaGeometrica com um
método abstrato calcularArea(). Em seguida, crie duas
classes que herdam de FormaGeometrica: Circulo e
Retangulo. Cada uma dessas classes deve implementar o
método calcularArea() de acordo com sua fórmula
específica. Use polimorfismo para calcular a área de diferentes
formas em uma lista. Crie os atributos conforme a necessidade.

Dicas:
Crie uma lista de formas e itere sobre ela, chamando o método
calcularArea() para cada forma.
'''
from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):
    @abstractmethod
    def calcularArea(self):
        pass

class circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def calcularArea(self):
        return math.pi * self.raio ** 2

class retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura
    
formas = [
    circulo(5),
    retangulo(4,6),
    circulo(3),
    retangulo(10,2)
]

for forma in formas:
    print(f'{forma.calcularArea():.2f}')