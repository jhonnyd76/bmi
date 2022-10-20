import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 5, 0.1])
for i in x:
    y = np.array([4, 7, 0.5])
    print(i)
plt.plot(x, y)
plt.show()
