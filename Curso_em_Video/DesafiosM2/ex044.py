p = float(input("Digite o preço do produto: R$"))
fp = str(input("Qual a forma de pagamento? (\033[34mdinheiro/cheque\033[m, \033[35mcartão\033[m, \033[36m2x\033[m, \033[30m3x ou mais\033[m): ")).strip().lower()
if fp in "dinheiro cheque":
    print("Pagamento em forma de dinheiro ou cheque possui {}10% de desconto{}!".format("\033[1;32m", "\033[m"))
    print("O valor a ser pago pelo produto será de R${:.2f}".format(p - (p * 0.1)))
elif fp in "cartão":
    print("Pagamento à vista no cartão possui {}5% de desconto{}!".format("\033[1;32m", "\033[m"))
    print("O valor a ser pago pelo produto será de R${:.2f}".format(p - (p * 0.05)))
elif fp in "2x":
    print("Pagamento em 2x no cartão {}não possui desconto{}!".format("\033[1;33m", "\033[m"))
    print("O valor a ser pago pelo produto será de R${:.2f}".format(p))
else:
    print("Pagamento em 3x ou mais no cartão {}20% de juros{}!".format("\033[1;31m", "\033[m"))
    print("O valor a ser pago pelo produto será de R${:.2f}".format(p + (p * 0.2)))
