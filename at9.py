# recebe a entrada do usuário
string = input("Digite a string: ")

# inicializa um contador de 1's
contador = 0

# percorre cada caractere da string
for caractere in string:
    # se o caractere for 1, incrementa o contador
    if caractere == '1':
        contador += 1

# exibe o resultado
print("O número de 1's na string é:", contador)
