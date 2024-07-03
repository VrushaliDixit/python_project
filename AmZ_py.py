#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns


# In[8]:


# Load the dataset
df = pd.read_csv('Amazon Sales data.csv')


# In[9]:


df.head()


# In[10]:


# Convert date columns to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Extract year and month from order_date
df['order_year'] = df['Order Date'].dt.year
df['order_month'] = df['Order Date'].dt.month
df['order_month_year'] = df['Order Date'].dt.to_period('M')

# Display the updated DataFrame
print(df.head())


# In[11]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[12]:


# Monthly sales trend
monthly_sales = df.groupby('order_month_year').agg({'Total Revenue': 'sum'}).reset_index()


# In[15]:


# Ensure 'order_month_year' is a string
monthly_sales['order_month_year'] = monthly_sales['order_month_year'].astype(str)

# Convert 'order_month_year' to datetime
monthly_sales['order_month_year'] = pd.to_datetime(monthly_sales['order_month_year'], format='%b-%Y', errors='coerce')

# Drop any rows where 'order_month_year' conversion failed
monthly_sales = monthly_sales.dropna(subset=['order_month_year'])

# Sort the DataFrame by 'order_month_year'
monthly_sales = monthly_sales.sort_values('order_month_year')

plt.figure(figsize=(14, 6))
sns.lineplot(x='order_month_year', y='Total Revenue', data=monthly_sales, marker='o')
plt.title('Monthly Sales Trend', fontsize=16)
plt.xlabel('Month-Year', fontsize=14)
plt.ylabel('Total Revenue', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[16]:


monthly_sales['order_month_year'] = monthly_sales['order_month_year'].astype(str)


# In[17]:


monthly_sales['order_month_year'] = pd.to_datetime(monthly_sales['order_month_year'], format='%b-%Y', errors='coerce')


# In[18]:


monthly_sales = monthly_sales.dropna(subset=['order_month_year'])


# In[19]:


monthly_sales = monthly_sales.sort_values('order_month_year')


# In[21]:


# Yearly sales trend
yearly_sales = df.groupby('order_year').agg({'Total Revenue': 'sum'}).reset_index()

# Plotting the yearly sales trend
plt.figure(figsize=(10, 5))
sns.barplot(x='order_year', y='Total Revenue', data=yearly_sales, palette='viridis')
plt.title('Yearly Sales Trend')
plt.xlabel('Year')
plt.ylabel('Total Revenue')
plt.show()


# In[24]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Example DataFrame structure
# df = pd.DataFrame({
#     'order_date': ['2020-01-01', '2020-02-01', '2020-03-01', ...],
#     'Total Revenue': [1000, 1500, 2000, ...]
# })
# df['order_date'] = pd.to_datetime(df['order_date'])
# df['order_year'] = df['order_date'].dt.year
# df['order_month'] = df['order_date'].dt.month

# Group by year and month, then aggregate the total revenue
yearly_monthly_sales = df.groupby(['order_year', 'order_month']).agg({'Total Revenue': 'sum'}).reset_index()

# Pivot the data for better visualization
pivot_table = yearly_monthly_sales.pivot_table(index='order_month', columns='order_year', values='Total Revenue')

# Plotting the heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=True, fmt='.0f', cmap='YlGnBu')
plt.title('Yearly Month-wise Sales Trend')
plt.xlabel('Year')
plt.ylabel('Month')
plt.show()


# In[25]:


yearly_monthly_sales = df.groupby(['order_year', 'order_month']).agg({'Total Revenue': 'sum'}).reset_index()


# In[26]:


pivot_table = yearly_monthly_sales.pivot_table(index='order_month', columns='order_year', values='Total Revenue')


# In[27]:


plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=True, fmt='.0f', cmap='YlGnBu')
plt.title('Yearly Month-wise Sales Trend')
plt.xlabel('Year')
plt.ylabel('Month')
plt.show()


# In[ ]:




