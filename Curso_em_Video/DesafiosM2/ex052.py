num = int(input("Digite um número para verificar se é primo: "))
mult = 0
for i in range(2, num):
    if num % i == 0:
        mult += 1
if mult != 0 or num == 1 or num == 0:
    print("\033[1;31mO número {} não é primo.\033[m".format(num))
else:
    print("\033[1;32mO número {} é primo.\033[m".format(num))
