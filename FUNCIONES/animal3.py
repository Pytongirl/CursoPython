def describe_animal(tipo_de_animal, nombre_de_animal):
    print(f"Tengo un animal de tipo {tipo_de_animal}")
    print(f"Mi {tipo_de_animal} se llama {nombre_de_animal}")
"""2keyword paramethers"""
def describe_animal_argumentos_keyword(tipo_de_animal = "Perro", nombre_de_animal = "Perry"):
    print(f"Tengo un animal de tipo {tipo_de_animal}")
    print(f"Mi{tipo_de_animal} se llama {nombre_de_animal}")
###describe_animal("Conejo", "Bugs Bunny")

describe_animal_argumentos_keyword()
