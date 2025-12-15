import pandas as pd

data={
    'NAME':['Abdullah','Azfar','Shaham','Ghulam Qadir'],
    'AGE':[20,19,21,20],
    'GPA':[3.5,3.8,3.2,3.6]
}
df=pd.DataFrame(data)
print(df)
print("Names in the Dataframe:")

print(df['NAME'])

print("ITERATING THROUGH NAMES:")
for name in df['NAME']:
    print(name)
print("above will print names one by one by remoing the indexes")

print("Filtering Dataframe based on condition like gpas and age:")
filter_df=df[df['GPA']>3.5]
print(filter_df)
print("Sorting DF in descending order based on GPA:")
sorted_df=df.sort_values(by='GPA',ascending=False)
print(sorted_df)

print("Adding new column to DF:")
df['GRADES']=['A','A+','B+','A']
print(df)

print("DROPPING COLUMNS:")
df_no_name = df.drop('AGE',axis=1)  # axis=1 means column
print("Without AGE column:")
print(df_no_name)

print("Descriptive statistics of the DataFrame:")
print(df.describe())
print(df['GPA'].describe())
