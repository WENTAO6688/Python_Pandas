'''Author: Wentao Ma'''

import pandas as pd
import numpy as np

# pandas is an open source python library providing high-performance and easy-to-use data structures and data analysis tools.

'''1. let's create the header for each component.'''
df_1 = pd.DataFrame([
    ['Martin', 25, 180, 130],
    ['Candice', 24, 172, 110],
    ['Howell', 28, 178, 160],
    ['Oliver', 26, 173, 120],
    ['Darren', 25, 180, 150],
    ['Barry', 26, 180, 140],
    ['Zhang', 25, 175, 135],
    ['Song', 28, 170, 100],
    ['Mike', 26, 180, 150],
    ['Lynn', 25, 185, 140],
    ['Eve', 26, 172, 120],
    ['Will', 26, 175, 120],
    ['Angela', 27, 173, 100],
    ['Tang', 24, 172, 110],
    ['James', 29, 170, 150]],
    index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14],
    columns = ['name','age','height','weight'])

print(df_1)

'''2. let's read the first 5 rows and last 5 rows.'''
# head() will print the first 5 rows.
print(df_1.head())
# tail() will print the last 5 rows.
print(df_1.tail())
print(df_1.head(8))
print(df_1.tail(3))

'''3. let us get the data types, index, column and values'''
print(df_1.dtypes)
print(df_1.index)
print(df_1.columns)
print(df_1.values)

'''4. statistical data'''
print(df_1.describe())

'''5.sort syntax'''
# sort by age
print(df_1.sort_values('age', ascending=False))

# sort by height
print(df_1.sort_values('height', ascending = False))

'''6. slicing syntax'''
age = df_1.age
print(age)
height = df_1.height
print(height)

height_weight = df_1[['height','weight']]
print(height_weight)

height_weight2 = df_1.loc[:, ['height', 'weight']]
print(height_weight2)

# get the specific row
num_9 = df_1.loc[9, ['height']]
print(num_9)

'''7. filtering '''
# filter the people whose age is greater than 25
age_greater_25 = df_1[df_1.age > 25]
print(age_greater_25)

# filter the people whose height equals to 178
height_equalto_178 = df_1[df_1.height == 178]
print(height_equalto_178)

# filter the people whose height equals to 175, 176, 177, 178
height_from_175_178 = df_1[df_1.height.isin([175,176,177,178])]
print(height_from_175_178)

'''8. Assign the value'''
df_1.loc[1,'age'] = 23
print(df_1.head())

df_1.loc[3,['age']] = np.nan
print(df_1.loc[3:4])

'''9. rename the column name'''
df_1.rename(columns={'age':'AGE'}, inplace=True)
print(df_1)

df_1.columns = ['NAME','AGE','HEIGHT','WEIGHT']
print(df_1)

