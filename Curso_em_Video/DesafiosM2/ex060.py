n = int(input("Digite um número para calcular seu fatorial: "))
valor = 1
print("{}! = ".format(n), end="")
for i in range(n, 0, -1):
    valor *= i
    """
    if i > 1:
        print("{} * ".format(i), end="")
    else:
        print("{} = {}".format(i, valor), end="")
        """
    print("{}".format(i), end="")
    print(" * " if i > 1 else " = ", end="")
print(valor)
