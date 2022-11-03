from datetime import date
ano = int(input("Digite o ano de seu nascimento: "))
atual = date.today().year
if atual - ano > 18:
    print("Já possou {} ano/s da hora do alistamento!".format(atual - ano - 18))
elif atual - ano < 18:
    print("Deve se alistar no serviço militar em {} ano/s!".format((atual - ano - 18) * -1))
else:
    print("Está na hora de se alistar!")
