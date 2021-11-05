palabra = input("Ingresa tu frase\n")
#Con las dos comillas identificamos que es string para usar método join
word = "".join(reversed(palabra))

if word == palabra:
    print("La palabra es un palindromo")
else:
    print("La palabra no es un palindromo")