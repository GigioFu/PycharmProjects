lados = input("Digite os tamanhos dos 3 segmentos de retas do triângulo: ").strip().split()
l1 = int(lados[0])
l2 = int(lados[1])
l3 = int(lados[2])
if l1 + l2 > l3 and l1 + l3 > l2 and l3 + l2 > l1:
    print("\033[1;32mO triângulo existe!\033[m")
    if l1 == l2 == l3:
        print("Esse triângulo é \033[1;33mEquilatero\033[m (Possui todos os lados iguais)")
    elif l1 != l2 != l3:
        print("Esse triângulo é \033[1;33mEscaleno\033[m (Possui todos os lados diferentes)")
    else:
        print("Esse triângulo é \033[1;33mIsósceles\033[m (Possui apenas dois lados iguais)")
else:
    print("\033[1;31mO triângulo não existe!")
