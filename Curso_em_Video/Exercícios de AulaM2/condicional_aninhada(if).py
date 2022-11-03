nome = input("Qual é o seu nome? ")
if nome == "Geovane" or nome == "Luísa":
    print("Seu nome é muito lindo!")
elif nome in "Ana Cláudia Maria":
    print("Seu nome é muito popular!")
else:
    print("Seu nome é normal!")
print("Prazer em te conhecer, {}!".format(nome))
