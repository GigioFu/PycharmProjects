# código padrão ANSI 033 (mais compatível com Python) (SEM BIBLIOTECAS)
# \033[**;**;**m (o '**;**;**' é o código)
# -----S--T--B------ S = Style / T = Text / B = Back

# ==================================================================================

# S = [0, 1, 4, 7] (Estilo) (tem mais, mas esses são os melhores para python)
# 0 = None
# 1 = Bold (negrito)
# 4 = Underline (Sublinhado)
# 7 = Negativo (inverte o T e B)

# ==================================================================================

# T = [30, 31, 32, 33, 34, 35, 36, 37] (Cores do texto)
# 30 = branco
# 31 = vermelho
# 32 = verde
# 33 = amarelo
# 34 = azul
# 35 = roxo
# 36 = ciano
# 37 = cinza

# ==================================================================================

# B = [40, 41, 42, 43, 44, 45, 46, 47] (Cores do fundo)
# 40 = branco
# 41 = vermelho
# 42 = verde
# 43 = amarelo
# 44 = azul
# 45 = roxo
# 46 = ciano
# 47 = cinza

# ==================================================================================

print("\033[0;30;41mteste", end="\033[m ")
print("\033[4;33;44mteste", end="\033[m ")
print("\033[1;35;43mteste", end="\033[m ")
print("\033[0;30;42mteste", end="\033[m ")
print("\033[7;30mteste", end="\033[m ")
print("\033[7mteste", end="\033[m\n")

# ==================================================================================

print("\033[7;33;44mOlá mundo\033[m")

print("Os valores são \033[31m{}\033[m e \033[32m{}\033[m!".format(3, 5))

print("Olá meu nome é {}{}{}!".format("\033[4;34m", "Geovane Otávio", "\033[m"))

cores = {"limpa": "\033[m",
        "azul": "\033[34m",
        "vermelho": "\033[31m"}
print("Olá {}Seja bem vindo{}!!".format(cores["vermelho"], cores["limpa"]))
