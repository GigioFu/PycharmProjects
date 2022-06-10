vz = tot = 0
while True:
    num = int(input("Digite um número [999 para parar]: "))
    if num == 999:
        break
    tot += num
    vz += 1
print(f"Foram digitados {vz} números e a soma total vale {tot}!")
