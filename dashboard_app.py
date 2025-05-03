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
    "Country": ["Myanmar", "Myanmar", "Myanmar", "Thailand", "Thailand", "Thailand", "China", "China", "China", "Vietnam", "Vietnam", "Vietnam"],
    "Region": ["Yangon", "Mandalay", "Naypyidaw", "Bangkok", "Chiang Mai", "Phuket", "Yunnan", "Guangxi", "Guizhou", "Hanoi", "Ho Chi Minh", "Da Nang"],
    "Date": ["2025-04-01", "2025-04-02", "2025-04-03", "2025-04-01", "2025-04-02", "2025-04-03", "2025-04-01", "2025-04-02", "2025-04-03", "2025-04-01", "2025-04-02", "2025-04-03"],
    "Casualties": [3000, 2000, 443, 40, 35, 15, 1, 0, 1, 1, 0, 0],
    "Injuries": [6000, 4000, 1402, 20, 10, 3, 0, 0, 0, 0, 0, 0],
    "Missing": [300, 200, 49, 5, 4, 2, 0, 0, 0, 0, 0, 0],
    "Affected Buildings": [5000, 2800, 500, 70, 60, 39, 150, 130, 120, 80, 60, 40],
    "Damage Cost (USD Millions)": [150, 100, 50, 8, 6, 3, 2, 1.5, 1, 1.2, 0.8, 0.6]
}
df = pd.DataFrame(data)
df["Severity Index"] = df["Casualties"] + df["Injuries"] + df["Missing"]


filtered_df = df[df["Country"].isin(country_filter)]
# Add this after filtering the data
st.subheader("📊 Casualties Over Time by Region")
fig_line = px.line(
    filtered_df,
    x="Date",
    y="Casualties",
    color="Region",
    markers=True,
    title="Casualties Over Time"
)
st.plotly_chart(fig_line, use_container_width=True)

st.subheader("🏥 Top 5 Most Affected Regions (Casualties)")
top_regions = filtered_df.sort_values(by="Casualties", ascending=False).head(5)
fig_bar_top = px.bar(
    top_regions,
    x="Casualties",
    y="Region",
    orientation="h",
    color="Region",
    title="Top 5 Regions by Casualties"
)
st.plotly_chart(fig_bar_top, use_container_width=True)

st.subheader("🏠 Proportion of Affected Buildings by Country")
fig_pie = px.pie(
    filtered_df,
    names="Country",
    values="Affected Buildings",
    title="Affected Buildings Distribution by Country"
)
st.plotly_chart(fig_pie, use_container_width=True)
st.subheader("📊 Casualties by Date and Country")
fig_bar = px.bar(
    filtered_df,
    x="Date",
    y="Casualties",
    color="Country",
    barmode="group",
    title="Casualties by Date and Country"
)
st.plotly_chart(fig_bar, use_container_width=True)


# Display total damage cost
total_cost = filtered_df["Damage Cost (USD Millions)"].sum()
st.metric("💰 Total Estimated Damage (USD Millions)", f"${total_cost:,.2f}")
st.subheader("📌 Insights")
most_affected = filtered_df.loc[filtered_df['Casualties'].idxmax()]
st.markdown(f"""
- **Most affected region:** {most_affected['Region']} ({most_affected['Country']})
- **Highest casualties:** {most_affected['Casualties']}
- **Total estimated damage:** ${total_cost:,.2f} million
""")


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



