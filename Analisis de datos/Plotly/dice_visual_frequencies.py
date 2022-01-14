from mydice import Dice

dice = Dice()   #Aqui se da la instancia  y nombre de la clase

result =[dice.roll() for _ in range(10)]

frequencies = []
for value in range(1, dice_num_sides + 1): #Iterando 6 veces