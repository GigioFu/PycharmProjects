print("A soma de todos os ímpares multiplos de 3 entre 1 e 500 são: ")
sm = 0
for i in range(1, 500, 2):
    if i % 3 == 0:
        sm += i
print(sm)
