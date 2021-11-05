#mostrar valores
dict1 = {
    "2": "dos",
    "3": "tres",
    "4": "cuatro",
    "5": "cinco"
}


# print("6. Imprimir soo valores")
# dict_keys = dict1.keys()
# dict_values = dict1.values()
# print (dict_values)
# print(f"{'*' * 20}\n")

####################################################################
###Ahora imprimir clave:valor
print("7. Imprimir clave valor")
for key, value in dict1.items():
    print(key, value)

print(f"{'*' * 20}\n")
######################################################################

##checar si existe una clave valor
print("8. Checando si estan la clave:valor especificos en el diccionario")
print(f"{'*' * 20}\n")


###################################################################
#Insertar clave y valor si no existen

print("9. Insertar clave y valor, si no exste")
dict1.update({"5": "cinco"})
print(dict1)
print(f"{'*' * 20}\n")


 
