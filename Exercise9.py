import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# adding a total column to the dataset
df = pd.read_csv("sales_data.csv")
df['Total']=df['Quantity']*df['Price']

#Grouping the total by region
print(df.groupby('Region')['Total'].sum())

# Average sales by product
print(df.groupby('Product')['Total'].mean())

#Total units sold per day
print(df.groupby('Date')['Quantity'].sum())

#bar chart of total sales per region
df.groupby('Region')['Total'].sum().plot(kind='bar', title='Total Sales per Region')
plt.ylabel('Total Sales')
plt.show()

# line plot of total sales per day
df.groupby('Date')['Total'].sum().plot(kind='line', marker='o', title='Sales per Day')
plt.xticks(rotation=45)
plt.ylabel('Sales')
plt.show()

# Pie chart of total quantity sold per product
df.groupby('Product')['Quantity'].sum().plot(kind='pie', autopct='%1.1f%%', title='Quantity per Product')
plt.ylabel('')
plt.show()

# Seaborn Boxplot
sns.boxplot(x='Product', y='Total', data=df)
plt.title('Sales Distribution by Product')
plt.show()

# The region with the highest average sale per order.

avg_sale = df.groupby('Region')['Total'].mean()
value= avg_sale.max()
print("Highest average sale per order:", avg_sale.idxmax(),value)




