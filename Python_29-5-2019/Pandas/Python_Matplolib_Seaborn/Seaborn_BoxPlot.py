import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

gapminder_df=pd.read_csv('gapminder-FiveYearData.csv')
lifeext_data=gapminder_df['lifeExp']
continent_data=gapminder_df['continent']
sbn.boxplot(lifeext_data,continent_data,data=gapminder_df)
plt.xlabel("Life Expectancy")
plt.ylabel("Continents")
#plt.legend()
plt.show()