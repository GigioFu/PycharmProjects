print("-=-" * 20)
print("{:^60}".format("Progressão Aritmética"))
print("-=-" * 20)

x = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a Razão da PA: "))

cont = 10
while cont != 0:
    print("{}{}{}{}".format("\033[1;33m", x, " -> ", "\033[m"), end="")
    x += r
    cont -= 1
print("FIM")
