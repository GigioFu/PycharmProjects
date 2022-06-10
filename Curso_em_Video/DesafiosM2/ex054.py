from datetime import date
atual = date.today().year
maior = menor = 0
for i in range(0, 7):
    nasc = int(input("Em que ano a {}ª pessoa nasceu: ".format(i + 1)))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print("Temos um total de {} pessoas maiores de 18 anos e {} menores".format(maior, menor))
