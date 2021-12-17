#def menu_disponible():
#    return "Ir por la pelota"

class Restaurante:
    """Una clase basica que representa nombre del rest y tipo de cocina"""

    def __init__(self, nombre_de_rest, tipo_de_cocina):
        """Definiendo e iniciallizando atributos"""
        self.nombre_de_rest = nombre_de_rest
        self.tipo_de_cocina = tipo_de_cocina
        
    def InformaciondelRestaurante(self):    
        return f"El restaurante {self.nombre_de_rest} está abierto, servimos comida tipo:{self.tipo_de_cocina}, \n{self.name1}\n{self.type1} \n{self.name2}\n{self.type2},\n{self.name3}\n{self.type3}"

    def restaurant1(self, name1, type1):
        self.name1 = name1
        self.type1 = type1

    def restaurant2(self, name2, type2):
        self.name2 = name2
        self.type2 = type2

    def restaurant3(self, name3, type3):
        self.name3 = name3
        self.type3 = type3


name = Restaurante("little India", "Comida india")
print(name.InformaciondelRestaurante())
res1 = Restaurante("Little India","Comida China")
print(res1.InformaciondelRestaurante())
res2 = Restaurante("Mi pequeño brocoli","Vegetarian")
print(res2.InformaciondelRestaurante())
res3 = Restaurante("Thai Chop", "Tailandesa")
print(res3.InformaciondelRestaurante())