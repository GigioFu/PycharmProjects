from random import choice
from time import sleep

print("-=-" * 20)
print("{}{:^60}{}".format("\033[34m", "Jokenpô", "\033[m"))
print("-=-" * 20)
esq = str(input("Vamos jogar Jokenpô! Escolha entre {} Pedra, Papel e Tesoura{}! ".format("\033[1;35m", "\033[m"))
          ).lower().strip().capitalize()
print("-=-" * 20)
print("{}{:^60}{}".format("\033[34m", "Processando", "\033[m"))
sleep(2)
print("-=-" * 20)
comp = choice(["Pedra", "Papel", "Tesoura"])
if comp == esq:
    print("{}Ops tivemos um empate, parabéns!!{}".format("\033[1;34m", "\033[m"))
elif comp == "Pedra":
    if esq == "Papel":
        print("{}Parabéns!! Você escolheu {} e eu {}{}".format("\033[1;32m", esq, comp, "\033[m"))
    else:
        print("{}Boa sorte na Próxima!! Você escolheu {} e eu {}{}".format("\033[1;31m", esq, comp, "\033[m"))
elif comp == "Papel":
    if esq == "Tesoura":
        print("{}Parabéns!! Você escolheu {} e eu {}{}".format("\033[1;32m", esq, comp, "\033[m"))
    else:
        print("{}Boa sorte na Próxima!! Você escolheu {} e eu {}{}".format("\033[1;31m", esq, comp, "\033[m"))
elif comp == "Tesoura":
    if esq == "Pedra":
        print("{}Parabéns!! Você escolheu {} e eu {}{}".format("\033[1;32m", esq, comp, "\033[m"))
    else:
        print("{}Boa sorte na Próxima!! Você escolheu {} e eu {}{}".format("\033[1;31m", esq, comp, "\033[m"))
