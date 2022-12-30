# Importing the matplotlib.pyplot
import matplotlib.pyplot as plt

# Declaring a figure "gnt"
fig, gnt = plt.subplots()

# Setting Y-axis limits
gnt.set_ylim(0, 1)

# Setting X-axis limits
gnt.set_xlim(0, 160)

# Setting labels for x-axis and y-axis
gnt.set_xlabel('time step')
gnt.set_ylabel('Machine')


# Setting ticks on y-axis
gnt.set_yticks([0])
# Labelling tickes of y-axis
gnt.set_yticklabels(['Machine 1'])

# Setting ticks on x-axis
x_ticks_list = list(range(0,161,10))
gnt.set_xticks(x_ticks_list)

# Setting graph attribute
gnt.grid(True)


# Declaring multiple bars in at same level and same width
gnt.broken_barh([(50, 65), (130, 10)], (0, 1),facecolors ='tab:blue')
gnt.broken_barh([(120, 10), (140, 10)], (0, 1),facecolors ='tab:red')
gnt.broken_barh([(0, 40), (70, 50)], (0, 1),facecolors ='tab:orange')

plt.savefig("gantt1.png")