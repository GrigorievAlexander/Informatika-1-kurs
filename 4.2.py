import matplotlib.pyplot as plt
import numpy as np

pos = 0
scale = 10

values1 = np.random.normal(pos, 1000, 10000)
values2 = np.random.normal(pos, 1000, 100000)

plt.hist(values2, 100, color = 'green')
plt.hist(values1, 10, alpha = 0.7, color='lightgreen')

plt.show()


