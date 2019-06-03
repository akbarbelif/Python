import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

tips_df=pd.read_csv("tips.csv")
day_data=tips_df['day']
tips_data=tips_df['tip']
sbn.boxplot(day_data,tips_data,data=tips_df)
plt.xlabel("Days")
plt.ylabel("Tips")
plt.title("Days by Tips")
plt.show()