palavra = input("Digite uma palavra: ")
caractere = input("Digite um caractere: ")

vogais = "aeiouAEIOU"
num_vogais = 0

for letra in palavra:
    if letra in vogais:
        num_vogais += 1

nova_palavra = palavra.replace("a", caractere).replace("e", caractere).replace("i", caractere).replace("o", caractere).replace("u", caractere).replace("A", caractere).replace("E", caractere).replace("I", caractere).replace("O", caractere).replace("U", caractere)

print("Número de vogais na palavra:", num_vogais)
print("Nova palavra:", nova_palavra)
