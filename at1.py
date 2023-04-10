palavra = input("Digite uma palavra de até 10 caracteres: ")
vogais = "aeiouAEIOU"
count = 0

for letra in palavra:
    if letra in vogais:
        count += 1

print("A palavra", palavra, "tem", count, "vogais.")
