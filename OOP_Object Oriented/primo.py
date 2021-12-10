import re
"""primos"""

def es_divisor(var1,var2):
    es_primo = var1/var2
    try:
        int(es_primo)
        calando=True
    except:
        calando=False
    print(calando)
    print(es_primo)

#def 

pri = int(input("Ingresa tu primera variable: \n"))

sec = int(input("Ingresa tu segunda variable: \n"))

es_divisor(pri,sec)


def genera_primos():
    res = []
    for x in range(2, 1001):
        es_primo = True
        for divisor in range(2, x):
            if x % divisor == 0:
                es_primo = False
    
        if es_primo:
            res.append(x)

    print(res)