import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

titanic_df=pd.read_csv('titanic.csv')
sex_data=titanic_df["sex"]
survived_data=titanic_df["survived"]
sb.barplot(sex_data,survived_data,data=titanic_df)
plt.show()

