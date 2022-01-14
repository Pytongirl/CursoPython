import matplotlib.pyplot as plt
from randomwalks import Randomwalk

rw = Randomwalk()
rw.fill_walk()

plt.style.use("classic")

fig, ax = plt.subplots()  ##subplots llamado de la clase

points_number = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=points_number, cmap=plt.cm.Blues, edgecolors='none', s=15)

ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

#ax.get_xaxis().set_visible(False)
#ax.get_yaxis().set_visible(False)
plt.show()