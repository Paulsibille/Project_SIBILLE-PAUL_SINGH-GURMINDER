# Import the necessary modules and libraries
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import sys
sys.path.append('https://github.com/GurminSingh/test/tree/ec698ac3d5bd72359309efd47d786223f75a52c1/streamlit-multipage-app-example-master')
# Set the page title
st.set_page_config(page_title="NWC")

# Hide the default format of the page
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# Display the title
st.markdown('<h1 style="color: #003554;">Net Working Capital</h1>', unsafe_allow_html=True)

# Import necessary modules and data
from Valuation import combined_df, M

# Define a function to format float values
def format_float(x):
    if isinstance(x, (float, int)):
        return '{:.2f}'.format(x)
    else:
        return x

# Prepare the DataFrame for display
df1 = pd.DataFrame(combined_df).reset_index().applymap(format_float)
df1.columns = ['', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028']

# Define a function to highlight specific rows in the DataFrame
def highlight_FCFF_row(row, highlight_rows):
    styles = ['' for _ in row]
    if row.name in highlight_rows:
        styles = ['background-color: #003554; color: #fafcfc' for _ in row]
    return styles

# Define the row names to be highlighted
highlight_rows = [2, 8, 14, 15]  # Add more row names if needed

# Apply the CSS styles to the DataFrame
highlighted_df = df1.style.apply(highlight_FCFF_row, highlight_rows=highlight_rows, axis=1)

# Convert styled DataFrame to HTML and hide index column
highlighted_html = highlighted_df.hide_index().to_html(index=False)

# Display the styled table
st.write(highlighted_html, unsafe_allow_html=True)

# Create an interactive bar chart
y_value = st.selectbox('', df1[''].unique())
x_values = df1.columns[1:]
y_values = df1.loc[df1[''] == y_value].values[0][1:]

fig = go.Figure()
fig.add_trace(go.Bar(x=x_values, y=y_values, marker_color='#003554'))
fig.update_layout(title=y_value, xaxis_title='', yaxis_title='')
st.plotly_chart(fig)

# Display the metrics section title
st.markdown('<h2 style="color: #003554;">Metrics</h2>', unsafe_allow_html=True)

# Prepare and display the metrics table
df2 = M.applymap(format_float)
df2.columns = ['2017', '2018', '2019', '2020', '2021', '2022', 'Average', 'Median', 'Last Value']
st.table(df2)
