import math
n = int(input("Digite o ângulo: "))
n2 = math.radians(n)
sen = math.sin(n2)
cos = math.cos(n2)
tg = math.tan(n2)
print("O seno do ângulo {} é: {:.2f}".format(n, sen))
print("O cosseno do ângulo {} é: {:.2f}".format(n, cos))
print("A tangente do ângulo {} é: {:.2f}".format(n, tg))
print("-" * 20)
# Forma do curso:
seno = math.sin(math.radians(n))
coss = math.cos(math.radians(n))
tang = math.tan(math.radians(n))
print("O seno do ângulo {} é: {:.2f}".format(n, seno))
print("O cosseno do ângulo {} é: {:.2f}".format(n, coss))
print("A tangente do ângulo {} é: {:.2f}".format(n, tang))