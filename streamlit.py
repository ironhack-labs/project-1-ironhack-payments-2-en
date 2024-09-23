import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('cohort_analysis_data.csv')

# Select metric
metric = st.selectbox('Choose a metric', ['Total Revenue', 'Average Usage', 'Retention Rate'])

# Plot based on metric
def plot_metric(data, metric):
    plt.figure(figsize=(10, 6))

    if metric == 'Total Revenue':
        plt.plot(data['cohort_month'], data['total_revenue'], marker='o', color='green')
        plt.title('Total Revenue by Cohort')
        plt.xlabel('Cohort Month')
        plt.ylabel('Total Revenue')

    elif metric == 'Average Usage':
        plt.plot(data['cohort_month'], data['average_usage'], marker='o')
        plt.title('Average Usage per User')
        plt.xlabel('Cohort Month')
        plt.ylabel('Average Usage')

    elif metric == 'Retention Rate':
        plt.plot(data['cohort_month'], data['retention_rate'], marker='o', color='purple')
        plt.title('Retention Rate by Cohort')
        plt.xlabel('Cohort Month')
        plt.ylabel('Retention Rate')

    st.pyplot(plt)

# Call the function to plot the selected metric
plot_metric(data, metric)
