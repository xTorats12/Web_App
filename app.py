
import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset's CSV file into a Pandas DataFrame
df = pd.read_csv('vehicles_us.csv') 

# Function to display a Plotly Express histogram based on the selected column
def display_histogram(selected_column):
    fig = px.histogram(df, x=selected_column, title=f'Distribution of {selected_column.capitalize()}')
    st.plotly_chart(fig)

# Function to display a Plotly Express scatter plot based on the selected columns
def display_scatterplot(x_column, y_column):
    fig = px.scatter(df, x=x_column, y=y_column, title=f'Scatter Plot: {x_column.capitalize()} vs {y_column.capitalize()}')
    st.plotly_chart(fig)

# Main function
def main():
    st.header('Exploratory Data Analysis')

    # Checkbox to toggle the display of histograms
    show_histograms = st.checkbox('Show Histograms')

    if show_histograms:
        selected_column = st.selectbox('Select a column for histogram:', df.columns)
        display_histogram(selected_column)

    # Checkbox to toggle the display of scatter plots
    show_scatterplots = st.checkbox('Show Scatter Plots')

    if show_scatterplots:
        x_column = st.selectbox('Select X-axis column:', df.columns)
        y_column = st.selectbox('Select Y-axis column:', df.columns)
        display_scatterplot(x_column, y_column)

if __name__ == '__main__':
    main()

