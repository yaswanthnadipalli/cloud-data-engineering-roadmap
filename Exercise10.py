import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("sales_data.csv")

# Converting the date string to datetime format
df['Date']=pd.to_datetime(df['Date'])
print(df)
df.to_csv('sales_data.csv')

#total sales per region

print(df.groupby('Region')['Total'].sum())

# Average price per product

print(df.groupby('Product')['Price'].mean())

#Total revenue per day

print(df.groupby('Date')['Total'].sum())

#only rows where quantity is greater than 5

print(df[df['Quantity']>5])

# Showing  only the orders from a specific region (e.g., "East")
print(df[df['Region']=='East'])

#bar chart of total sales per region
df.groupby('Region')['Total'].sum().plot(kind='bar', title='Total Sales per Region')
plt.ylabel('Total Sales')
plt.xlabel('Region')
plt.show()


# Daily Revenue 
# Daily Revenue 
daily_revenue = df.groupby('Date')['Total'].sum()
plt.figure(figsize=(10, 5))
plt.plot(daily_revenue.index, daily_revenue.values, marker='o', label='Total Revenue')
plt.title('Daily Revenue')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)  
plt.tight_layout()
plt.grid(True)
plt.legend()
plt.show()


# Pie chart: Quantity sold per product
df.groupby('Product')['Quantity'].sum().plot(kind='pie',autopct='%1.1f%%',title='Quantity Sold per Product')
plt.show()

# Boxplot: Distribution of Total sales per Product
sns.boxplot(x='Product', y='Total', data=df)
plt.title('Sales Distribution by Product')
plt.show()

# Exporting the region-wise total sales to region_sales_summary.csv
grouped=df.groupby('Region')['Total'].sum()
print(grouped)
grouped.to_csv('region_sales_summary.csv')

# Day with highest revenue
top_day = df.groupby('Date')['Total'].sum().idxmax()
print("Day with highest revenue:", top_day)

# Product with highest quantity sold
top_product = df.groupby('Product')['Quantity'].sum().idxmax()
print("Top-selling product:", top_product)
