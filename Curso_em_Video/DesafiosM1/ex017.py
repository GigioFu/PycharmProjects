from math import sqrt, hypot
co = float(input("Qual o comprimento do cateto OPOSTO do triângulo retângulo: "))
ca = float(input("Qual o comprimento do cateto ADJACENTE do triângulo retângulo: "))
hypo = (ca ** 2) + (co ** 2)
hypo = sqrt(hypo)
print("O valor da Hipotenusa é {:.2f}".format(hypo))
print("=" * 20)
# Outra forma de fazer
print("O valor é {:.2f}".format(hypot(co, ca)))
