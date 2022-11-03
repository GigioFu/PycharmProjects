n = input("Digite dois valores: ").strip().split()
n1 = int(n[0])
n2 = int(n[1])
if n1 > n2:
    print("O primeiro valor é maior!")
elif n2 > n1:
    print("O segundo valor é maior!")
else:
    print("Os dois valores são iguais!")
