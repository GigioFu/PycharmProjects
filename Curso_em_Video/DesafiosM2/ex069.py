totman = plus18 = Wless20 = 0

while True:
    ID = int(input("Digite a idade da passoa: "))
    sx = input("Digite o sexo da pessoa [MASC/FEM]").strip()
    if ID > 18:
        plus18 += 1
    if sx[0] in "Mm":
        totman += 1
    if sx[0] in "Ff" and ID < 20:
        Wless20 += 1
    cont = input("Deseja cadastrar outra pessoa [S/N]?: ")
    if cont[0] in "Nn":
        break
print(f"Há um total de {plus18} pessoas maiores de 18 anos. {totman} homens. E {Wless20} mulheres com menos de 20 anos")
