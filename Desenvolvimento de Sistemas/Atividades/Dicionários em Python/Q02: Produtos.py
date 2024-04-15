produtos = {}

for i in range(3):
    produto = input(f"Insira o nome do {i + 1} produto: ")
    preco = float(input(f"Insira o preço de {produto}: R$ "))
    produtos[produto] = preco

print("\nProdutos e Preços:")
for produto, preco in produtos.items():
    print(f"{produto}: R$ {preco:.2f}")
