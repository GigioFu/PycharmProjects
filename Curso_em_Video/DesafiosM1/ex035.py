print("-=-" * 20)
print("Analizando retas")
print("-=-" * 20)
tam = input("Digite o comprimento de três retas: ")
tam = tam.split()
tam[0] = int(tam[0])
tam[1] = int(tam[1])
tam[2] = int(tam[2])
if (tam[0] + tam[1]) <= tam[2] or (tam[1] + tam[2]) <= tam[0] or (tam[0] + tam[2]) <= tam[1]:
    print("As retas NÃO podem formar um triângulo")
else:
    print("As retas PODEM formar um triângulo")
