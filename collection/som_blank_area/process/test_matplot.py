import matplotlib.pyplot as plt
import numpy as np


a = np.arange(0, 8, 1)
b = np.arange(0, 6, 1)
A, B = np.meshgrid(a, b)
print A
print B

plt.pcolor(A, B, A + B)
plt.show()
