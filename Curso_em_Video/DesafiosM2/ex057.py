sx = input("Informe se sexo [M/F]: ").strip().upper()[0]
while sx not in "FM":
    sx = input("{}Dados inválidos{}\nInforme se sexo [M/F]: ".format("\033[1;31m", "\033[m")).strip().upper()[0]
