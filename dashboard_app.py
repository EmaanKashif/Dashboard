import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load and clean data
df = pd.read_csv("Adidas Vs Nike.csv")
df['Brand'] = df['Brand'].str.lower().str.strip()

# Normalize brands strictly to adidas and nike only
df = df[df['Brand'].str.contains("adidas") | df['Brand'].str.contains("nike")]
df['Brand'] = df['Brand'].apply(lambda x: 'adidas' if 'adidas' in x else 'nike')

st.set_page_config(page_title="Adidas vs Nike Dashboard", layout="wide")
st.title("📈 Adidas vs Nike Product Dashboard")

# Sidebar filters
brands = df['Brand'].unique().tolist()
selected_brand = st.sidebar.multiselect("Select Brand(s)", brands, default=brands)

min_price = int(df['Sale Price'].min())
max_price = int(df['Sale Price'].max())
price_range = st.sidebar.slider("Select Sale Price Range", min_price, max_price, (min_price, max_price))

# Filtered Data
filtered_df = df[
    (df['Brand'].isin(selected_brand)) &
    (df['Sale Price'].between(price_range[0], price_range[1]))
]

st.markdown("---")

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total Products", len(filtered_df))
col2.metric("Average Discount (%)", round(filtered_df['Discount'].mean(), 2))
col3.metric("Average Rating", round(filtered_df['Rating'].mean(), 2))

# Tabs for visualization
tab1, tab2, tab3 = st.tabs(["Brand Insights", "Price & Discounts", "Customer Feedback"])

with tab1:
    st.subheader("🔍 Brand-Level Insights")
    brand_group = filtered_df.groupby("Brand").agg({
        "Sale Price": "mean",
        "Listing Price": "mean",
        "Discount": "mean",
        "Rating": "mean"
    }).reset_index()

    fig1 = px.bar(brand_group.sort_values("Discount", ascending=False), x="Brand", y="Discount",
                  color="Brand", title="Average Discount by Brand", text_auto=True)

    fig2 = px.bar(brand_group.sort_values("Rating", ascending=False), x="Brand", y="Rating",
                  color="Brand", title="Average Rating by Brand", text_auto=True, range_y=[0, 5])

    st.plotly_chart(fig1, use_container_width=True)
    st.plotly_chart(fig2, use_container_width=True)

with tab2:
    st.subheader("💸 Price & Discount Analysis")

    fig3 = px.histogram(filtered_df, x="Discount", nbins=30, color="Brand",
                        title="Distribution of Discounts", barmode="overlay", opacity=0.7)

    fig4 = px.scatter(filtered_df, x="Listing Price", y="Sale Price", color="Brand", size="Discount",
                      title="Sale vs Listing Price", hover_name="Product Name")

    # Add a diagonal reference line y=x
    fig4.add_trace(go.Scatter(x=[0, max(df['Listing Price'])], y=[0, max(df['Listing Price'])],
                              mode='lines', line=dict(dash='dash', color='gray'), name='Equal Price'))

    top_discounts = filtered_df.sort_values("Discount", ascending=False).head(10)
    top_discounts["Short Name"] = top_discounts["Product Name"].str.slice(0, 30)
    fig5 = px.bar(top_discounts, x="Discount", y="Short Name", orientation='h', color="Brand",
                  title="Top 10 Products with Highest Discounts", text_auto=True)

    st.plotly_chart(fig3, use_container_width=True)
    st.plotly_chart(fig4, use_container_width=True)
    st.plotly_chart(fig5, use_container_width=True)

with tab3:
    st.subheader("⭐ Customer Feedback")

    fig6 = px.histogram(filtered_df, x="Rating", nbins=10, color="Brand",
                        title="Rating Distribution", barmode='group', opacity=0.75)

    fig7 = px.scatter(filtered_df, x="Rating", y="Reviews", color="Brand", size="Reviews",
                      title="Rating vs Number of Reviews", hover_name="Product Name")

    st.plotly_chart(fig6, use_container_width=True)
    st.plotly_chart(fig7, use_container_width=True)

    # Optional Word Cloud from Descriptions
    if st.checkbox("Show Word Cloud from Descriptions"):
        text = " ".join(desc for desc in filtered_df['Description'].dropna())
        wordcloud = WordCloud(background_color='white', max_words=100).generate(text)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt)

st.markdown("---")
st.caption("Crafted with ❤️ using Streamlit and Plotly")
