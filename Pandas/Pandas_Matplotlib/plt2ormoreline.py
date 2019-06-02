import matplotlib.pyplot as plt
# line 2 points
x1 = [10, 20, 30]
y1 = [20, 40, 10]
x2 = [10, 20, 30]
y2 = [40, 10, 30]
plt.plot(x1, y1, label="line 1")
plt.plot(x2, y2, label="line 2")
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Two or more lines on same plot with suitable legends ')
# show a legend on the plot
plt.legend()
plt.show()
