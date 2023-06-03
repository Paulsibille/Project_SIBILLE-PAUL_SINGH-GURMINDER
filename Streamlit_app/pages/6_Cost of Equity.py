import pandas as pd
import streamlit as st
import sys
sys.path.append('https://github.com/GurminSingh/test/tree/ec698ac3d5bd72359309efd47d786223f75a52c1/streamlit-multipage-app-example-master')
st.set_page_config(
    page_title="Cost of Equity"
)

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

st.markdown('<h1 style="color: #003554;">The Cost of Equity</h1>', unsafe_allow_html=True)

# Importing required functions from the "Valuation" module
from Valuation import erp, shares_outstanding, Current_Share_Price, definitive_coef_0, definitive_coef_2, stati_mean_SMB, marketCap, definitive_coef_1, stati_mean_HML, cost_of_equity

# Formatting the data for display
erp *= 100
erp = f"{erp:.2f}%"
marketCap = "{:.1f} M€".format(marketCap / 1e6)
Current_Share_Price = f"{Current_Share_Price:.2f}€"
shares_outstanding = "{:.1f} M".format(shares_outstanding / 1e6)
definitive_coef_0 = f"{definitive_coef_0:.2f}"
definitive_coef_1 = f"{definitive_coef_1:.2f}"
definitive_coef_2 = f"{definitive_coef_2:.2f}"
cost_of_equity *= 100
cost_of_equity = f"{cost_of_equity:.2f}%"

# CSS styles for the statistical values section
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

stat_header_style = """
    color: #fafcfc;
"""

stat_value_style = """
    color:  #fafcfc;
    font-size: 24px;
    font-weight: medium;
    display: center;
"""
stat_value_style1 = """
    color:  #FFA500;
    font-size: 28px;
    font-weight: medium;
    display: center;
"""

# CSS style for displaying the difference in statistical values
stat_diff_style = """
    color: #009688;
    font-weight: bold;
"""

stat_previous_style = """
    color: #46505A;
    font-size: 12px;
"""

# CSS style for the main container
container_style = """
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    margin-right: 10px;
    margin-left: 10px;
    margin-bottom: 10px;
"""

# Displaying the cost of equity
st.markdown(f'<div style="{stat_wrapper_style}">'
            f'<div  style="{stat_header_style}"></div >'
            f'<div style="{stat_value_style1}">{cost_of_equity}</div>'
            f'</div>', unsafe_allow_html=True)

st.markdown('<h3 style="color: #003554;">The Equity Risk Premium</h3>', unsafe_allow_html=True)

# Displaying the risk-free rate of Belgium
st.markdown(f'<div style="{stat_wrapper_style}">'
            f'<div  style="{stat_header_style}">Risk free rate of Belgium</div >'
            f'<div style="{stat_value_style}">{erp}</div>'
            f'</div>', unsafe_allow_html=True)

st.subheader('Market capitalization')
col1, col2, col3 = st.columns(3)

# Displaying market capitalization, shares outstanding, and current share price in separate columns
with col1:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}">Market capitalization</div >'
                f'<div style="{stat_value_style}">{marketCap}</div>'
                f'</div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}">Shares outstanding</div >'
                f'<div style="{stat_value_style}">{shares_outstanding}</div>'
                f'</div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}">Current Share Price</div >'
                f'<div style="{stat_value_style}">{Current_Share_Price}</div>'
                f'</div>', unsafe_allow_html=True)

st.markdown('<h3 style="color: #003554;">Betas Risks</h3>', unsafe_allow_html=True)

col1, col2, col3= st.columns(3)

# Displaying beta values for market risk, size risk, and value risk in separate columns
with col1:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}">Beta market risk</div >'
                f'<div style="{stat_value_style}">{definitive_coef_0}</div>'
                f'</div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}">Beta size risk</div >'
                f'<div style="{stat_value_style}">{definitive_coef_2}</div>'
                f'</div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}">Beta value risk</div >'
                f'<div style="{stat_value_style}">{definitive_coef_1}</div>'
                f'</div>', unsafe_allow_html=True)
