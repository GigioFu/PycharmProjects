print("-=-" * 20)
print("{:^60}".format("Sequência de Fibonacci"))
print("-=-" * 20)

t0 = 0
t1 = 1
cont = 3
n = int(input("Quantos termos deseja mostrar?: "))
print("{} -> {}".format(t0, t1), end="")
while cont <= n:
    t2 = t0 + t1
    print(" -> {}".format(t2), end="")
    t0 = t1
    t1 = t2
    cont += 1
print(" -> FIM")
