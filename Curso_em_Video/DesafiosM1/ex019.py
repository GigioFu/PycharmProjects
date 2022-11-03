from random import choice
n1 = input("Qual o nome do primeiro aluno: ")
n2 = input("Qual o nome do segundo aluno: ")
n3 = input("Qual o nome do terceiro aluno: ")
n4 = input("Qual o nome do quarto aluno: ")
n = [n1, n2, n3, n4]
print("O aluno escolhido foi {}".format(choice(n)))
