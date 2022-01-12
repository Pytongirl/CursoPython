from matplotlib import pyplot

pyplot.style.use("seaborn")

x_values = list(range(1, 6))   ##En un rang el 1 valor es inclusivo,e ultimo exclusivo
y_values = [x **2 for x in x_values]


fig, ax = pyplot.subplots()

ax.scatter(x_values, y_values, c='red', s=5)  #ax.scatter(2, 4)     #donde S es tamaño del punto(point mark)
                              #para colores rgv se da un valorpara cada letra base hexadecimal de 1 a 245,, 
                 # en este programa  el rango para cada color  va de 0 a 1 (menores cerca de negro, mayores mas luminosos)

ax.set_title("Square Numbers")
ax.set_xlabel("Value")
ax.set_ylabel("Square of value")

ax.tick_params(axis="both")
ax.axis([0, 1100, 0, 1_100_000])   ##Esa lista espera 4 valores valor min x, valor max X, valor min Y , valor max Y

pyplot.show()