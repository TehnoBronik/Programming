import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-1000000000, 1000000000, 10000)
y = x**2
plt.plot(x, y);
plt.grid()
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title('Парабола', fontsize=15);
plt.show()
