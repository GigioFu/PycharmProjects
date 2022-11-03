n = input("Qual é o seu nome?")
# Normal
print("Olá {}, prazer em te conhecer!".format(n))
# Em 20 caracteres
print("Olá {:20}, prazer em te conhecer!".format(n))
# Em 20 caracteres formatado no início
print("Olá {:<20}, prazer em te conhecer!".format(n))
# Em 20 caracteres formatado no final
print("Olá {:>20}, prazer em te conhecer!".format(n))
# Em 20 caracteres formatados no meio
print("Olá {:^20}, prazer em te conhecer!".format(n))
# Em 20 caracteres formatado no meio entre '='
print("Olá {:=^20}, prazer em te conhecer!".format(n))
# '!' 20 vezes
print("="*20)
