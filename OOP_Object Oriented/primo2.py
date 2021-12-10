"""primos"""

def es_divisor(var1):
    for n in range(2, var1):
        if var1 % n == 0:
            print("No es numero primo")
            return False
    print("Es primo")
    return True

def primo():
    pri = int(input("Ingresa tu variable: \n"))
    return pri

paso = primo()
es_divisor(paso)
#sec = int(input("Ingresa tu segunda variable: \n"))

#es_divisor(pri,sec)


# def genera_primos():
#     res = []
#     for x in range(2, 1001):
#         es_primo = True
#         for divisor in range(2, x):
#             if x % divisor == 0:
#                 es_primo = False
    
#         if es_primo:
#             res.append(x)

#     print(res)