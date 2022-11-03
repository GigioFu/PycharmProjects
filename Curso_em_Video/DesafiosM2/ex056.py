print("{}{}{}".format("\033[1;33m", "===" * 20, "\033[m"))
print("{}{:^60}{}".format("\033[1;32m", "Analizador de Pessoas", "\033[m"))
print("{}{}{}".format("\033[1;33m", "===" * 20, "\033[m"))
print("Esse programa irá ler o nome, idade e sexo de quatro pessoas e fazer a analize\n")

medID = 0
maiIDH = 0
nomH = ""
menor = 0
for i in range(1, 5):
    print("========= {}ª PESSOA =========".format(i))
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sx = input("Sexo [M/F]: ").strip()
    medID += idade
    if i == 1 and sx in "Mm":
        maiIDH = idade
        nomH = nome
    if sx in "Mm" and idade > maiIDH:
        maiIDH = idade
        nomH = nome
    if sx in "Ff" and idade < 20:
        menor += 1

print("A média de idade do grupo é de {:.1f} anos!".format(medID/4))
print("O homem mais velho se chama {} e possui {} anos!".format(nomH, maiIDH))
print("Nesse grupo há {} mulheres com menos de 20 anos!".format(menor))
