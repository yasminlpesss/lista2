# Função para converter letras maiúsculas em letras minúsculas usando a tabela ASCII
def converter_para_minusculas(cadeia):
    resultado = ""
    for char in cadeia:
        # Verifica se o caractere é uma letra maiúscula (código ASCII entre 65 e 90)
        if 65 <= ord(char) <= 90:
            # Subtrai 32 do código ASCII para converter em letra minúscula
            char = chr(ord(char) + 32)
        resultado += char
    return resultado

# Entrada do usuário
entrada = input("Digite uma cadeia de caracteres em letras maiúsculas: ")

# Chamada da função para converter para letras minúsculas
resultado = converter_para_minusculas(entrada)

# Saída do resultado
print("A cadeia de caracteres em letras minúsculas é:", resultado)
