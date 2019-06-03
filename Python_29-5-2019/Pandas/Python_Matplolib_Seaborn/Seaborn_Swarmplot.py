import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

tips_df=pd.read_csv('tips.csv')
total_bill_data=tips_df['total_bill']
days_data=tips_df['day']
sbn.swarmplot(total_bill_data,days_data,data=tips_df)
plt.xlabel('Total Billing')
plt.ylabel("Days")
plt.title("Total Bill Against Days")
plt.show()