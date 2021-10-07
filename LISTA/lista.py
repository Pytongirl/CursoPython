import sys
lista=[] 
mi_tuple=()



#doc string
"""saber el tamaño de una lista o un tuple"""
print(type(lista))
print(type(mi_tuple))

print(f"tamaño en memoria de la lista:{sys.getsizeof(lista)}")
print(f"tamaño en memoria de la lista:{sys.getsizeof(mi_tuple)}")


"""Acceder a losvalores de una lista y un tuple"""
lista2 =[1, 2 ,3 , 4, 5]
tuple2 =(6, 7, 8)   #se puede poner comentarios en la misma linea con al menos 2 espacios
                   #el indice en python inicia en el numero 0

print(lista2[-2])  #{}                 
print(tuple2[-2])  #aqui tengo error de sintaxis no se pk.. no veo bien en el video de julio
