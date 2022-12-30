import pandas as pd
import numpy as np
import copy

def efd(df):
    # create n lists of tupes (start time, duration)
    processing_times = df['processing_times']
    release_dates = df['release_dates']
    #print(release_dates)
    deadlines = df['deadlines']
    schedule = np.zeros(shape=(len(processing_times),deadlines.max()))

    deadline_moved = deadlines.max() + 1

    #for i in range(len(processing_times)):
    #    for j in range(release_dates[i]-1):
    #        schedule[i,j] = 0

    t = release_dates.min()

    while (t < deadlines.max()) and (deadlines.max() < deadline_moved):
        bool_release_dates_greater_t = release_dates >= t 
        available_deadlines = copy.deepcopy(deadlines)
        for i in range(len(release_dates)):
            if not bool_release_dates_greater_t[i]:
                available_deadlines[i] = deadlines.max() + 10
        min_job = available_deadlines.argmin()
        schedule[min_job, t] = 1
        processing_times[min_job] = processing_times[min_job] - 1
        if processing_times[min_job] == 0:
            deadlines[min_job] = deadline_moved
        t = t + 1


    while deadlines.min() > deadlines.max():
        deadlines_greater_zero = deadlines[deadlines > 0]
        min_job = deadlines.argmin()
        

    return schedule