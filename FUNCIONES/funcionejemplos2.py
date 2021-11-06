# from FUNCIONES.Funcionejemplos import hello_world
# from Funcionejemplos import (sumar_numeros)
# pass

name = ["lupita", "paco"]
NAMES = ["juan", "marc", "joe"]
##print(hello_world(name))
def hello_world(name):
    ####title convierte o llama al string
    return f"Hello {name.title()}"

def my_function():
    name=NAMES[2]
    
    print(hello_world(name))

# def dar_nombre(name):   #name es un parametro, valor pasado a una funcion en su declaracion.
#     return name
my_function ()










