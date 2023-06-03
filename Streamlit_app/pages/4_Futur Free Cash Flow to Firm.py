import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Set the page configuration and title
st.set_page_config(
    page_title="Futur FCFF"
)

# Hide the default Streamlit format and footer
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# Display a title using HTML markup
st.markdown('<h1 style="color: #003554;">Futur Free Cash Flow to Firm</h1>', unsafe_allow_html=True)

Valuation ="Streamlit_app/Valuation.py"
from Valuation import Futur_FCFF_df

# Define a function to format float values
def format_float(x):
    if isinstance(x, (float, int)):
        return '{:.2f}'.format(x)
    else:
        return x

# Create a DataFrame from Futur_FCFF_df and apply formatting
df1 = pd.DataFrame(Futur_FCFF_df).reset_index().applymap(format_float)
df1.columns = ['', '2023', '2024', '2025', '2026', '2027', '2028']

# Define a function to highlight specific rows in the DataFrame
def highlight_FCFF_row(row, highlight_rows):
    styles = ['' for _ in row]
    if row.name in highlight_rows:
        styles = ['background-color: #003554; color: #fafcfc' for _ in row]
    return styles

highlight_rows = [0, 2, 7, 10, 17, 19, 20]  # Add more row names if needed

# Apply row highlighting to the DataFrame and convert it to HTML
highlighted_df = df1.style.apply(highlight_FCFF_row, highlight_rows=highlight_rows, axis=1)
highlighted_html = highlighted_df.hide_index().to_html(index=False)

# Display the highlighted DataFrame in Streamlit
st.write(highlighted_html, unsafe_allow_html=True)

# Create interactive components for selecting data
y_value = st.selectbox('', df1[''].unique())
x_values = df1.columns[1:]
y_values = df1.loc[df1[''] == y_value].values[0][1:]

# Create a bar plot using Plotly
fig = go.Figure()
fig.add_trace(go.Bar(x=x_values, y=y_values, marker_color='#003554'))
fig.update_layout(title=y_value, xaxis_title='', yaxis_title='')

# Display the plot using Streamlit
st.plotly_chart(fig)
