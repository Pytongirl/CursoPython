from cgitb import html
from fileinput import filename
from matplotlib.pyplot import bar, title
from mydice import Dice
from plotly.graph_objs import bar, Layout
from plotly import offline

dice = Dice()   #Aqui se da la instancia  y nombre de la clase

result =[dice.roll() for _ in range(10)]

frequencies = []
for value in range(dice.num_sides): #Iterando 6 veces
    frequency = result.count(value + 1)
    frequencies.append(frequency)

#print(frequencies)
x_values = list(range(1, dice.num_sides +1))
data = [bar(x=x_values, y=frequencies)]

x_axis_config = {'title':'Result'}
y_axis_config = {'title': 'Frequency of result'}

layout =Layout(title='Result of rolling one dice 100 times', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': layout}, filename='dicefreqencies.html')    ##Offline necesita 
# los diccionarios y los parametros de datos, lay out y filename


   #grafica que funcinara offline- En caso de no necesitar raficas No en sitio de Internet