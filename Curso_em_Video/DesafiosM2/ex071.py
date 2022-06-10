t50 = t20 = t10 = t1 = 0
print("-=-" * 20)
print("{}{:^60}{}".format("\033[1;32m", "Caixa eletrônico", "\033[m"))
print("-=-" * 20)
tot = int(input("Qual valor deseja sacar? R$"))
while tot >= 50:
    tot -= 50
    t50 += 1
while tot >= 20:
    tot -= 20
    t20 += 1
while tot >= 10:
    tot -= 10
    t10 += 1
while tot >= 1:
    tot -= 1
    t1 += 1
print("=" * 60)
if t50 > 0:
    print("Um total de {} cédulas de R${}".format(t50, 50))
if t20 > 0:
    print("Um total de {} cédulas de R${}".format(t20, 20))
if t10 > 0:
    print("Um total de {} cédulas de R${}".format(t10, 10))
if t1 > 0:
    print("Um total de {} cédulas de R${}".format(t1, 1))
