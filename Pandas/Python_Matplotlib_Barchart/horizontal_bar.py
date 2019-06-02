import matplotlib.pyplot as plt

y = ["Java", "Python", "PHP", "JavaScript", "C#"]
popularity = [22.2, 17.6, 8.8, 8, 7.7]
y_pos = [i for i, _ in enumerate(y)]
# Horizontal Bar barh
# bar(X-axis,y-axis,color)
plt.barh(y_pos, popularity, color='Red')
plt.title("PopularitY of Programming Language\n")
plt.xlabel("Language")
plt.ylabel("Popularity")
# horizontal ticks
plt.yticks(y_pos, y)
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='blue')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='green')
plt.show()
