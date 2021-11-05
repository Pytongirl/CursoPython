##acceder valor por su clave
dict1 = {
    "2": "dos",
    "3": "tres",
    "4": "cuatro",
    "5": "cinco"
}

print("5. Acceder a valor por su clave")
value2 = dict1["2"]

print (value2)     #Ejemplo1

print(dict1.get("9", "nada por aqui"))    #ejemplo2

#print(f"{'*' * 20}\n")