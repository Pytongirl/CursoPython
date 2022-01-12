import matplotlib.pyplot as plt

squares=[1, 4, 9, 16, 25]

fig, ax = plt.subplots()

ax.plot(squares, linewidth=3)

ax.set_title("Square numbers", fontsize=14)
ax.set_xlabel("value", fontsize=12)
ax.set_ylabel("Square of value", fontsize=12)

plt.show()
