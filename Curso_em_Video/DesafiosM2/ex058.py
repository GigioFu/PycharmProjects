from random import randrange
print("-=-" * 20)
print("{:^60}".format("Jogo da advinhação"))
print("-=-" * 20)
tent = 0
print("Eu irei pensar em um número e você deve acertar!")
pens = randrange(1, 10)
num = int(input("Digite um número de 1 a 10: "))
while num != pens:
    tent += 1
    print("Infelizmente você não acertou! Tente novamente:\n\t")
    num = int(input("Digite um número de 1 a 10: "))
print("Meus parabéns, você acertou o número que eu pensei em {} tentativas!!".format(tent))
