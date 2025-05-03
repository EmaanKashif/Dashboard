import streamlit as st
import pandas as pd

st.set_page_config(page_title="Adidas vs Nike Dashboard", layout="wide")

# Title
st.title("👟 Adidas vs Nike Sales Dashboard")

# Load data
df = pd.read_csv("Adidas Vs Nike.csv")

# Show raw data
if st.checkbox("Show Raw Data"):
    st.write(df)

# Brand filter
brands = df['Brand'].unique()
selected_brand = st.selectbox("Select Brand", brands)

filtered_df = df[df['Brand'] == selected_brand]

# Display filtered data
st.subheader(f"Data for {selected_brand}")
st.write(filtered_df)

# Summary stats
st.subheader("Summary Statistics")
st.write(filtered_df.describe())
