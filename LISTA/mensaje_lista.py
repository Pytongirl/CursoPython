#indicacion arendida con julio
import sys
from os import system

#limpia cada vez que iniciamos el programa
system("cls")

nom = []
v = input("Ingresa el nombre a ingresar:\n")
nom.append(v)

f = input("Desea agregar más nombres? Si = 1, No = 0\n")
f = int(f)

while f != 0 :
    v = input("Ingresa el nombre a ingresar:\n")
    nom.append(v)
    f = input("Desea agregar más nombres? Si = 1, No = 0\n")
    f = int(f)

for n in nom :
    print(f"Hola, ben dia {n}, el horaro de la clase y link siguen siendo los mismos, nos vemos al rato\n")