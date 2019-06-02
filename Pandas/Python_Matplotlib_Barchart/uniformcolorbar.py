# Uniform color-bar
import matplotlib.pyplot as plt

x = ["Java", "Python", "PHP", "JavaScript", "C#"]
popularity = [22.2, 17.6, 8.8, 8, 7.7]
x_pop = [i for i, _ in enumerate(x)]
# bar(X-axis,y-axis,color)
plt.bar(x_pop, popularity, color=(0.4, 0.6, 0.8, 1.0))
plt.xlabel("Language")
plt.ylabel("Popluarity")
plt.xticks(x_pop, x)
plt.minorticks_on()
plt.grid(which="major", linestyle="-", linewidth="0.5", color="Red")
plt.grid(which="minor", linestyle=":", linewidth="0.5", color="green")
plt.show()
