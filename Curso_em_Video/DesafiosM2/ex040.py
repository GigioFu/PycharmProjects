nota = input("Digite as duas notas do aluno: ").strip().split()
n1 = float(nota[0])
n2 = float(nota[1])
md = (n1 + n2) / 2
print("A média do aluno é {}".format(md))
if md < 5.0:
    print("\033[31mO aluno está reprovado!\033[m")
elif md < 6.9:
    print("\033[33mO aluno está de recuperação!\033[m")
else:
    print("\033[32mO aluno está aprovado! Parabéns\033[m")
