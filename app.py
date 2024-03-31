import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    # Read the dataset's CSV file into a Pandas DataFrame
    df = pd.read_csv('/Users/rafaelhernadez/Documents/PythonProject/Web_app/vehicles_us.csv')

    # Header with text
    st.header('Exploratory Data Analysis')

    # Plotly Express histogram using st.plotly_chart
    histogram_data = px.histogram(df, x='column_name')
    st.plotly_chart(histogram_data)

    # Plotly Express scatter plot using st.plotly_chart
    scatter_data = px.scatter(df, x='column1', y='column2')
    st.plotly_chart(scatter_data)

    # Checkbox to toggle the display of the plots
    show_plots = st.checkbox('Show Plots')

    # Conditional display based on the checkbox value
    if show_plots:
        st.header('Plots')
        st.write('Histogram:')
        st.plotly_chart(histogram_data)

        st.write('Scatter Plot:')
        st.plotly_chart(scatter_data)

if __name__ == '__main__':
    main()

