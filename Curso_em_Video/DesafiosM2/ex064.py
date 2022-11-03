flag = tot = vz = 0
while flag != 999:
    flag = int(input("Digite um número [999 para parar]: "))
    tot += flag
    vz += 1
print("Foram inseridos {} números e a soma total foi {}!".format(vz - 1, abs(tot - 999)))
