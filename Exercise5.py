import pandas as pd

df=pd.read_csv('Employee.csv')

#filling the missing age values with the average of the age

df['age']=df['age'].fillna(df['age'].mean())
print(df)
df=df.to_csv('Employee.csv')

# dropping empty rows by department

df = df.dropna(subset=['department'])
print(df)

# Employees whose salary is greater than 50000
print(df[df['salary']>50000])


# filtering employees whose age is less than 30 
print(df[df['age']<30])



# adding new column tax to the dataset
df['tax']=df['salary']*0.1
print(df)
df=df.to_csv('Employee.csv')


# remaning the column name from salary to monthly salary
df.rename(columns={'salary':'monthly_salary'},inplace=True)
df.to_csv('Employee.csv')

# Group by department and calculate average salary
grouped = df.groupby('department')['monthly_salary'].mean()
print(grouped)

# Showing  total tax by department.
group=df.groupby('department')['tax'].sum()
print(group)


# Sort employees by age in descending order

sorted_df = df.sort_values(by='age', ascending=False)
print(sorted_df)    

# Count number of employees in each department
df = pd.read_csv('Employee.csv')
dept_count = df['department'].value_counts()
print(dept_count)
