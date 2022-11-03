A = float(input("Qual a altura da parede? "))
L = float(input("Qual a largura da parede? "))
Ar = A * L
print("Sabendo que cada litro de tinta pinta 2m² da parede, serão necessários {} litros de tinta.".format(Ar / 2))
