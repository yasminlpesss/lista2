# Entrada do usuário
nome = input("Digite um nome: ")

# Verifica se a primeira letra do nome é "a" (maiúscula ou minúscula)
if nome[0].lower() == 'a':
    # Imprime o nome se a primeira letra for "a"
    print("O nome digitado é:", nome)
else:
    print("A primeira letra do nome não é 'a'.")
