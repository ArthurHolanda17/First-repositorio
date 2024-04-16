preco1 = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))

produto_mais_barato = min(preco1, preco2, preco3)
print("Você deve comprar o produto de R$", produto_mais_barato)
