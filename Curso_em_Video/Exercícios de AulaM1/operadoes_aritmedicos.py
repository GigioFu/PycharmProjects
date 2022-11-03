n1 = int(input("Qual o primeiro número? "))
n2 = int(input("Qual o segundo número? "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2
# para formatar 3 números após a vírgula (:.3f)
# Para não pular a linha e/ou adicional algo no final (end = ' ') e para adicionar outra linha (\n)
print("A soma é {},\nO produto é: {} e a divisão é: {:.3f}".format(s, m, d), end=" ")
print("A divisão inteira é: {}, a potência é: {} e o resto é: {}".format(di, e, r))
