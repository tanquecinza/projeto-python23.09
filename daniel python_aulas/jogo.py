import random


def chute():
    return random.choice([True, False])


def jogo():
    print("Bem-vindo ao jogo de Gol a Gol!")
    print("Você tem 5 chutes para tentar marcar o maior número de gols.")

    gols = 0
    tentativas = 5

    for tentativa in range(tentativas):
        input(f"Tentativa {tentativa + 1}: Pressione Enter para chutar!")
        if chute():
            print("GOOOOL! Você marcou um gol!")
            gols += 1
        else:
            print("A bola foi pra fora! Tente novamente.")

    print(f"\nFim do jogo! Você marcou {gols} gol(s) em {tentativas} tentativas.")


if __name__ == "__main__":
    jogo()
