'''Exercício 3: Métodos de Classe para Controle de Instâncias

Crie uma classe chamada Animal com um atributo de classe
contador que rastreia quantas instâncias de Animal foram
criadas. Use um método de classe para incrementar esse
contador sempre que uma nova instância for criada. Adicione
também um método estático para exibir uma mensagem
genérica sobre animais.

Exemplo de uso:

29

cachorro = Animal("Rex")
gato = Animal("Mimi")
print(Animal.quantidade_instancias()) # Saída: 2
Animal.mensagem_sobre_animais() # Saída: "Animais são seres vivos!"
'''

class Animal:
    contador = 0
    
    def __init__(self, nome):
        self.nome = nome
        self.incrementar_contador()


    @classmethod