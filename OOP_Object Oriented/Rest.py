class Restaurante:

    def __init__(self, nombre_de_rest, tipo_de_cocina):
        self.nombre = nombre_de_rest
        self.cocina = tipo_de_cocina
        self.open = True

    def describe_restaurante(self):
        return f"El restaurante se llama:\n{self.nombre}\nY sirven comida tipo:\n{self.cocina}"

    def open_restaurant(self):
        if self.open == True:
            return "El restaurante esta abierto"
        else:
            return "El restaurante esta cerrado"

name = input("Ingresa el nombre del restaurante: \n")
kitchen = input("Ingresa el tipo de cocina:\n")

datos = Restaurante(name,kitchen)
print(datos.describe_restaurante())
print(datos.open_restaurant())