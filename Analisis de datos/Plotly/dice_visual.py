from mydice import Dice

dice = Dice()   #Aqui se da la instancia  y nombre de la clase

result =[]

for _ in range(100):
    result.append(dice.roll())

print(result)
