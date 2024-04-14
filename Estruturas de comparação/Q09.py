salario = float(input("Digite o salário do colaborador: "))

if salario <= 280:
    percentual_aumento = 20
elif salario <= 700:
    percentual_aumento = 15
elif salario <= 1500:
    percentual_aumento = 10
else:
    percentual_aumento = 5

aumento = (percentual_aumento / 100) * salario
novo_salario = salario + aumento

print("Salário antes do reajuste:", salario)
print(f"Percentual de aumento aplicado: {percentual_aumento}%")
print("Valor do aumento: R$", aumento)
print("Novo salário após o aumento: R$", novo_salario)
