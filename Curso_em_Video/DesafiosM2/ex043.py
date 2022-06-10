print("-=-" * 20)
print("{:^70}".format("\033[1;33mCalculadora IMC\033[m"))
print("-=-" * 20)
peso = float(input("Digite o seu peso em kg: "))
alt = float(input("Digite a sua altura em metros: "))
imc = peso / alt ** 2
print("O seu IMC é {:.1f}".format(imc))
if imc < 18.5:
    print("Você está ABAIXO do peso!")
elif imc < 25:
    print("Você está no peso IDEAL!")
elif imc < 30:
    print("Você está com SOBREPESO!")
elif imc <= 40:
    print("Você está OBESO!")
else:
    print("Você está com OBESIDADE MÓRBIDA")
