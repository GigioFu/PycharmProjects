maior = menor = 0
for i in range(0, 5):
    n = float(input("Digite o peso da {}ª pessoa: ".format(i + 1)))
    if i == 0:
        maior = menor = n
    if maior < n:
        maior = n
    if menor > n:
        menor = n
print("O {}maior peso foi de {:.1f}Kg{} e o {}menor peso foi de {:.1f}Kg.{} ".format("\033[1;33m", maior, "\033[m", "\033[1;32m", menor, "\033[m"))
