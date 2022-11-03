med = vz = tot = 0
num = int(input("Digite um número [0 para parar]: "))
maior = menor = num

while num != 0:
    tot += num
    vz += 1
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    num = int(input("Digite um número [0 para parar]: "))
med = tot / vz
print("A média dos valores digitados é {}, o maior valor digitado foi {} "
      "e o menor valor foi {}!".format(med, maior, menor))
