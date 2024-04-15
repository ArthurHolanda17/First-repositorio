funcionarios = {}

for i in range(3):
    nome = input(f"Insira o nome do {i + 1}º funcionário: ")
    funcionarios[nome] = True

print("\nFuncionários:")
for nome in funcionarios:
    print(nome)

nome_demitido = input("\nInsira o nome do funcionário a ser demitido: ")

if nome_demitido in funcionarios:
    del funcionarios[nome_demitido]
    print(f"\nFuncionário {nome_demitido} demitido com sucesso!")
else:
    print(f"\nFuncionário {nome_demitido} não encontrado.")

print("\nFuncionários restantes:")
for nome in funcionarios:
    print(nome)
