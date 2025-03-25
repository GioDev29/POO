class Pessoa:
    def __init__ (self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    def alterar (self, endereco):
        self.endereco = endereco
    
    def exibe (self):
        print(f"{self.nome} , {self.idade} , {self.endereco}")   


person = Pessoa("saméia", 19, "rua das orquideas 17")
person.exibe()
person.alterar("xique xique bahia")
person.exibe()