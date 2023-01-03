import numpy as np

today = np.datetime64('today', 'D')
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("Yesterday: ", yesterday)
print("Today: ", today)
print("Tomorrow: ", tomorrow)
