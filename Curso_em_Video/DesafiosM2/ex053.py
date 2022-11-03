f = input("Digite uma palavra/frase: ").strip().lower().replace(" ", "")

# for i in range(len(f) - 1, -1, -1):
#     inverso += f[i]

# A forma mais fácil sem utilizar o (for) é:
inverso = f[::-1]

if f == inverso:
    print("\033[1;32mA palavra/frase é um palíndromo\033[m")
else:
    print("\033[1;31mA palavra/frase NÂO é um palíndromo\033[m")
