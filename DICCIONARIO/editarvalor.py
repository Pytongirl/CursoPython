##Editar valor
dict1 = {
    "2": "dos",
    "3": "tres",
    "4": "cuatro",
    "5": "cinco"
}

# print("10. Editar Valor")
# dict1.update({"2": "doss"})
# print(dict1)

# print (f"{'*' * 20}\n")

# ###Insertar clave y valor si no existe, si existe lo retorna, no lo edita
# print("11. Insertar clave y valor si o existe, si existe  lo retorna, no lo edita")
# dict1.setdefault("7", "siete")
# dict1.setdefault("7", "manzana")
# print(dict1)

# print(f"{'*' * 20}\n")


###################################
##Insertar clave y valor si no existe, si existe lo retorna, no lo edita
print("12. Insertar clave y valor si o existe, si existe  lo retorna, no lo edita")
dict1 = {**dict1, **{"6": "seis"}}
print(dict1)

print(f"{'*' * 20}\n")