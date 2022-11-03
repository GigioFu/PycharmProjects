# TUPLAS SÃO IMUTÁVEIS

# Declarando uma Tupla:
lanche = ("Hamburguer", "Suco", "Pizza", "Pudim", "Batata frita")
# ou
# lanche = "Hamburguer", "Suco", "Pizza", "Pudim", "Batata frita"

# Locais:       Hamburgues    Suco          Pizza           Pudim
#               [0] ou [-4]   [1] ou [-3]   [2] ou [-2]     [3] ou [-1]

print(lanche)

# -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-

print("-=-" * 20)
print(len(lanche))

for comida in lanche:
    print(f"Eu vou comer {comida}")
print("-=-" * 20)

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")
print("-=-" * 20)

for i in range(0, len(lanche)):
    print(f"Eu vou comer {lanche[i]} na posição {i}")
print("-=-" * 20)

# -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-

# Organizado em órdem alfabética:
print(lanche)
# Apenas mostra
print(sorted(lanche))
print(lanche[0])

# Transforma a Tupla em lista {() -> []}
lanche = sorted(lanche)
print(lanche[0])
