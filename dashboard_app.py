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

# Price Distribution (using 'Sale Price')
st.subheader(f"📈 Sale Price Distribution for {selected_brand}")
fig, ax = plt.subplots()
sns.histplot(filtered_df['Sale Price'], kde=True, ax=ax, color='skyblue')
st.pyplot(fig)
# Sale Price Distribution
st.subheader(f"📈 Sale Price Distribution for {selected_brand}")
fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(filtered_df['Sale Price'], kde=True, ax=ax, color='skyblue')
st.pyplot(fig)

# Discount Distribution
st.subheader(f"📉 Discount Distribution for {selected_brand}")
fig2, ax2 = plt.subplots(figsize=(8, 4))
sns.histplot(filtered_df['Discount'], kde=True, ax=ax2, color='lightgreen')
st.pyplot(fig2)

# Correlation Heatmap
st.subheader(f"🔍 Correlation Heatmap for {selected_brand}")
fig3, ax3 = plt.subplots(figsize=(6, 4))
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax3)
st.pyplot(fig3)


