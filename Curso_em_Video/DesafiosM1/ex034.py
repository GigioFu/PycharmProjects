sal = float(input("Digite seu salário: "))
if sal > 1250:
    print("Com o aumento do salário em 10%, seu salário será {:.2f} reais".format(sal + (sal * 0.1)))
else:
    print("Com o aumento do salário em 15%, seu salário será {:.2f} reais".format(sal + (sal * 0.15)))
