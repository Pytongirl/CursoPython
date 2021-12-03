def dame_un_juego_al_azar():
    return "Ir por la pelota"

class Perro:
    """Una clase basica que representa a un perro"""

    def __init__(self, nombre, edad, raza, tamaño, color):
        """Definiendo e iniciallizando atributos"""
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.tamaño = tamaño
        self.color = None
        self.numero_de_juegos_restantes = 3
        
    def ladrar(self):
    print(f"Hola soy {self.nombre} y digo guau")

    def jugar(self):
    juego = dame_un_juego_al_azar()
    print(f"Hola soy un perro de la raza {self.raza}, por tanto cuando juego , me divierto y ahora estoy jugando {juego}")
            #self.numero_de_juegos_restantes = self.numero_de_juegos_restantes -1
            #print(f"{self.nombre} tu ya no puedes jugar")
    def saludar_a_otro_perro(self, otro_perro):
    print(f"Hola soy {self.nombre} y estoy saludando a mi amigo{otro_perro.nombre} ")
    print(f"Hola soy {self.nombre} y estoy saludando a mi amigo que tiene {otro_perro.edad} años")
    
#Crear una instancia
mi_primer_perro = Perro("Perry", 2, "Schnawzer","blanco")
mi_segundo_perro = Perro("Diablo", 2, "Doberman","negro")
#Print (mi_primer_perro.nombre) 
mi_primer_perro.ladrar()

mi_primer_perro.saludar_a_otro_perro(mi_segundo_perro)