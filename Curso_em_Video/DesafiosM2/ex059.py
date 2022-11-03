print("Calculadora inteligente: ")
x = int(input("Digite um número inteiro: "))
y = int(input("Digite outro número inteiro: "))
print("\n")
cont = True
while cont:
    print("{}{}{}".format("\033[1;33m", "[1] - Somar", "\033[m\n"))
    print("{}{}{}".format("\033[1;33m", "[2] - Multiplicar", "\033[m\n"))
    print("{}{}{}".format("\033[1;33m", "[3] - Maior", "\033[m\n"))
    print("{}{}{}".format("\033[1;33m", "[4] - Novos números", "\033[m\n"))
    print("{}{}{}".format("\033[1;33m", "[5] - Sair da calculadora", "\033[m\n"))
    opc = int(input("Digite a opção desejada listada acima: "))
    if opc == 1:
        print("A soma dos valores é: ", x + y)
    elif opc == 2:
        print("A multiplicação dos valores é: ", x * y);
    elif opc == 3:
        if x >= y:
            maior = x
        else:
            maior = y
        print("O maior valor digitado foi: ", maior)
    elif opc == 4:
        x = int(input("Digite um número inteiro: "))
        y = int(input("Digite outro número inteiro: "))
    else:
        cont = False
