import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.title("Weather Data Analysis")

# Upload CSV
uploaded_file = st.file_uploader("Upload Weather Data", type="csv")
if uploaded_file:
    data = pd.read_csv(uploaded_file)

    # Show data
    st.write("### Dataset", data.head())

    # Analysis
    st.write("### Average Temperature")
    st.write(data['Temperature'].mean())

    # Visualization
    st.write("### Temperature Over Time")
    fig, ax = plt.subplots()
    sns.lineplot(x='Date', y='Temperature', data=data, ax=ax)
    st.pyplot(fig)
