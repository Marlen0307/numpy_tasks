import numpy as np
import matplotlib.pyplot as plt


vector = np.arange(10, 49)
print("Original vector:")
print(vector)
reversed_vector = np.flip(vector)
print("Reversed vector:")
_, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.pie(vector)
ax2.pie(reversed_vector)
ax3.bar(x=vector, height=vector)
ax4.bar(x=vector, height=reversed_vector)

plt.show()
