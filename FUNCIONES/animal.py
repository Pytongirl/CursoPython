def describe_animal(tipo_de_animal, nombre_de_animal):
    print(f"Tengo un animal de tipo {tipo_de_animal}")
    print(f"Mi {tipo_de_animal} se llama {nombre_de_animal}")

# describe_animal("perro", "perry")
# describe_animal ("perro", "firulais")


mascotas = [("Gato", "Garfield"), ("perro", "perry"), ("Conejo", "Bugs Bunny")]
for mascota_nombre in mascotas:
        describe_animal(mascota_nombre[0], mascota_nombre[1])
        
