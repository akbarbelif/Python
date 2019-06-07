# Pandas Class Library Installation
# sudo apt-get install python3-pandas
# Addition,Multiplication,Division,Substraction of two series number

import pandas as pd
import numpy as np

# a=pd.Series([2, 4, 6, 8, 10])
# print(a)
# b=pd.Series([1, 3, 5, 7, 9])
# print(b)
# c=a+b
# print("Addition of two Series:\n",c)
# c=a*b
# print("Multiplication of two Series:\n",c)
# c=a-b
# print("Substraction of two Series:\n",c)
# c=a/b
# print("Division of two Series:\n",c)

exam_detail= {
'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df=pd.DataFrame(exam_detail,index=labels)
print(df)
print("First 3 Row:\n",df[:3])
print("Specific Row and column :\n",df.iloc[[1,2,3],[1,3]])
print("Name Score:\n")
print(df[['name','score']])

print("Number of attempt is greater then 2:\n")
print(df.ix[[1,3,5],['name','score','attempts']])
print('Score is NUll:\n',df[['score']].isnull())
print('Score is between 15 and 20 \n:',df[df['score'].between(15,20)])

print('Number of Attempts is less then 2:\n:',df.ix[[0,6,7,8],['name','score','attempts']])



