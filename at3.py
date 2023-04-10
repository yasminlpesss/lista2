vetA = "COMPUTACAO"
vetB = input("Digite uma palavra de 10 letras: ")

for i in range(len(vetB)):
    if vetB[i].upper() == vetA[i].upper():
        print(i, end=' ')


palavra = input("Digite uma palavra: ")
comprimento = len(palavra)
print("O comprimento da palavra é:", comprimento)
