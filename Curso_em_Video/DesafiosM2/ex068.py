from random import randint
print("-=-" * 20)
print("{:^60}".format("Jogo PAR ou ÍMPAR"))
print("-=-" * 20)

tot = 0

while True:
    n = int(input("Digite um número: "))
    cat = input("Par ou ímpar: ").strip()
    comp = randint(0, 9)
    resp = comp + n

    if resp % 2 == 0:
        if cat[0] in "Pp":
            print(f"Parabéns, você jogou {n} e o computador {comp}. Totalizando {resp} que é PAR")
            print("Você VENCEU!!!")
            print("Vamos mais uma...")
            tot += 1
        else:
            print(f"Infelizmente, você jogou {n} e o computador {comp}. Totalizando {resp} que é PAR")
            break

    else:
        if cat[0] in "IiÍí"[0]:
            print(f"Parabéns, você jogou {n} e o computador {comp}. Totalizando {resp} que é ÍMPAR")
            print("Você VENCEU!!!")
            print("Vamos mais uma...")
            tot += 1
        else:
            print(f"Infelizmente, você jogou {n} e o computador {comp}. Totalizando {resp} que é ÍMPAR")
            break
        print("\n")

print("GAME OVER!!!")
print("Você venceu {} vezes!".format(tot))
