import numpy as np
import pandas as pd

np.random.seed(42)

p_max = 40
n = 5

processing_time_nparray = np.random.randint(p_max, size=(n))
processing_time = processing_time_nparray.tolist()
release_dates_nparray = np.random.randint(processing_time_nparray.sum()-processing_time_nparray.max(), size=(n))
release_dates = release_dates_nparray.tolist()
deadlines = []
for i in range(n):
    upper = processing_time_nparray.sum()-processing_time[i]
    lower = release_dates[i] + processing_time[i]
    difference = upper - lower
    deadline = np.random.randint(lower ,upper + difference + processing_time[i])
    deadlines.append(deadline)


dict = {'processing_times': processing_time, 'release_dates': release_dates, 'deadlines': deadlines}
df = pd.DataFrame(data=dict)



def return_example():
    return df


