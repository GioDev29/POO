#3. Sistema de Biblioteca
#Descrição: Desenvolva uma classe Livro com atributos para título,
#autor, ano de publicação e disponibilidade. Adicione métodos
#para emprestar e devolver o livro, alterando seu status de
#disponibilidade.

class Livro:
    def __init__(self, titulo, autor, ano, disponibilidade):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponibilidade = disponibilidade
    
    def emprestar (self):
        if self.disponibilidade == "disponvel":
           self.disponibilidade = "indisponivel"
        else:
            print("indisponivel")
    
    def devolver (self):
        if self.disponibilidade == "indisponivel":
            self.disponibilidade = "disponivel"
    
    def info (self):
        print(f"{self.titulo}, {self.autor}, {self.ano}, {self.disponibilidade}")

livro = Livro ("O livro foda", "Saméia", 2004, "indisponivel")
livro.info()
        