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
    "Country": ["Myanmar", "Myanmar", "Thailand", "Thailand", "China", "China", "Vietnam", "Vietnam", "Myanmar", "Thailand", "China", "Vietnam"],
    "Region": ["Yangon", "Mandalay", "Chiang Mai", "Bangkok", "Yunnan", "Guangxi", "Hanoi", "Ho Chi Minh", "Naypyidaw", "Phuket", "Guizhou", "Da Nang"],
    "Date": ["2025-04-01", "2025-04-02", "2025-04-01", "2025-04-03", "2025-04-01", "2025-04-02", "2025-04-02", "2025-04-03", "2025-04-03", "2025-04-04", "2025-04-04", "2025-04-04"],
    "Casualties": [3000, 2443, 40, 50, 1, 1, 1, 0, 1000, 30, 0, 0],
    "Injuries": [6000, 5402, 15, 18, 0, 0, 0, 0, 2000, 5, 0, 0],
    "Missing": [300, 249, 5, 6, 0, 0, 0, 0, 100, 0, 0, 0],
    "Affected Buildings": [5000, 3300, 80, 89, 200, 200, 100, 300, 2500, 20, 100, 100],
    "Damage Cost (USD Millions)": [150, 120, 10, 12, 2, 3, 1, 1.5, 80, 1, 1, 1]
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



