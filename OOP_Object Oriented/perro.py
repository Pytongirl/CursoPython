from typing import overload


class Perro:
    """Una clase basica que representa a un perro"""

    def __init__(self, nombre, edad):
        """Inicializando el nombre y edad del perro"""
        self.nombre = nombre
        self.edad = edad
        """Ahora definimos atribtos yos inicializamos"""

        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.tamaño = tamaño
        self.color = None
        self.numero_de_juegos_restantes = 3

    def ladrar(self):
        print(f"Hola soy {self.nombre} y digo guau")

    def jugar(self):
        if self.numero_de_juegos_restantes > 0:
            juego = dame_un_juego_al_azar()
            print(f"Hola soy un perro de la raza {self.raza}, por tanto cuando juego , me divierto y ahora estoy jugando {juego}")
            self.numero_de_juegos_restantes = self.numero_de_juegos_restantes -1
        else:
            print(f"{self.nombre} tu ya no puedes jugar")

        def saludar_a_otro_perro(self, otro_perro):
            print(f"Hola soy {self.nombre} y estoy saludando a mi amigo{otro_perro.nombre} ")
            print(f"Hola soy {self.nombre} y estoy saludando a mi amigo que tiene {otro_perro.edad} años")    

