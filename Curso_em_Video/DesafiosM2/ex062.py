print("-=-" * 20)
print("{:^60}".format("Progressão Aritmética"))
print("-=-" * 20)

x = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a Razão da PA: "))
cont = True
tot = 10

for i in range(0, tot):
    print("{}{}{}{}". format("\033[1;33m", x, " -> ", "\033[m"), end="")
    x += r
print("Pausa")
while cont:
    resp = int(input("Deseja mostrar mais quantos termos?: "))
    tot += resp
    if resp != 0:
        for i in range(0, resp):
            print("{}{}{}{}".format("\033[1;33m", x, " -> ", "\033[m"), end="")
            x += r
        print("Pausa")
    else:
        cont = False
print("A progrssão foi finalizada após mostras {} termos!".format(tot))
