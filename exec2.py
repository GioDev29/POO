#Preencha um dicionário com as informações de 5 produtos fornecidos pelo usuário.
'''- Solicite os dados ao usuário
- Utilize o nome do produto como chave e o preço como valor.
- Percorra o dicionário e exiba o nome dos produtos com preço
superior a R$ 50,00.
Exemplo:
Veja um exemplo da estrutura do dicionário.
{'caneta': 3.0, 'Pen drive': 100.0,'Teclado': 30.0, 'Lápis': 1.5}'''


dicionario = {}
qtd = 2
preco = 50
cont = 0

while cont < qtd:
    nome = input("produto:")
    valor = float(input("valor:"))
    dicionario[nome] = valor
    cont += 1

for chave, valor in dicionario.items():
    if valor >= preco:
        print(f'{nome} : {valor}')