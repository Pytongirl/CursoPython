#Retornar un diccionario agregando con claves y valores declarados
print("14.Retornar un diccionario agregando con claves y valores declarados ")
dict1 = {
    "2": "dos",
    "3": "tres",
    "4": "cuatro",
    "5": "cinco"
}
campo = ["key1", "key2"]
valor = ""
dict3 = dict.fromkeys(campo, valor)
print(dict3)

print(f"{'*' * 20}\n")