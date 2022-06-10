from datetime import date
ano = int(input("Digite o ano de nascimento do atleta: "))
at = date.today().year
ida = at - ano
if ida <= 9:
    print("O atleta se encaixa na categoria: \033[33mMIRIM\033[m")
elif ida <= 14:
    print("O atleta se encaixa na categoria: \033[33mINFANTIL\033[m")
elif ida <= 19:
    print("O atleta se encaixa na categoria: \033[33mJUNIOR\033[m")
elif ida <= 20:
    print("O atleta se encaixa na categoria: \033[33mSENIOR\033[m")
else:
    print("O atleta se encaixa na categoria: \033[33mMASTER\033[m")
