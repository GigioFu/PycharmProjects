print("{}{}{}".format("\033[33m", "-=-" * 20, "\033[m"))
print("{}{:^60}{}".format("\033[31m", "Aprovador de empréstimos", "\033[m"))
print("{}{}{}".format("\033[33m", "-=-" * 20, "\033[m"))

v = float(input("Insira o valor da casa: R$"))
s = float(input("Insira o valor do seu salário: R$"))
p = int(input("Em quantos anos pretende pagar? "))
pre = v / (p * 12)
mini = s * 0.3
print("Caso seja aprovado, você irá pagar R${:.2f} p/ mês".format(pre))

if pre > mini:
    print("Infelizmente o valor excede 30% do seu salário.\n\033[31m NÃO será possível aprovar o empréstimo\033[m")
else:
    print("Parabéns, seu empréstimo foi \033[32mAPROVADO\033[m")
