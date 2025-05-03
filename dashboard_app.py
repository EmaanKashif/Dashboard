import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Page config
st.set_page_config(page_title="Amazon Sales Dashboard", layout="wide")

# Set Seaborn theme
sns.set_theme(style="whitegrid")
plt.rcParams["figure.dpi"] = 100

# Title
st.title("📊 Amazon Sales Dashboard - 2025")

# Load dataset
df = pd.read_csv("amazon_sales_data 2025.csv")

# Parse 'Date' column
df['Date'] = pd.to_datetime(df['Date'])

# Compute Total Sales column
df['Total'] = df['Quantity'] * df['Price']

st.subheader("🗃️ Preview of Amazon Sales Data")
st.dataframe(df.head())  # Show first few rows of the DataFrame

# Optional: Show dimensions
st.caption(f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

# Sidebar filters
with st.sidebar:
    st.header("Filters")
    product_filter = st.multiselect("Select Products", df['Product'].unique())
    if product_filter:
        df = df[df['Product'].isin(product_filter)]

# 1. Total Sales by Product Category
st.subheader("💰 Total Sales by Product Category")
category_sales = df.groupby('Product')['Total'].sum().sort_values(ascending=False)

fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.barplot(x=category_sales.values, y=category_sales.index, palette='viridis', ax=ax1)
ax1.set_title('Total Sales by Product Category')
ax1.set_xlabel('Total Sales')
ax1.set_ylabel('Product')
st.pyplot(fig1)

# 2. Monthly Sales Trend
st.subheader("📈 Monthly Sales Trend")
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Total'].sum()
monthly_sales.index = monthly_sales.index.astype(str)

fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker='o', color='teal', ax=ax2)
ax2.set_title('Monthly Sales Trend')
ax2.set_xlabel('Month')
ax2.set_ylabel('Total Sales')
plt.xticks(rotation=45)
st.pyplot(fig2)

# 3. Sales by Payment Method
st.subheader("💳 Sales by Payment Method")
payment_sales = df.groupby('Payment Method')['Total'].sum().sort_values(ascending=False)

fig3, ax3 = plt.subplots(figsize=(8, 4))
sns.barplot(x=payment_sales.index, y=payment_sales.values, palette='Set2', ax=ax3)
ax3.set_title('Sales by Payment Method')
ax3.set_xlabel('Payment Method')
ax3.set_ylabel('Total Sales')
st.pyplot(fig3)

