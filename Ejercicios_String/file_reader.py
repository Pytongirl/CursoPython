#Leer e imprimir cada linea del archvo haciendo right - stripe a cada linea
#with open("Ejercicos/archivos/pi_million_digits1.txt") as file object:

with open("Ejercicos/archivos/pi_million_digits1.txt") as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string = pi_string + line.strip()

#print(pi_string [:10002])

birthday = input("Ingresa tu fechade nacimiento  formato ddmmaa: ")

if birthday in pi_string:
    print(f"Tu fecha de nacimiento {birthday}, se encuentra en el primer millon de digitos de PI" )
else:
    print(f"Tu fecha de nacimiento {birthday}, no se encuentra en el primer millon de digitos de PI")



