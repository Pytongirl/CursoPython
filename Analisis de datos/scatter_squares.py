from matplotlib import pyplot

pyplot.style.use("seaborn")

x_values = list(range(1, 1000000))   ##En un rang el 1 valor es inclusivo,e ultimo exclusivo
y_values = [x **2 for x in x_values]


fig, ax = pyplot.subplots()

ax.scatter(x_values, y_values, s=5)   #ax.scatter(2, 4)     #donde S es tamaño del punto(point mark)

ax.set_title("Square Numbers")
ax.set_xlabel("Value")
ax.set_ylabel("Square of value")

ax.tick_params(axis="both")
ax.axis([0, 1100, 0, 1_100_000])   ##Esa lista espera 4 valores valor min x, valor max X, valor min Y , valor max Y

pyplot.show()