# Importing required libraries
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import sys
sys.path.append('https://github.com/GurminSingh/test/tree/ec698ac3d5bd72359309efd47d786223f75a52c1/streamlit-multipage-app-example-master')
# Setting page configuration
st.set_page_config(
    page_title="Cost of Debt"
)

# Hiding default format for better layout
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# Adding a header for the Cost of Debt
st.markdown('<h1 style="color: #003554;">The Cost of Debt</h1>', unsafe_allow_html=True)

# Importing required data and functions from Valuation module
from Valuation import df, ratio, spread, total_debt, w_avg_maturity, cost_of_debt, debts, mv_debt, rf

# Function to format float values
def format_float(x):
    if isinstance(x, (float, int)):
        return '{:.2f}'.format(x)
    else:
        return x

# Applying formatting to relevant variables
df6 = df
total_debt = "{:.1f} M€".format(total_debt / 1_000)
w_avg_maturity = round(w_avg_maturity, 2)
cost_of_debt = cost_of_debt * 100
cost_of_debt = f"{cost_of_debt:.2f}%"
ratio = "{:.1f}".format(ratio)
spread = spread * 100
spread = f"{spread:.2f}%"
mv_debt = "{:.1f} M€".format(mv_debt / 1e6)
rf = rf * 100
rf = f"{rf:.2f}%"

# Styling for the statistical wrapper
stat_wrapper_style = """
    background-color: #003554;
    box-shadow: 1px 1px 10px rgba(0, 0, 0, 0.2);
    border-radius: 10px;
    padding: 10px;
    min-width: 170px;
    align-items: center;
    display: inline-block;
    flex-direction: column;
    margin-right: 10px;
    margin-bottom: 10px;
    text-align: center;
"""

# Styling for the statistical header
stat_header_style = """
    color: #fafcfc;
"""

# Styling for the statistical value
stat_value_style = """
    color:  #fafcfc;
    font-size: 24px;
    font-weight: medium;
    display: center;
"""

# Styling for the statistical value (highlighted)
stat_value_style1 = """
    color:  #FFA500;
    font-size: 28px;
    font-weight: medium;
    display: center;
"""

# Displaying the cost of debt in a statistical wrapper
st.markdown(f'<div style="{stat_wrapper_style}">'
            f'<div  style="{stat_header_style}"></div >'
            f'<div style="{stat_value_style1}">{cost_of_debt}</div>'
            f'</div>', unsafe_allow_html=True)

# Adding a header for the default spread
st.markdown('<h3 style="color: #003554;">The Default Spread</h3>', unsafe_allow_html=True)

# Displaying a table with data
st.table(df6)

# Creating columns for displaying statistics
col1, col2 = st.columns(2)

# Displaying the interest coverage ratio in a statistical wrapper
with col1:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}">Interest Coverage ratio</div >'
                f'<div style="{stat_value_style}">{ratio}</div>'
                f'</div>', unsafe_allow_html=True)

# Displaying the default spread in a statistical wrapper
with col2:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}">Default Spread</div >'
                f'<div style="{stat_value_style}">{spread}</div>'
                f'</div>', unsafe_allow_html=True)

# Adding a header for the market value of debt
st.markdown('<h3 style="color: #003554;">The Market value of debt</h3>', unsafe_allow_html=True)

# Creating a DataFrame with debt data
df = pd.DataFrame(debts, columns=['Year', 'Debt'])
df['Year'] = ['2023', '2024', '2025', '2028', '2033']

# Creating a bar chart for debt by maturity
fig = go.Figure(data=[go.Bar(x=df['Year'], y=df['Debt'], marker_color='#003554')])
fig.update_layout(
    title='Debt by maturity',
    xaxis_title='Year',
    yaxis_title='Debt',
    xaxis=dict(type='category'),
)
st.plotly_chart(fig)

# Creating columns for displaying additional statistics
col1, col2, col3= st.columns(3)

# Displaying the total debt in a statistical wrapper
with col1:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}">Total Debt</div >'
                f'<div style="{stat_value_style}">{total_debt}</div>'
                f'</div>', unsafe_allow_html=True)

# Displaying the weight to maturity in a statistical wrapper
with col2:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}">Weight to maturity</div >'
                f'<div style="{stat_value_style}">{w_avg_maturity}</div>'
                f'</div>', unsafe_allow_html=True)

# Displaying the market value of debt in a statistical wrapper
with col3:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}">Market value of debt</div >'
                f'<div style="{stat_value_style}">{mv_debt}</div>'
                f'</div>', unsafe_allow_html=True)

# Adding a header for the risk-free rate
st.markdown('<h3 style="color: #003554;">The risk free rate </h3>', unsafe_allow_html=True)

# Displaying the risk-free rate for Belgium in a statistical wrapper
st.markdown(f'<div style="{stat_wrapper_style}">'
            f'<div  style="{stat_header_style}">Belgium</div >'
            f'<div style="{stat_value_style}">{rf}</div>'
            f'</div>', unsafe_allow_html=True)
