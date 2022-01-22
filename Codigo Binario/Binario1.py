numero = input ("Ingresa el numero decimal deseado")
numero= int(numero)
binario=bin(numero).lstrip("0b")
print(f"numero decimal={numero} en codigo binario: {binario}")
