import numpy as np
import matplotlib.pyplot as plt


def get_num():
    for i in range(10):
        yield i


generated_array = np.fromiter(get_num(), int)

print(generated_array)

_, (ax1, ax2) = plt.subplots(1, 2)
ax1.pie(generated_array)
ax2.bar(x=generated_array, height=generated_array)

plt.show()
