print("-=-" * 20)
print("{:^60}".format("Tabuada 3.0"))
print("-=-" * 20)
while True:
    n = int(input("Digite a tabuada desejada: "))
    if n < 0:
        break
    for i in range(0, 11):
        print(f"{n} * {i} = {n * i}")
print("Número negativo digitado!! Encerrando programa!")
