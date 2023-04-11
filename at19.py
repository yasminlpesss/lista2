# Função para converter uma cadeia de caracteres de letras maiúsculas em letras minúsculas
def converter_para_minusculas(cadeia):
    return cadeia.lower()

# Entrada do usuário
entrada = input("Digite uma cadeia de caracteres em letras maiúsculas: ")

# Chamada da função para converter para letras minúsculas
resultado = converter_para_minusculas(entrada)

# Saída do resultado
print("A cadeia de caracteres em letras minúsculas é:", resultado)
