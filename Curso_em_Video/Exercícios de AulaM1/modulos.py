# O comando (import 'biblioteca') importa todas as funções de uma biblioteca/módulo.
# import math
# O comando (from 'biblioteca' import 'função') importa apenas a função desejada da biblioteca
# from math import sqrt, ceil
# -----------------------------------------
import math
num = int(input("Qual o número desejado? "))
# sqrt = raiz quadrada
# ceil = arredonda para cima
# floor = arredonda para baixo
raiz = math.sqrt(num)
print("A raiz de {} é {}".format(num, raiz))
print("A raiz de {} é {}".format(num, math.ceil(raiz)))
print("A raiz de {} é {}".format(num, math.floor(raiz)))
