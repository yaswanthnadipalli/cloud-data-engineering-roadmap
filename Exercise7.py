import pandas as pd
import pandasql as ps

df=pd.read_csv('Modified_Employee_Exercise6.csv')


# grouping the department by average tax and salary
print(df.groupby('department')[['salary', 'tax']].mean())

# grouping the department by the age minimum and maximum
print(df.groupby('department')['age'].agg(['min', 'max']))

# print(df.groupby('department')['age'].min())
# print(df.groupby('department')['age'].max())


# Group by department and calculate average salary
grouped = df.groupby('department')['salary'].mean()

# Filter departments with avg salary > 60000
filtered = grouped[grouped > 60000]

#Count departments
print("Departments with average salary > 60000:", len(filtered))




# Merging Concept 
emp_df = pd.read_csv('Modified_Employee_Exercise6.csv')
dept_df = pd.read_csv('departments.csv')

# Merge on department its like joins in sql
merged_df = pd.merge(emp_df, dept_df, on='department', how='inner')
print("Merged DataFrame:\n", merged_df)

# Group by location and calculate average monthly salary
avg_salary_by_location = merged_df.groupby('location')['salary'].mean()
print("\nAverage Monthly Salary by Location:\n", avg_salary_by_location)

# pandasql concept 
# Executing Queries Using pandasql library on dataframes 
# Selecting name,age,tax from the dataframe who age is greater than 30 and tax greater than 6000
query1 = "SELECT name, age, tax FROM df WHERE age > 30 AND tax > 6000"
result1 = ps.sqldf(query1, locals())
print("Employees with age > 30 and tax > 6000:\n", result1)

#Get department-wise average monthly salary using SQL

query2 = "SELECT department, AVG(salary) AS avg_salary FROM df GROUP BY department"
result2 = ps.sqldf(query2, locals())
print("\nDepartment-wise Average Monthly Salary:\n", result2)
