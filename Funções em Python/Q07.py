def imprime_tabuada(numero):

    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

numero_input = int(input("Digite um número para imprimir sua tabuada: "))
imprime_tabuada(numero_input)
