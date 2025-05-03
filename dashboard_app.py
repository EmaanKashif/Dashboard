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
st.write(filtered_df.describe())

# Price Distribution
st.subheader(f"📈 Price Distribution for {selected_brand}")
fig, ax = plt.subplots()
sns.histplot(filtered_df['Price'], kde=True, ax=ax, color='skyblue')
st.pyplot(fig)

# Category Count
if 'Category' in df.columns:
    st.subheader(f"📊 Product Categories for {selected_brand}")
    category_counts = filtered_df['Category'].value_counts()
    st.bar_chart(category_counts)

# Correlation Heatmap
if filtered_df.select_dtypes(include='number').shape[1] > 1:
    st.subheader(f"🔍 Correlation Heatmap for {selected_brand}")
    corr = filtered_df.select_dtypes(include='number').corr()
    fig2, ax2 = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax2)
    st.pyplot(fig2)

