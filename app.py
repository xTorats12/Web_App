import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    # Read the dataset CSV file into a Pandas DataFrame
    df = pd.read_csv('/Users/rafaelhernadez/Documents/PythonProject/Web_app/vehicles_us.csv')

    # Display the DataFrame
    st.write(df)

if __name__ == '__main__':
    main()
