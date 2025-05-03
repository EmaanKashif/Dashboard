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

# Filter by Brand
brands = df['Brand'].unique()
selected_brand = st.selectbox("Select Brand", brands)
filtered_df = df[df['Brand'] == selected_brand]

st.subheader(f"📊 Summary Statistics for {selected_brand}")
st.dataframe(filtered_df.describe())

# Use columns to show charts side-by-side
col1, col2 = st.columns(2)

# Sale Price Distribution
with col1:
    st.markdown("### 📈 Sale Price Distribution")
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.histplot(filtered_df['Sale Price'], kde=True, ax=ax, color='skyblue')
    st.pyplot(fig, clear_figure=True)

# Discount Distribution
with col2:
    st.markdown("### 📉 Discount Distribution")
    fig2, ax2 = plt.subplots(figsize=(5, 3))
    sns.histplot(filtered_df['Discount'], kde=True, ax=ax2, color='lightgreen')
    st.pyplot(fig2, clear_figure=True)

# Correlation Heatmap (Check if numeric columns exist)
numeric_columns = ['Listing Price', 'Sale Price', 'Discount', 'Rating', 'Reviews']
if all(col in filtered_df.columns for col in numeric_columns):
    st.markdown("### 🔍 Correlation Heatmap")
    corr = filtered_df[numeric_columns].corr()
    fig3, ax3 = plt.subplots(figsize=(5,3))
    
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax3)
    st.pyplot(fig3, clear_figure=True)
else:
    st.write("🔴 Not enough numeric data to generate a correlation heatmap.")


