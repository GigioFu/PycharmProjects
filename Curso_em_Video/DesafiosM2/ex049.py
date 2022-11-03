print("-=-" * 20)
print("{:^70}".format("\033[1;34mGerador de tabuada\033[m"))
print("-=-" * 20)
n = float(input("Digite o um número para gerar sua tabuada: "))
for i in range(1, 10):
    print("{:.0f} x {} = {:2.0f}".format(n, i, n * i))
