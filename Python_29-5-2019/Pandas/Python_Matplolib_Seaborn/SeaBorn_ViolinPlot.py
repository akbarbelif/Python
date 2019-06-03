import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

tips_df=pd.read_csv("tips.csv")
sex_data=tips_df["sex"]
totalbill_df=tips_df["total_bill"]
sbn.violinplot(sex_data,totalbill_df,data=tips_df)
plt.show()
