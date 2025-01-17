import pandas as pd

df=pd.read_csv("C:\\Users\\vani1\\Desktop\\6655_COE\\Uber.csv",nrows=100)
print(df)

data=pd.read_excel("C:\\Users\\vani1\\Desktop\\6655_COE\\Uber.xlsx",nrows=100)
print(data)

print("first 5 rows and last 2 columns")
print(df.iloc[0:5,-2:])

print("50 to 100 rows")
print(df.iloc[50:100])

print("all rows from first 3 columns")
print(df.iloc[:,0:3])

print(df.columns)
print(df.dtypes)

df['START_DATE*'] = pd.to_datetime(df['START_DATE*'])
df['END_DATE*'] = pd.to_datetime(df['END_DATE*'])

print(df.dtypes)

