import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set Seaborn theme
sns.set_theme(style="whitegrid")
plt.rcParams["figure.dpi"] = 100

# Load your dataset
df = pd.read_csv("amazon_sales_data 2025.csv")

# Parse 'Date' column
df['Date'] = pd.to_datetime(df['Date'])

# 1. Total Sales by Product Category
df['Total'] = df['Quantity'] * df['Price']
category_sales = df.groupby('Product')['Total'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(x=category_sales.values, y=category_sales.index, palette='viridis')
plt.title('Total Sales by Product Category', fontsize=14)
plt.xlabel('Total Sales')
plt.ylabel('Product')
plt.tight_layout()
plt.savefig('category_sales.png')
plt.close()

# 2. Monthly Sales Trend
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Total'].sum()

plt.figure(figsize=(10, 5))
monthly_sales.index = monthly_sales.index.astype(str)
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o', color='teal')
plt.title('Monthly Sales Trend', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_sales.png')
plt.close()

# 3. Sales by Payment Method
payment_sales = df.groupby('Payment Method')['Total'].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 4))
colors = sns.color_palette("Set2")
sns.barplot(x=payment_sales.index, y=payment_sales.values, palette=colors)
plt.title('Sales by Payment Method', fontsize=14)
plt.xlabel('Payment Method')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('payment_sales.png')
plt.close()
