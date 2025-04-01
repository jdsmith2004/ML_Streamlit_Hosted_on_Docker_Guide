import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Sidebar navigation
page = st.sidebar.selectbox("Select a Page", ["Title Page", "Graphs", "Machine Learning"])
# Title Page
if page == "Title Page":
    st.title("Streamlit Basics")
    st.markdown("# This is a Header (Large Title or #)")
    st.markdown("This is a simple paragraph of text.")
    st.markdown("**This is bold text**")
    st.markdown("*This is italicized text*")
    st.markdown("~~Strikethrough~~")
    st.markdown("`Inline code`")
    st.code("""
    # Code block example
    def say_hello():
        print("Hello World!")
    """, language="python")
    user_input = st.text_input("Please Enter Your Name: ")
    if user_input:
        st.write("Hello!", user_input,"! How nice to meet you!")
# Graphs Page
elif page == "Graphs":    
    # App title
    st.title("Graphs Demo for: Idaho Target Data")
    # Load data
    @st.cache_data
    def load_data():
        return pd.read_parquet("idaho_target_2023.parquet")

    df = load_data()



    df['DAY_OF_PREDICTION'] = pd.to_datetime(df['DAY_OF_PREDICTION'])

    # Filter data for January and February 2023
    df_filtered = df[(df['DAY_OF_PREDICTION'] >= "2023-01-01") & (df['DAY_OF_PREDICTION'] <= "2023-02-28")]
    # Group by DAY_OF_PREDICTION and sum TOTAL_QUANTITY
    df_grouped = df_filtered.groupby('DAY_OF_PREDICTION', as_index=False)['TOTAL_QUANTITY'].sum()

    st.title("TOTAL_QUANTITY Visualization (Jan & Feb 2023)")

    # Select chart type
    chart_type = st.selectbox("Select Chart Type", ["Line Chart", "Bar Chart"])

    # Create charts
    if chart_type == "Line Chart":
        fig = px.line(df_grouped, x='DAY_OF_PREDICTION', y='TOTAL_QUANTITY', title="TOTAL_QUANTITY Over Time (Jan & Feb 2023)")
        st.plotly_chart(fig)
    elif chart_type == "Bar Chart":
        fig = px.bar(df_grouped, x='DAY_OF_PREDICTION', y='TOTAL_QUANTITY', title="TOTAL_QUANTITY Distribution (Jan & Feb 2023)")
        st.plotly_chart(fig)

    st.write("The DataFrame:")
    st.dataframe(df.head())
# Machine Learning Page
elif page == "Machine Learning":
    st.title("Machine Learning Page")
    st.write("This page is currently blank.")
