import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="WACC"
)

# Hide default formatting of Streamlit
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# Set the title of the page
st.markdown('<h1 style="color: #003554;">Weighted Average Cost of Capital</h1>', unsafe_allow_html=True)

Valuation ="Streamlit_app/Valuation.py"
from Valuation import cost_of_equity, cost_of_debt, cap_structure, w_cost_equity, w_cost_debt, wacc

# Function to format floating-point numbers
def format_float(x):
    if isinstance(x, (float, int)):
        return '{:.2f}'.format(x)
    else:
        return x

# Format the metric values
cost_of_equity_formatted = format_float(cost_of_equity * 100) + "%"    # Format cost of equity as a percentage
cost_of_debt_formatted = format_float(cost_of_debt * 100) + "%"        # Format cost of debt as a percentage
w_cost_equity_formatted = format_float(w_cost_equity * 100) + "%"      # Format weight of equity as a percentage
w_cost_debt_formatted = format_float(w_cost_debt * 100) + "%"          # Format weight of debt as a percentage
wacc_formatted = format_float(wacc * 100) + "%"                        # Format WACC as a percentage
cap_structure_formatted = "{:.0f} M€".format(cap_structure / 1e6)      # Format capital structure in millions of euros
wacc = wacc * 100                                                       # Convert WACC to a percentage
wacc = f"{wacc:.2f}%"                                                   # Format WACC as a percentage

# Set up the page layout with three columns
col1, col2, col3 = st.columns(3)

# Define the styled components using CSS styles

# CSS style for the wrapper of each metric value
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

# CSS style for the header of each metric value
stat_header_style = """
    color: #fafcfc;
"""

# CSS style for the metric value itself
stat_value_style = """
    color:  #fafcfc;
    font-size: 24px;
    font-weight: medium;
    display: center;
"""

# CSS style for a special metric value
stat_value_style1 = """
    color:  #FFA500;
    font-size: 28px;
    font-weight: medium;
    display: center;
"""

# Customize the metrics display in the columns
with col1:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}">Cost of equity</div >'
                f'<div style="{stat_value_style}">{cost_of_equity_formatted}</div>'
                f'</div>', unsafe_allow_html=True)

with col2:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}">WACC</div >'
                f'<div style="{stat_value_style1}">{wacc}</div>'
                f'</div>', unsafe_allow_html=True)

with col3:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}">Cost of debt</div >'
                f'<div style="{stat_value_style}">{cost_of_debt_formatted}</div>'
                f'</div>', unsafe_allow_html=True)

with col2:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}">Capital structure</div >'
                f'<div style="{stat_value_style}">{cap_structure_formatted}</div>'
                f'</div>', unsafe_allow_html=True)

with col1:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}">Weight of equity</div >'
                f'<div style="{stat_value_style}">{w_cost_equity_formatted}</div>'
                f'</div>', unsafe_allow_html=True)

with col3:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}">Weight of debt</div >'
                f'<div style="{stat_value_style}">{w_cost_debt_formatted}</div>'
                f'</div>', unsafe_allow_html=True)
