import sys
usuarios=("Andrea", "Juan", "Matias", "Jorge", "Ismael", "admin")
for users in usuarios:
    if users != "admin":
        print (f"Hola {users}, bienvenido")
    else:
        print( "Hola admin, Quieres visualizar el reporte de uso?")