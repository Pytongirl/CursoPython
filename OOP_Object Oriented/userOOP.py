class User:
    
    def __init__(self, first_name, last_name, age, address, ):
        self.nombre = first_name
        self.apeido = last_name
        self.edad = age
        self.direccion = address

    def describe_use(self):
        return f"\nNombre: {self.nombre}\nApeido: {self.apeido}\nEdad: {self.edad}\nDomicilio: {self.direccion}"

    def bienvenido(self):
        return f"\nBienvenido {self.nombre}"

name = input("Ingresa tu nombre:\n") 
last_name = input("Ingresa tu apeido:\n")
age = input("Ingresa tu edad:\n")
adress = input("Ingresa tu direcciรณn:\n")

datos = User(name,last_name,age,adress)
print(datos.describe_use())
print(datos.bienvenido())