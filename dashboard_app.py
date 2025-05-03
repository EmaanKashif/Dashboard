import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Adidas vs Nike Dashboard", layout="wide")

# Load data
df = pd.read_csv("Adidas Vs Nike.csv")

st.title("👟 Adidas vs Nike Sales Dashboard")

# Show raw data
if st.checkbox("Show Raw Data"):
    st.write(df)

# Ensure that the columns are numeric
df['Listing Price'] = pd.to_numeric(df['Listing Price'], errors='coerce')
df['Sale Price'] = pd.to_numeric(df['Sale Price'], errors='coerce')
df['Discount'] = pd.to_numeric(df['Discount'], errors='coerce')
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')

# Filter by Brand
brands = df['Brand'].unique()
selected_brand = st.selectbox("Select Brand", brands)
filtered_df = df[df['Brand'] == selected_brand]

# Show Summary Statistics
st.subheader(f"📊 Summary Statistics for {selected_brand}")
st.dataframe(filtered_df.describe())

# Bar Plot for Brand Distribution
st.markdown("### 🏷️ Product Count by Brand")
fig1, ax1 = plt.subplots(figsize=(6, 4))
filtered_df['Brand'].value_counts().plot(kind='bar', color='skyblue', ax=ax1)
ax1.set_title("Product Count by Brand")
st.pyplot(fig1)

# Histogram for Sale Price Distribution
st.markdown("### 📈 Sale Price Distribution")
fig2, ax2 = plt.subplots(figsize=(6, 4))
sns.histplot(filtered_df['Sale Price'], kde=True, ax=ax2, color='lightgreen')
ax2.set_title("Sale Price Distribution")
st.pyplot(fig2)

# Scatter Plot: Sale Price vs Listing Price
st.markdown("### 📉 Sale Price vs Listing Price")
fig3, ax3 = plt.subplots(figsize=(6, 4))
sns.scatterplot(x=filtered_df['Listing Price'], y=filtered_df['Sale Price'], ax=ax3, color='orange')
ax3.set_title("Sale Price vs Listing Price")
st.pyplot(fig3)

# Box Plot for Discount Distribution
st.markdown("### 📊 Discount Distribution")
fig4, ax4 = plt.subplots(figsize=(6, 4))
sns.boxplot(data=filtered_df, x='Discount', ax=ax4, color='lightcoral')
ax4.set_title("Discount Distribution")
st.pyplot(fig4)


