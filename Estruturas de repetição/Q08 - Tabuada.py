numero_tabuada = int(input("Digite um número para a tabuada: "))

print(f"Tabuada de {numero_tabuada}:")
for i in range(1, 11):
    resultado = numero_tabuada * i
  print(f"{numero_tabuada} X {i} = {resultado}")
