#Invocacion de funciones co valor de retorno de otras funcions
def suma(a, b):
    return a + b

def factorial(x):
    if (x==1): return 1
    return x * factorial(x - 1)

# print(factorial(4))   

x, y, z, = 6, 4, 3
print(suma(x, suma(x, suma(z, factorial(y)))))