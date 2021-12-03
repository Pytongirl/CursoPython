def add2(x, y):
    print(x + y)

result = add2(8, 8)
print(result)
pass
    ##print(add(8, 5))***Retorna  valor None

"""List comprehension"""

def double(x):
    return x = 2


sequence =[1, 3, 5, 9]
mi_list=[]

# for numero in sequence:
#     mi_list.append(numero)
# print(mi_list)
#    ## doble= double(numero)

doubled = [double(numero) for numero in sequence]    ##Esto es declarar lista []
print(doubled)
###Doubled =[numero *2 for numero in sequence]
print(doubled)

##print numero = 2