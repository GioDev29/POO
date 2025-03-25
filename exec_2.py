''''Exercício 2: Métodos Estáticos em uma Calculadora

Crie uma classe chamada Calculadora com métodos estáticos
para operações matemáticas básicas, como somar, subtrair,
multiplicar e dividir. Esses métodos devem ser chamados
diretamente na classe, sem a necessidade de instanciar um
objeto.

Exemplo de uso:

28

resultado = Calculadora.somar(5, 3)
print(resultado) # Saída: 8'''''


class Calculadora:
    @staticmethod
    def somar(a, b):
        return a + b
    
    @staticmethod
    def subtrair(a, b):
        return a - b
    
    @staticmethod
    def multiplicar(a, b):
        return a * b
    
    @staticmethod
    def dividir(a, b):
        return a / b
    
resultado = Calculadora.subtrair(2, 5)
print(resultado)