# Importing the required libraries
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sys
sys.path.append('https://github.com/GurminSingh/test/tree/ec698ac3d5bd72359309efd47d786223f75a52c1/streamlit-multipage-app-example-master')

# Setting the page title
st.set_page_config(page_title="FCFF")

def page1():
    st.write("This is Page 1")

# Hiding the default Streamlit menu and footer
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# Adding a title using HTML styling
st.markdown('<h1 style="color: #003554;">Free Cash Flow to Firm</h1>', unsafe_allow_html=True)

# Importing the FCFF_df from the Valuation module
from Valuation import FCFF_df

# Function to format float values
def format_float(x):
    if isinstance(x, (float, int)):
        return '{:.2f}'.format(x)
    else:
        return x

# Converting FCFF_df to a DataFrame and applying formatting
df1 = pd.DataFrame(FCFF_df).reset_index().applymap(format_float)
df1.columns = ['', '2017', '2018', '2019', '2020', '2021', '2022']

# Function to highlight specific rows in the DataFrame
def highlight_FCFF_row(row, highlight_rows):
    styles = ['' for _ in row]
    if row.name in highlight_rows:
        styles = ['background-color: #003554; color: #fafcfc' for _ in row]
    return styles

highlight_rows = [0, 2, 7, 10, 17, 19]  # Add more row names if needed
highlighted_df = df1.style.apply(highlight_FCFF_row, highlight_rows=highlight_rows, axis=1)
highlighted_html = highlighted_df.hide_index().to_html(index=False)

# Displaying the highlighted DataFrame
st.write(highlighted_html, unsafe_allow_html=True)

# Creating a dropdown to select the y-axis value
y_value = st.selectbox('', df1[''].unique())

# Extracting the x-axis and y-axis values for the selected y-value
x_values = df1.columns[1:]
y_values = df1.loc[df1[''] == y_value].values[0][1:]

# Creating a bar chart using Plotly
fig = go.Figure()
fig.add_trace(go.Bar(x=x_values, y=y_values, marker_color='#003554'))
fig.update_layout(title=y_value, xaxis_title='', yaxis_title='')

# Displaying the bar chart
st.plotly_chart(fig)
