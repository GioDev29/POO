numero = int(input())

cont = 0
soma = 1
descarte = 1

while cont < numero:
    print(descarte)
    descarte = soma
    soma = soma + descarte
    cont += 1

    

