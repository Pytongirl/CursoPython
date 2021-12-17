#Ejercicio 1  con parametros por default


def multiply(x, y=5):
    return f"el producto es:{x * y}"

print(multiply(10))
pass

def multiply(x, y, z=30):
    return f"el producto es:{x * y + z}"

print(multiply(10, 20, 50))
pass

def subtract(o=0, p):
    return o - p

print (subtract(20,20))