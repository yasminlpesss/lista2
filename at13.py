string = input("Digite uma string: ")
vogais = "aeiouAEIOU"
string_sem_vogais = ""

for letra in string:
    if letra not in vogais:
        string_sem_vogais += letra

print("A string sem vogais é:", string_sem_vogais)