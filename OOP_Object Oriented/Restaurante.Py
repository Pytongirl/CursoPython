#def menu_disponible():
#    return "Ir por la pelota"

class Restaurante:
    """Una clase basica que representa nombre del rest y tipo de cocina"""

    def __init__(self, nombre_de_rest, tipo_de_cocina):
        """Definiendo e iniciallizando atributos"""
        self.nombre_de_rest = nombre_de_rest
        self.tipo_de_cocina = tipo_de_cocina
        
    def InformaciondelRestaurante(self):    
        return print(f"El restaurante {self.nombre_de_rest} está abierto, servimos comida tipo:{self.tipo_de_cocina} ")

name = Restaurante("little India", "Comida india")
print(name.InformaciondelRestaurante())

    