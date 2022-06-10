a = (1, 2, 3, 4)
b = (3, 4, 5, 6)
c = a + b
d = b + a
print(c)
print(d)

# -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-

print("O número 3 aparece quantas vezes?")
print(c.count(3))

print("O número 9 aparece quantas vezes?")
print(c.count(9))

print("Em que posição está o 2?")
print(c.index(2))
print(d.index(2))

# -=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-

# É possível apagar tuplas:
del c, d
