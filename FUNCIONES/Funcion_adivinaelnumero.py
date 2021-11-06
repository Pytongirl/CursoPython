
import random
def adivinaelnumero ():
    myrandom = random.randint(1,100)
    print("Intenta adivinar el numero secreto")
    comparable = int(input("Ingresa un numero del 1 al 100:\n"))

    if comparable == myrandom:
        print("Felicidades_ganaste")
    else: 
        print("fallaste_sigue intentando")

    while comparable != myrandom:
        myrandom = random.randint(1,100)
        print("Intenta adivinar el numero secreto")
        comparable = int(input("Ingresa un numero del 1 al 100:\n"))

        if comparable == myrandom:
            print("Felicidades_ganaste")
        else: 
            print("fallaste_sigue intentando")
adivinaelnumero ()