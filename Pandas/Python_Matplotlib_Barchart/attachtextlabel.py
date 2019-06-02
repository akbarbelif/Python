import matplotlib.pyplot as plt


def autolabel(text_label):
    for labels in text_label:
        height = labels.get_height()
        ax.text(labels.get_x()+labels.get_width()/2., 1.05*height, '%f' % float(height),
                ha='center', va='bottom')


lan = ["Java", "Python", "PHP", "JavaScript", "C#"]
popularity = [22.2, 17.6, 8.8, 8, 7.7]
fig, ax = plt.subplots()
lan_enum = [i for i, _ in enumerate(lan)]
txtlabel = ax.bar(lan_enum, popularity, color='Green')
plt.xlabel("Language")
plt.ylabel("Popularity")
plt.title("Poplar lanaguge on 2019\n")
plt.xticks(lan_enum, lan)
plt.minorticks_on
plt.grid(which="minor", linestyle=":", linewidth="0.5", color="red")
plt.grid(which="major", linestyle="-", linewidth="0.5", color="blue")

autolabel(txtlabel)
plt.show()
