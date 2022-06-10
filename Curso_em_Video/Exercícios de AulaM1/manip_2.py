# Algumas utilidades e manipulações de caracteres
frase = "Olá, tenha um Bom dia!"
# Contar quantos microespaços de memória foi alocado (tamanho) = (22)
print(len(frase))
# Colocar toda a string em maiúscula
print(frase.upper())
# Coloca toda a string em minúscula
print(frase.lower())
# Coloca maiúsculo no início de cada palavra
print(frase.title())
# Coloca em maiúculo apenas a primeira letra da string
print(frase.capitalize())

# Essa frase possui espaços antes e depois das palavras
frase = "     Olá, tenha um Bom dia    !      "
print(frase)

# Utilize para retirar esses espaços (colocando 'r' ou 'l' pode se focalizar num lado da string (frase.rstrip()/frase.lstrip()))
print(frase.strip())
frase = "Olá, tenha um Bom dia!"
# Separa cada palavra numa string diferente (separando por espaços)
print(frase.split())
# Conta quantos 'x' caracteres tem na string (dentro ou não de um intervalo)
print(frase.count("m"))
print(frase.count("m", 11, 15))
# Procura e retorno a posição do primeiro caractere de uma palavra (iniciando do 0)
print(frase.find("Bom"))
# No caso de não existir a palavra procurada, retornará "-1"
print(frase.find("android"))
# Substitui uma palavra/caracter por outro
print(frase.replace("tenha", "android"))
# Verifica e retorna positivo caso haja a palavra/caracter na string
print("tenha" in frase)
print("android" in frase)
# junta strings diferentes em um utilizando qualquer caracter
print(frase.split())
print(">>>".join(frase.split()))
print("---".join(frase.split()))
