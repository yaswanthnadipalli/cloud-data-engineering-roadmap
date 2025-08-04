import pandas as pd

df=pd.read_csv('Employee_Exercise6.csv')

# Strips the extra white spaces in the name data 
df['name'] = df['name'].str.strip().str.title()

#makes capital all departments
df['department'] = df['department'].str.strip().str.upper()

# droping the duplicate rows

df=df.drop_duplicates()


# droping the rows where age or salary is missing 
df['age'] = df['age'].replace(r'^\s*$', pd.NA, regex=True)
df=df.dropna(subset=['age','salary'])

# converting the data age and salary to integers

df['salary']=df['salary'].astype(int)
df['age'] = df['age'].astype(int)

# normalizing the salary column using min-max normalization

df['normalized_salary'] = (df['salary'] - df['salary'].min()) / (df['salary'].max() - df['salary'].min())

# adding a column level  junior if age is less than 30 else senior

df['level']=df['age'].apply(lambda x: 'Junior' if x<30 else 'senior')

# saving all the modifications to modified_Employee_Exercise6.csv
df.to_csv("Modified_Employee_Exercise6.csv", index=False)