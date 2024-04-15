notas = {}

for i in range(4):
    nota = float(input(f"Insira a nota {i + 1}: "))
    notas[f"Nota {i + 1}"] = nota

media = sum(notas.values()) / len(notas)

print("\nNotas:")
for chave, valor in notas.items():
    print(f"{chave}: {valor}")

print(f"Média: {media:.2f}")
