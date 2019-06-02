import matplotlib.pyplot as plt

x = ["Java", "Python", "PHP", "JavaScript", "C#"]
popularity = [22.2, 17.6, 8.8, 8, 7.7]
bar_color = ['red', 'black', 'green', 'blue', 'yellow', 'cyan']
x_pop = [i for i, _ in enumerate(x)]
# bar(X-axis,y-axis,color)
plt.bar(x_pop, popularity, color=bar_color)
plt.xlabel("Language")
plt.ylabel("Popluarity")
plt.xticks(x_pop, x)
plt.minorticks_on()
plt.title("Poplar lanaguge on 2019\n")
plt.grid(which="major", linestyle="-", linewidth="0.5", color="red")
plt.grid(which="minor", linestyle=":", linewidth="0.5", color="black")
plt.show()
