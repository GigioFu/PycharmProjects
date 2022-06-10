tot = totm = menor = nmenor = i = 0
while True:
    nome = input("Qual o nome do produto?: ").strip()
    preco = float(input("Qual o preço do produto? R$"))
    tot += preco
    if preco > 1000:
        totm += 1
    if i == 0:
        menor = preco
        i += 1
    if preco < menor:
        nmenor = nome
        menor = preco

    resp = " "
    while resp not in "SN":
        resp = input("Deseja continuar? [S/N] ").strip().upper()[0]
    if resp == "N":
        break
print("{:=^40}".format("FIM DO PROGRAMA"))
print("O total gasto foi de R${:.2f}".format(tot))
print("Um total de {} produtos custaram mais de R$1000".format(totm))
print("O produto mais barato foi {}.".format(nmenor))
