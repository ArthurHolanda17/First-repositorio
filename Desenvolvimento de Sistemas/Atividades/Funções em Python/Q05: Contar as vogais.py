def conta_vogais(string):

    vogais = "aeiouAEIOU"

    return sum(1 for char in string if char in vogais)

string_input = input("Digite uma string para contar as vogais: ")
numero_vogais = conta_vogais(string_input)
print("O número de vogais na string é:", numero_vogais)
