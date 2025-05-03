import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="2025 Myanmar-Thailand Earthquake Impact", layout="wide")

# Title
st.title("🌏 2025 Myanmar-Thailand Earthquake Impact Dashboard")

# Sidebar for user input
st.sidebar.header("Filter Options")
country_filter = st.sidebar.multiselect(
    "Select Country",
    options=["Myanmar", "Thailand", "China", "Vietnam"],
    default=["Thailand"]
)

# Sample data (replace with actual data sources)
data = {
    "Country": ["Myanmar", "Thailand", "China", "Vietnam"],
    "Casualties": [5443, 90, 2, 1],
    "Injuries": [11402, 33, 0, 0],
    "Missing": [549, 11, 0, 0],
    "Affected Buildings": [8300, 169, 400, 400]
}
df = pd.DataFrame(data)
filtered_df = df[df["Country"].isin(country_filter)]

# Display metrics
st.subheader("📌 Key Impact Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Casualties", f"{filtered_df['Casualties'].sum():,}")
col2.metric("Total Injuries", f"{filtered_df['Injuries'].sum():,}")
col3.metric("Total Missing", f"{filtered_df['Missing'].sum():,}")

# Bar chart for affected buildings
st.subheader("🏚️ Affected Buildings by Country")
fig = px.bar(
    filtered_df,
    x="Country",
    y="Affected Buildings",
    color="Country",
    labels={"Affected Buildings": "Number of Buildings"},
    title="Number of Affected Buildings by Country"
)
st.plotly_chart(fig, use_container_width=True)

# Display data table
st.subheader("📄 Detailed Data")
st.dataframe(filtered_df.reset_index(drop=True))  # Display filtered data



