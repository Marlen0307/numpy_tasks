import numpy as np

structured_arr = np.zeros(10, [('position', [('x', float, 1),
                                             ('y', float, 1)]),
                               ('color', [('r', float, 1),
                                          ('g', float, 1),
                                          ('b', float, 1)])])
print(structured_arr)
