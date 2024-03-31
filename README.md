# Web_App

Project Description: This project aims to provide additional practice on common software engineering tasks while complementing data skills. The goal is to develop and deploy a web application to a cloud service, making it accessible to the public.

Dataset: The dataset used in this project is based on car sales advertisements, familiar from previous work.

This project replicates the process outlined in a blog post, focusing on practical implementation and deployment using the Render platform.

The project is rich with visuals, including histograms and scatter plots. Examples include: price distributions, bar chart of car models, examinations of car conditions by model year, among many others. 

Functions: 
1) display_histogram(selected_column):
This function takes a selected column as input (selected_column).
It uses Plotly Express (px) to create a histogram (px.histogram) based on the selected column from the DataFrame (df).
The title of the histogram is dynamically generated to indicate the distribution of the selected column.
Finally, the histogram is displayed using st.plotly_chart.

2) display_scatterplot(x_column, y_column):
This function takes two selected columns as input (x_column and y_column).
It uses Plotly Express (px) to create a scatter plot (px.scatter) based on the selected X and Y columns from the DataFrame (df).
The title of the scatter plot is dynamically generated to indicate the relationship between the X and Y columns.
The scatter plot is then displayed using st.plotly_chart.


How to use: 
Clone the repository to your local machine by running the following command in your terminal:

git clone https://github.com/your_username/your_repository.git

Navigate to the project directory using the cd command:
cd your_repository

Install the required libraries using pip by executing the following command:
pip install -r requirements.txt
