# Importing necessary libraries
import streamlit as st
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import base64
import sys
sys.path.append('https://github.com/GurminSingh/test/tree/ec698ac3d5bd72359309efd47d786223f75a52c1/streamlit-multipage-app-example-master')
# Setting the page configuration
st.set_page_config(
    page_title="Product"
)

# Hiding default formatting
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# Displaying a header
st.markdown('<h1 style="color: #003554;"> Product</h1>', unsafe_allow_html=True)

# Adding a path to sys.path
sys.path.append('/Users/gavysingh/Downloads/streamlit-multipage-app-example-master')  # Replace 'path/to/directory' with the actual path

# Importing from a module called Valuation
from Valuation import Assumption_revenues_df

# Defining a function to format float values
def format_float(x):
    if isinstance(x, (float, int)):
        return '{:.2f}'.format(x)
    else:
        return x

# Creating a DataFrame from Assumption_revenues_df and formatting it
df1 = pd.DataFrame(Assumption_revenues_df)
df1 = df1.reset_index()
df1.columns = ['', '2023', '2024', '2025', '2026', '2027', '2028']
df1 = df1.applymap(format_float)

# Defining the rows to be highlighted
highlight_rows = [4]

# Function to highlight specific rows in the DataFrame
def highlight_FCFF_row(row, highlight_rows):
    styles = ['' for _ in row]
    if row.name in highlight_rows:
        styles = ['background-color: #003554; color: #fafcfc' for _ in row]
    return styles

# Applying the row highlighting to the DataFrame
highlighted_df = df1.style.apply(highlight_FCFF_row, highlight_rows=highlight_rows, axis=1)
highlighted_html = highlighted_df.hide_index().to_html(index=False)

# Displaying the highlighted DataFrame
st.write(highlighted_html, unsafe_allow_html=True)

# Transposing the Assumption_revenues_df DataFrame
Assumption_revenues_df = Assumption_revenues_df.T

# Melting the DataFrame for visualization
melted_df = pd.melt(Assumption_revenues_df, ignore_index=False, var_name='Product', value_name='Sales')
melted_df.reset_index(inplace=True)
melted_df.rename(columns={'index': 'Year'}, inplace=True)

# Filtering out the 'Total' rows from melted_df
melted_df = melted_df[melted_df['Product'] != 'Total']

# Defining labels and color scale for the sunburst chart
labels = {
    'Year': 'Year',
    'Product': 'Product',
    'Sales': 'Sales (in millions)',
}
color_scale = 'Blues'

# Creating the sunburst chart using Plotly Express
fig = px.sunburst(melted_df, path=['Year', 'Product'], values='Sales', color='Sales',
                  color_continuous_scale=color_scale, hover_name='Year', labels=labels,
                  branchvalues='total', title='Revenues by Year and Product')

# Displaying the sunburst chart
st.plotly_chart(fig)
