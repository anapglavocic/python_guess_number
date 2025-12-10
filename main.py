import random # Biblioteca para gerar números aleatórios

print ("***********")
print ("Bem vindo ao jogo de adivinhação!")
print ("***********")

numero_secreto = random.randint(1, 100) # Gera um número aleatório entre 1 e 100

acertou = False

while not acertou:
    chute_str = input ("Digite um número entre 1 e 100: ") # Solicita ao usuário que insira um número
    print("Você digitou: ", chute_str)
    chute = int(chute_str) # Converte a entrada do usuário para um número inteiro

    foi_certo = chute == numero_secreto
    foi_maior = chute > numero_secreto
    foi_menor = chute < numero_secreto

    if foi_certo:
        print("Você acertou! O número secreto era ", numero_secreto)
        acertou = True
    else:
        if foi_maior:
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif foi_menor:
            print("Você errou! O seu chute foi menor do que o número secreto.")


print("Fim do jogo.")