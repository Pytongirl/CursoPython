import sys
#Esta librerialimpia antes de  iniciar el programa
from os import system
system("cls")

#Iniciamosconformando la lista, con la funciónn append agregamos un elemento al final ->->
#en este caso seria el primero porque esta vacio
nom = []
v = input("Ingresa el nombre a registrar:\n")
nom.append(v)

#Se declara la variable para el uso de while, con esto te permitira ingresar los nombres deseados antes de remplazarlos
f = input("Desea agregar más nombres? Si = 1, No = 0\n")
f = int(f)

#Creamos el ciclo while para ingresar tantos nombres deseemo
while f != 0 :
    v = input("Ingresa el nombre a registrar:\n")
    nom.append(v)
    f = input("Desea agregar mรกs nombres? Si = 1, No = 0\n")
    f = int(f)

#Declaracion con  "for", con esta indicación recorera la lista e imprimira uno por uno hasta el final
for n in nom :
    print(n)