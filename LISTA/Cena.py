#indicacion aprendida con Julio
import sys

#limpia cada vez que iniciamos el programa
from os import system
system("cls")

#Declaramos nuestro array
invitation = ["Maria", "Angela", "Leo"]

#4.1 El mensaje de invitacion grupal, recorre el array completo e imprime 1 a 1
for i in invitation:
    print(f"Hola {i} estas invitado a mi cena, no faltes")

#L4.2 se escogió la posicion 2  para ser remplazado (el de el medio)
print(f"\nHola, soy {invitation[1]} no podre asistir a tu cena, una disculpa\n")
#Pop es para elimiar u obtener
#insert nos sirve para agregar a otros en la posicion que deseemos
invitation.pop(1)
invitation.insert(1,"Ariel")

#Igual nuevo mensaje
print(f"\nHola {invitation[1]} estas invitado a mi cena, no faltes\n")

#Agregamos a los nuevos en las posiciones que queriamos
##Pepe es posicion Inicial
print("\nEncontre una mesa mas chida, voy a invitar a 3 amigos mas\n")
invitation.insert(0,"Pepe")
invitation.insert(2,"Juan")
#len nos da la ultima posicion del array, con esto agregamos a  alguien mas
n = len(invitation)
invitation.insert(n,"Esteban")

#Mensaje para todos_grupal
for i in invitation:
    print(f"Hola {i} estas invitado a mi cena, no faltes")


#4.3 Usa un ciclo para eliminar uno por uno y enviar el mensaje
for i in invitation[2] :
    #Escribo el mensaje y al mismo tiempo los voy eliminando
    print(f"\nLo siento {invitation.pop(0)}, la mesa que reserve ya no está disponible, solo me podre quedar con dos invitados")

#4.4 El mensaje final con los ultimos 2 invitados
for i in invitation :
    print(f"\nHola {i} sigues invitado a la cena, espero tu asistencia")

print("Como les parecio la cena al final?")