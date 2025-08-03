

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Country': ['USA', 'UK', 'India', 'Canada']
}
df = pd.DataFrame(data)
print(df)

df=pd.read_csv('people.csv')
print(df)

print(df[df['Age'] > 30])

print(df[['Name','Age']])

df['experience']=df['Age']-21
print(df)

df.to_csv('people.csv')
print(df)