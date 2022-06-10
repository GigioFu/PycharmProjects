from time import sleep
print("-=-" * 20)
print("{:^70}".format("\033[1;33mContagem regressiva se iniciando...\033[m"))
print("-=-" * 20)
for i in range(10, 0, -1):
    print(i)
    sleep(1)
print("FIM")
