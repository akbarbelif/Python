import matplotlib.pyplot as plt
x = ['Java', 'C#', 'Python', 'Javascript', 'C++']
popularity = [22.2, 17.3, 8.8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
# bar(X-axis,y-axis,color)
plt.bar(x_pos, popularity, color='Blue')
plt.xlabel("Language")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n")
plt.xticks(x_pos,  x)
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='Red')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='green')
plt.show()
