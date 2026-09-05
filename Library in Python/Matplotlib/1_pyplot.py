# Types OF Metplotlib:
# 1)pyplot 2)plotting 3)marker 4)line 5)labels 6)Grid 7)subplots 8)scatters 9)Bars
# 10)Histogram 11)piecharts

# 1) pyplot
# pyplot is a module inside a matplotlib library that provide simple function that creating graphs and chart

'''import matplotlib.pyplot as plt  # "plt" is a nickname of "matplotlib.pyplot"'''

#Example 1):-
#Draw a Simple graph
'''
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.plot(x,y) # line graph function

plt.show() # desplay function
'''
# Example 2):-
#Draw a line in a diagram from position (0,0) to position (6,250):
'''
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,6])
ypoints = np.array([0,250])

plt.plot(xpoints,ypoints)
plt.show()
'''

# ploting X and Y points
# plot():
# The plot() function is used to draw points(Markers) in a diagram.
# By default, The plot() function Drows a line from point to point.
# The funtion takes parameters for specifying point in the diagram
# Parameter 1 is an array containing the points on the x-axis.
# Parameter 2 is an array containing the points on the y-axis.

# if We need to plot a line from (1,3) to (8,10),
# We have to pass two arrays [1,8] and [3,10] to the plot function

#Example:-
#Draw a line in a diagram from position (1, 3) to position (8, 10):
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,8])
y = np.array([3,10])

plt.plot(x,y)
plt.show()
'''

# figure(): syntax: plt.figure(figsize=(width,height))
# figsize determines the size of the graph (figure) that Matplotlib creates.
# Create  A new figure.
'''
import matplotlib.pyplot as plt

plt.figure(figsize=(8,7))

x = [1,2,3]
y = [4,5,6]

plt.plot(x,y)
plt.show()
'''

# title(): syntax: plt.title("Students Graph")
# Add a title:
'''
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
plt.plot([1,2,3],[10,20,30])
plt.title("Students Marks")
plt.show()
'''
# xlabel(): syntax: plt.xlabel("X Points Name")
# Add Label X
'''
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,5))

x = np.array([0,10])
y = np.array([0,500])

plt.plot(x,y)
plt.title("Demo Line Graph")
plt.xlabel("X-axis Label")

plt.show()
'''
# ylabel(): syntax: plt.ylabel("Y Points Name")
# add Label Y
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,10])
y = np.array([0,500])

plt.plot(x,y)
plt.title("Demo Line Graph")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")

plt.show()
'''
# legend(): show label of top left inside the graph
# Display The Legend
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,3])
y = np.array([0,3])

plt.plot(x,y,label="Boys")
plt.title("Demo Line Graph")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")

plt.legend()
plt.show()
'''
# grid()
# show grid line
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,5])
y = np.array([0,250])

plt.plot(x,y,label = "Net Profit")
plt.title("Todays Stock")
plt.xlabel("Stock'S")
plt.ylabel("Profit or Loss")

plt.legend()
plt.grid()
plt.show()
'''
# savefig()
# Save the graph as an image
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,"Sun","Mon","Tue","Wed","Thus","Fri","Sat"])
y = np.array([0,100,200,300,400,500,600,700])

plt.plot(x,y,label="Burger")
plt.xlabel("Day's")
plt.ylabel("Profit")
plt.title("Burger King")

plt.legend()
plt.grid()
plt.savefig("demo-graph.png")
plt.show()
'''
# close()
# close the current figure
'''
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,5))

x = np.array([0,7])
y = np.array([0,25])

plt.title("Strowabary")
plt.xlabel("Day's")
plt.ylabel("Day's Profit")
plt.plot(x,y,label = "Strowbary")

plt.legend()
plt.grid()
plt.savefig("Demo-graph-2.png")
plt.close()
plt.show()
'''

# xlim(), ylim()
# Sets the "x-axis" range and Sets the "y-axis" range
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3])
y = np.array([1,2,3])

plt.title("Add x-axis and y-axis Range")
plt.xlabel("x-axis range")
plt.ylabel("y-axis range")

plt.plot(x,y,label="legend")

plt.legend()
plt.grid()
plt.savefig("x_&_y_axis_range.png")
plt.xlim(2,3) # plt.xlim(min-point,max-point)
plt.ylim(1,3) # plt.ylim(min-point,max-point)
#plt.close()
plt.show()
'''
# xticks()
# Customize X-axis tick marks
'''
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(9,5))

x = np.array([0,5])
y = np.array([0,10])

plt.title("Tick Marks on X Axis")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.plot(x,y,label="Demo")
plt.grid()
plt.savefig("Tick_Marks_on_X_axis.png")
plt.xlim(0,5)
plt.ylim(0,10)
plt.xticks([1,2,3,4,5],["Sun","Mon","Tue","Wed","Thu"]) # xticks([tickes],[labels])
plt.show()
'''
# yticks()
# Customize X-axis tick marks
'''
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(9,5))

x = np.array([0,5])
y = np.array([0,10])

plt.title("Tick Marks on Y Axis")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.plot(x,y,label="Demo")
plt.grid()
plt.savefig("Tick_Marks_on_y_axis.png")

plt.xlim(0,4)
plt.ylim(0,8)
plt.xticks([1,2,3,4,5],["Sun","Mon","Tue","Wed","Thu"])
plt.yticks(np.array([0,10,1,2,3,4,5,7,8,9]))
plt.show()
'''

# text()
# Add text in Graph
'''
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(9,5))

x = np.array([0,5])
y = np.array([0,10])

plt.title("Add Text In Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.plot(x,y,label="Demo")
plt.grid()
plt.savefig("Add_text.png")

plt.text(2,3,"Lowe Point",fontsize=12,color="red")
plt.text(3,5,"Mid Point",fontsize=12,color="blue")
plt.text(4,7,"Heigh Point",fontsize=12,color="green")

plt.xlim(0,4)
plt.ylim(0,8)
plt.xticks([1,2,3,4,5],["Sun","Mon","Tue","Wed","Thu"])
plt.yticks(np.array([0,10,1,2,3,4,5,7,8,9]))
plt.show()
'''

# annotate()
# annotate() is used to add text with an arrow pointing to a specific point.
'''
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(9,5))

x = np.array([0,5])
y = np.array([0,10])

plt.title("Add Text In Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.plot(x,y,label="Demo")
plt.grid()
plt.savefig("annotate_text.png")

# Add Text
plt.text(2,3,"Lowe Point",fontsize=12,color="red")
plt.text(3,5,"Mid Point",fontsize=12,color="blue")
plt.text(4,7,"Heigh Point",fontsize=12,color="green")

# Annotate
plt.annotate(
    "Heigst",
    xy=(4,10),
    xytext=(4,9),
    arrowprops=dict(facecolor="green")
    )

plt.xlim(0,4)
plt.ylim(0,8)
plt.xticks([1,2,3,4,5],["Sun","Mon","Tue","Wed","Thu"])
plt.yticks(np.array([0,10,1,2,3,4,5,7,8,9]))
plt.show()
'''
# subplot()
# subplot() divides one figure into multiple sections, allowing you to display multiple graphs in
# the same window.
'''
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(9,5))

plt.subplot(1,3,1)
plt.title("Graph 1")

x = np.array([0,5])
y = np.array([0,10])

plt.plot(x,y)


plt.subplot(1,3,3)
a = np.array([1,2,3])
b = np.array([9,4,1])
plt.title("Graph 2")
plt.plot(a,b)


plt.xlabel("X-axis")
plt.ylabel("Y-axis")


plt.savefig("Subplot.png")
plt.show()
'''

# subplots()
# subplots() creates a figure and one or more Axes objects.
# Unlike subplot(), it returns objects that you can use to control each plot individually
'''
import matplotlib.pyplot as plt

fig , ax = plt.subplots()

ax.plot([1,2,3],[4,3,2])

ax.set_title("Sales")
plt.savefig("subplots().png")

plt.show()

'''

#Plotting Without Line
#To plot only the markers, you can use shortcut string notation parameter 'o',
#which means 'rings'.

#Example
#Draw two points in the diagram, one at position (1, 3) and one in position (8,
'''
import matplotlib.pyplot as plt

import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()
'''
#Multiple Points
#we can plot as many points as you like, just make sure we have the same number
#of points in both axis.

#Example
#Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and
#finally to position (8, 10):
'''
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()
'''

#Default X-Points
#If we do not specify the points in the x-axis,
#they will get the default values 0, 1, 2, 3,
#(etc. depending on the length of the y-points.

#So, if we take the same example as above, and leave out the x-points,
#the diagram will look like this:

#Example
#Plotting without x-points:
'''
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)
plt.show()
'''
# Example
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,4,8])
y = np.array([8,6,3,4])

plt.plot(x,y)

plt.show()
'''
# Use Multiple subplots

import matplotlib.pyplot as plt

fig , ax = plt.subplots(2,2)

ax[0,0].plot([1,2,3],[2,1,3],label="Data1")
ax[0,0].set_title("Graph 1")
ax[0,0].set_xlabel("x-axis")
ax[0,0].set_ylabel("y-axis")
ax[0,0].grid(True)
ax[0,0].legend()

ax[0,1].plot([1,2,3],[3,1,2],label="Data2")
ax[0,1].set_title("Graph 2")
ax[0,1].set_xlabel("x-axis")
ax[0,1].set_ylabel("y-axis")
ax[0,1].grid(True)
ax[0,1].legend()

ax[1,0].plot([1,2,3],[2,3,4],label="Data3")
ax[1,0].set_title("Graph 3")
ax[1,0].set_xlabel("x-axis")
ax[1,0].set_ylabel("y-axis")
ax[1,0].grid(True)
ax[1,0].legend()

ax[1,1].plot([1,2,3],[4,3,2],label="Data4")
ax[1,1].set_title("Graph 4")
ax[1,1].set_xlabel("x-axis")
ax[1,1].set_ylabel("y-axis")
ax[1,1].grid(True)
ax[1,1].legend()

plt.tight_layout()
plt.savefig("Multiple_Subplots.png")
plt.show()


