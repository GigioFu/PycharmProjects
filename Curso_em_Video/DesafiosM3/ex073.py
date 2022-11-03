serie = ('América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Avaí', 'Botafogo', "Bragantino", "Ceará",
         'Corinthians', "Coritiba", "Cuiabá", 'Flamengo', "Fluminense", "Fortaleza", 'Goiás', "Internacional",
         "Juventude", "Palmeiras", "Santos", "São Paulo")
print("Os cinco primeiros times são: {}".format(serie[:6]))
print("Os últimos quatro colocados são: {}".format(serie[-4:]))
print("Os times em órdem alfabética fica: \n{}".format(sorted(serie)))
print("O time do Corinthians está em {}º lugar".format(serie.index("Corinthians") + 1))
