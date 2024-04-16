while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    if senha != usuario:
        break
    else:
        print("Erro: Senha igual ao nome de usuário. Tente novamente.")

print("Usuário e senha aceitos.")
