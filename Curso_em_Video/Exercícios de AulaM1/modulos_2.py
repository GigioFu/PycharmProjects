# O comando (import 'biblioteca') importa todas as funções de uma biblioteca/módulo.
# import math
# O comando (from 'biblioteca' import 'função') importa apenas a função desejada da biblioteca
# from math import sqrt, ceil, floor
# -----------------------------------------
from math import sqrt
num = int(input("Qual o número desejado? "))
# sqrt = raiz quadrada
# ceil = arredonda para cima
# floor = arredonda para baixo
raiz = sqrt(num)
print("A raiz de {} é {:.2f}".format(num, raiz))
