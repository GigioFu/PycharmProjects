sm = 0
for i in range(0, 6):
    n = int(input("Digite o valor do {}º número: ".format(i + 1)))
    if n % 2 == 0:
        sm += n
print("A soma dos valores pares digitados é: {}".format(sm))
