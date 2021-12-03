
def x():
    y()
    print("Estoy en la funcion x")
    

def y():
    z() 
    print("Estoy en la funcion y")
    

def z():
    print("Estoy en la funcion z")
    #return none

x()