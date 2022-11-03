n = (input("Digite 3 números: "))
n = n.split()
a = int(n[0])
b = int(n[1])
c = int(n[2])
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O maior número é: {}".format(maior))
print("O menor número é: {}".format(menor))
