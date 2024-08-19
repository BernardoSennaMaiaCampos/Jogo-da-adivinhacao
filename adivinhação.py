import random

def main():
    print("\nBem vindo ao Jogo da Adivinhação! Este jogo gera aleatoriamente um número de 1 a 100. Você terá quantas chances precisar para conseguir adivinhar corretamente     o número gerado. Ao longo das tentativas, o jogo te dará dicas se o número que digitou está abaixo ou acima que o número gerado.\n" )
    adivinhacao()

def adivinhacao():
    tentativa = 1
    numeroEscolhido = random.randint(1, 10)
    numero = int(input(f"\nAdivinhe um número, {tentativa}ª tentativa: "))
    
    while numero != numeroEscolhido:
        tentativa +=1
        if numero > numeroEscolhido:
            print("\nO número está abaixo.")
            numero = int(input(f"\nAdivinhe um número, {tentativa}ª tentativa: "))
        elif numero < numeroEscolhido:
            print("\nO número está acima.")
            numero = int(input(f"\nAdivinhe um número {tentativa}ª tentativa: "))
        else:
            print("\n\nValor incorreto, por favor, tente novamente.")
            return adivinhacao()
    
    if  numero == numeroEscolhido:
            print("\n\nAcertou!")
            return jogarnovamente()
    else:
            print("\n\nOpção inválida, por favor, tente novamente.")
            return adivinhacao() 


def jogarnovamente():
    jogar = int(input(print("\n\nDeseja jogar novamente?\n\n1 - Sim.\n2 - Não.\n\nVocê escolheu: ")))
    
    match jogar:
        case 1:
            print("\nBem vindo de volta ao jogo!")
            return adivinhacao()
        case 2:
            print("\nO jogo se encerrou.")
            exit()
        case _:
            print("\nOpção inválida, por favor, tente novamente.")
            return jogarnovamente()

main()
