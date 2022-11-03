from random import randint
from time import sleep
c = randint(0, 5)
print("-=-" * 20)
print("Estou pensando em um número de 0 a 5, tente adivinhar...")
print("-=-" * 20)
j = int(input("Em qual número eu pensei?? "))
print("PROCESSANDO...")
sleep(2)
if c == j:
    print("Congratulations, você conegiu adivinhar qual número eu pensei!")
else:
    print("Infelizmente eu pensei no número {} e não no {}.".format(c, j))
