#Programa para calcular el area de un triangulo
# A = b * h   Use denominacion  base * altura  (base y altura son mis variables)
#variable base inicia como string y luego como entero
base = input ("Ingresa el valor de la base")
base= str (base)
base = int (base)

#variable altura inicia como string y luego como entero
altura = input ("Ingresa el valor de la altura")
altura= str (altura)
altura = int (altura)

#area base * altura
area = base * altura
print(f"El area de tu triangulo con base = {base} y altura = {altura} es : {area}")
#print("El area del triangulo con base=" + str(base) + "y altura = " str(altura) " es: " + str(area))