import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

tips_df=pd.read_csv('tips.csv')
total_bill_data=tips_df['total_bill']
size_data=tips_df['size']
sbn.swarmplot(total_bill_data,size_data,data=tips_df)
plt.xlabel('Total Billing')
plt.ylabel("Size")
plt.title("Total Bill Against Size")
plt.show()