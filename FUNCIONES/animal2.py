##from FUNCIONES.animal import describe_animal


##from FUNCIONES.animal import describe_animal
##from FUNCIONES.animal3 import describe_animal_argumentos_keyword
def describe_animal(tipo_de_animal, nombre_de_animal):
    print(f"Tengo un animal de tipo {tipo_de_animal}")
    print(f"Mi {tipo_de_animal} se llama {nombre_de_animal}")

mascotas =[("Gato", "Garfield"), ("Conejo", "Bugs Bunny"), ("Perro", "Firulais")]
# for mascota_nombre in mascotas:
#     describe_animal(mascota_nombre[0], mascota_nombre[1])

#     describe_animal("Conejo", "Bugs Bunny")
describe_animal("Conejo", "Bugs Bunny")
describe_animal("Perro", "Firulais")

