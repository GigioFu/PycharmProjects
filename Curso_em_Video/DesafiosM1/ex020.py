from random import shuffle
n1 = input("Qual o nome do primeiro aluno: ")
n2 = input("Qual o nome do segundo aluno: ")
n3 = input("Qual o nome do terceiro aluno: ")
n4 = input("Qual o nome do quarto aluno: ")
n = [n1, n2, n3, n4]
shuffle(n)
print("A ordem de apresentação será {}".format(n))
