n = input("Digite algo para ser analizado: ")
print("O tipo:", type(n))
print("É um número?", n.isnumeric())
print("É alfabético?", n.isalpha())
print("É alfaNumérico?", n.isalnum())
print("Está em maiúsculo?", n.isupper())
print("Está em minúsculo?", n.islower())
print("É apenas espaços?", n.isspace())
print("Está capitalizada?", n.istitle())