import numpy as np
import pandas as py
import copy

a = np.zeros(5)
b = np.ones(5)

c = copy.deepcopy(a)
c[3] = 1

print(c)
print(a)