palavra = input("Digite uma palavra: ")
nova_palavra = ""

for letra in palavra:
    codigo_ascii = ord(letra) + 1
    nova_letra = chr(codigo_ascii)
    nova_palavra += nova_letra

print("Nova palavra:", nova_palavra)