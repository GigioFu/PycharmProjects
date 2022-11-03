n = int(input("Digite um número inteiro: "))
op = int(input("""Qual base de conversão deseja? 
(\033[34m1 - binário\033[m / \033[35m2 - octal\033[m / \033[36m3 - hexadecimal\033[m): """))
if op == 1:
    conv = bin(n)[2:]
    print("O número {}{}{} em {}{}{} é {:2}!".format("\033[33m", n, "\033[m", "\033[34m", "binário", "\033[m", conv))
elif op == 2:
    conv = oct(n)[2:]
    print("O númeor {}{}{} em {}{}{} é {}!".format("\033[33m", n, "\033[m", "\033[35m", "octal", "\033[m", conv))
elif op == 3:
    conv = hex(n)[2:]
    print("O número {}{}{} em {}{}{} é {}!".format("\033[33m", n, "\033[m", "\033[36m", "hexadecimal", "\033[m", conv))
else:
    print("\033[31mVocê não digitou uma opção válida!\033[m")
