import random

def jogar():
    print("*" * 32)
    print("Bem vindo ao jogo de Advinhação!")
    print("*" * 32)
    print("Você tem até 3 tentativas")

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil, (2) Médio, (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada,tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))

        if(chute < 1 or chute > 100):
            print("Número inválido. Digite um número entre 1 e 100.")
            continue

        acerto = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        print("Vocë digitou {}".format(chute))

        if(acerto):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou... Seu chute foi maior que o número secreto.")
                if (rodada == tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto,pontos))
            elif(menor):
                print("Você errou... Seu chute foi menor que o número secreto.")
                if (rodada == tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto,pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


    print(f"O número secreto era {numero_secreto}")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()