import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

iris_df=pd.read_csv('iris.csv')
species_data=iris_df['species']
sepal_length_data=iris_df['sepal_length']
sbn.violinplot(species_data,sepal_length_data,label=species_data,data=iris_df)
plt.xlabel("Species")
plt.ylabel("Sepal Lenght")
plt.legend()
plt.show()