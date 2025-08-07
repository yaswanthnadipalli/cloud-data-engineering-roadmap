import pandas as pd


df=pd.read_csv('Employee.csv')
#Applying multiple aggregations at once gives department average salary and maximum salary in each department
print(df.groupby('department')['monthly_salary'].agg(['mean', 'max']))

# Using lamba function to determine salary level
df['salary_level']=df['monthly_salary'].apply(lambda x:'High' if x>60000 else 'Low')
print(df)

# Aggregating with three attributes
agg_res=df.groupby('department').agg({
    'monthly_salary':['mean','max'],
    'age':['mean']
})
print(agg_res)