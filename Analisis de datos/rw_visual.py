import matplotlib.pyplot as plt
from randomwalks import Randomwalk

rw = Randomwalk()
rw.fill_walk()

plt.style.use("classic")

fig, ax = plt.subplots()  ##subplots llamado de la clase

ax.scatter(rw.x_values, rw.y_values, s=15)

plt.show()
