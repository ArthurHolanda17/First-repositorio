#1 - Modele uma pessoa!
print("._____________.")
print("| Bem-vindo ao cadastro de usuário! |")
print("|_____________|")
print(" ")
print("Iremos iniciar com um questionário, ok?")

        #esperar 0.5
        #limpatela

print("PART 1/3")
Nome = str(input(print("Let's go! Qual o seu nome?")))
Idade = int(input(print("Qual ano você nasceu?")))
calculoIdade = (2023 - Idade)

if calculoIdade >= 18:
    continue #ou pass?
else:
    print("Parece que você ainda não atingiu a idade mínima...")
    #colocar uma tela de carregamento " . . . "
    break

print("PART 2/3 - Descrições adicionais.")
Altura = float(input(print("Altura (em cm): "))
Peso =  float(input(print("Peso (em Kg): ")))
Genero = str(input(print("Gênero (F/M): ")))
    if Genero == F:
        Genero = Mulher
    else:
        Genero = Homem

CPF = str(input(print("CPF: ")))
endereco = int(input(print("CEP: ")))

#limpa tela
print("PART 3/3 - CONTATO")
numero = str(input(print("Número: "))))
email = str(input(print("E-mail: ")))

        #esperar 0.5
        #limpatela

""" 
.___________.
|    MODELAÇÃO DEFINITIVA       |
|    falar (conteudoFala)       |
|    andar (destino)            |
|    dormir (lugar, tempo)      |
|    comer (alimento)           |
|___________|

.___________.
|            SAÍDAS             |
|___________|

"""
