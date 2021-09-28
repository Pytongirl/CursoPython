#Programa para calcular el area de un cuadrado
# A = L * L
#lado es un string
lado = input ("Ingresa el valor del lado")
lado = int (lado)

#area es lado al cuadrado
area = lado ** 2
print(f"El area de tu cuadrado con l={lado} es: {area}")
print("El area del cuadrado con l=" + str(lado) + " es: " + str(area))


