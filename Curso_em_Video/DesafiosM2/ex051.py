print("-=-" * 20)
print("{:^70}".format("\033[1;33mProgrssão Aritmédica\033[m"))
print("-=-" * 20)
i = int(input("Digite o primeiro termo da P.A. : "))
r = int(input("Digite a razão da P. A. : "))
fim = i + (10 - 1) * r
for i in range(i, fim + r, r):
    print(i, end=" -> ")
print("FIM")
