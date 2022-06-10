dist = int(input("De quantos Km será a viagem? "))
if dist <= 200:
    print("Para uma viagem de {} Km, o preço da passagem será {:.2f} reais".format(dist, dist * 0.5))
else:
    print("Para uma viagem de {} Km, o preço da passagem será {:.2f} reais".format(dist, dist * 0.45))
