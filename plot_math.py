import matplotlib.pyplot as plt
import math
import numpy as np

LEFT = -1.5
RIGHT = 2.5
DOT = 100

x1 = np.linspace(LEFT, RIGHT, DOT)
y1 = 3*x1**2 - 4*x1 - 1
plt.plot(x1, y1)

x2 = np.linspace(LEFT, RIGHT, DOT)
y2 = x2**3 - 2*x2**2 - x2 + 2
plt.plot(x2, y2)

plt.grid()
plt.show()
