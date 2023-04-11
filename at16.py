# Função para somar 1 no valor ASCII de cada caractere da palavra
def somar_ascii(palavra):
    resultado = ""
    for char in palavra:
        # Soma 1 ao valor ASCII do caractere
        novo_char = chr(ord(char) + 1)
        resultado += novo_char
    return resultado

# Entrada do usuário
entrada = input("Digite uma palavra: ")

# Chamada da função para somar 1 no valor ASCII dos caracteres
resultado = somar_ascii(entrada)

# Saída do resultado
print("A palavra com 1 adicionado ao valor ASCII de cada caractere é:", resultado)
