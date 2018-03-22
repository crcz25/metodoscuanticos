import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import sys


size = 40
# cols = 2
# low = 0
# high = 20
# step = 1
#
# matrix = np.random.choice([x for x in range(low, high, step)], rows*cols)
# matrix.resize(rows, cols)

# print(matrix)

# plt.plot(matrix, 'ro')
# plt.axis([-10, 50, -10, 50])

# plt.hist(matrix)
# plt.title('Holi')
# plt.subplot().xaxis.set_major_formatter(FormatStrFormatter('%d'))
# plt.show()

# grid = np.random.binomial(1, 0.2, size=(50, 50))
# print(grid)
# plt.plot(grid, 'ro')
# plt.title('Grid')
# plt.show()

data = np.random.random_integers(0, 1, size=(size, size))
print(data)

# create discrete colormap
cmap = colors.ListedColormap(['white', 'black'])
bounds = [0, 1, 9]
norm = colors.BoundaryNorm(bounds, cmap.N)

fig, ax = plt.subplots(1, 1, figsize=(size / 10, size / 10))
ax.imshow(data, cmap=cmap, norm=norm)

print(fig)
print(ax)

# draw gridlines
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=1)
# ax.set_xlabel('holi', size=12)
# ax.set_xticks(np.arange(0, size))
# ax.set_yticks(np.arange(0, size))
plt.xticks([])
plt.yticks([])
plt.show()
