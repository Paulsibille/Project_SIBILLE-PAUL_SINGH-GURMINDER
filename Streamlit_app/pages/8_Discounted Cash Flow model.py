import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import base64
import streamlit.components.v1 as components
import sys
# Set the page configuration
st.set_page_config(
    page_title="DCF"
)

# Hide default format for the page
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# Set the page title
st.markdown('<h1 style="color: #003554;">The Discounted Cash Flow model</h1>', unsafe_allow_html=True)

# Import required modules
sys.path.append('https://github.com/GurminSingh/test/tree/ec698ac3d5bd72359309efd47d786223f75a52c1/streamlit-multipage-app-example-master')  # Replace 'path/to/directory' with the actual path
from Valuation import sum_DCF, Discounted_Terminal_Value, Forecasted_Enterprise_Value, mv_debt, last_cash, Forecasted_Market_Cap, Forecasted_Share_Price, Current_Share_Price, gap_in_pct, wacc, share_price_mt

# Function to format floating-point numbers
def format_float(x):
    if isinstance(x, (float, int)):
        return '{:.2f}'.format(x)
    else:
        return x

# Format the metric values
sum_DCF = "{:.1f} M€".format(sum_DCF)
Discounted_Terminal_Value = "{:.1f} M€".format(Discounted_Terminal_Value)
Forecasted_Enterprise_Value = "{:.1f} M€".format(Forecasted_Enterprise_Value)
last_cash = "{:.1f} M€".format(last_cash)
mv_debt = "{:.1f} M€".format(mv_debt/1e6)
wacc = wacc * 100
wacc = f"{wacc:.2f}%"
Current_Share_Price1 = f"{Current_Share_Price:.2f}€"
Forecasted_Share_Price1 = f"{Forecasted_Share_Price:.2f}€"
gap_in_pct = f"{gap_in_pct:.2f}%"

# Define the styles for the metrics display
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
    font-size: 24px;
    font-weight: medium;
    display: center;
"""

# Create four columns for the metrics display
col1, col2, col3, col4 = st.columns(4)

# Display the metrics in the first column
with col1:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}">Discounted Terminal Value</div >'
                f'<div style="{stat_value_style}">{Discounted_Terminal_Value}</div>'
                f'</div>', unsafe_allow_html=True)

# Display the metrics in the second column
with col2:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}">Discounted Cash Flows</div >'
                f'<div style="{stat_value_style}">{sum_DCF}</div>'
                f'</div>', unsafe_allow_html=True)

# Display the metrics in the third column
with col3:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}">Forecasted Enterprise Value</div >'
                f'<div style="{stat_value_style1}">{Forecasted_Enterprise_Value}</div>'
                f'</div>', unsafe_allow_html=True)

# Display the metrics in the fourth column
with col4:
    st.markdown(
        f'<div style="{stat_wrapper_style}">'
        f'<div  style="{stat_header_style}"> Forecasted Share Price </div >'
        f'<div style="{stat_value_style1}">{Forecasted_Share_Price1}</div>'
        f'</div>',unsafe_allow_html=True)

# Display the remaining metrics in the columns
with col1:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}"> WACC </div >'
                f'<div style="{stat_value_style}">{wacc}</div>'
                f'</div>', unsafe_allow_html=True)

with col2:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}">Market Value of Debt</div >'
                f'<div style="{stat_value_style}">{mv_debt}</div>'
                f'</div>', unsafe_allow_html=True)

with col3:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}">Cash</div >'
                f'<div style="{stat_value_style}">{last_cash}</div>'
                f'</div>', unsafe_allow_html=True)

with col4:
    st.markdown(f'<div style="{stat_wrapper_style}">'
                f'<div  style="{stat_header_style}">Current Share Price</div >'
                f'<div style="{stat_value_style}">{Current_Share_Price1}</div>'
                f'</div>', unsafe_allow_html=True)

# Create the first graph
fig1 = go.Figure(go.Indicator(
    mode="gauge+number",
    value=Forecasted_Share_Price,
    title={'text': "Price"},
    domain={'x': [0, 1], 'y': [0, 1]},
    number={'font': {'color': '#003554'}}
))

# Create the second graph
fig2 = go.Figure()
fig2.add_trace(go.Indicator(
    mode="delta",
    value=Forecasted_Share_Price,
    delta={'reference': Current_Share_Price},
    domain={'row': 1, 'column': 1}
))

# Set the size of the figures
fig1.update_layout(width=300, height=400)
fig2.update_layout(width=400, height=400)

# Create a layout with two columns
col1, col2 = st.columns(2)

# Display the first graph in the first column
with col1:
    st.plotly_chart(fig1)

# Display the second graph in the second column
with col2:
    st.plotly_chart(fig2)

# Display the heading for the Monte Carlo Simulation
st.markdown('<h3 style="color: #003554;">Monte Carlo Simulation</h3>', unsafe_allow_html=True)

# Create the histogram for the share prices
fig = px.histogram(share_price_mt, nbins=50)
fig.update_layout(
    xaxis_title="Share prices",
    yaxis_title="Frequency"
)

# Set the color of the histogram
fig.update_traces(marker_color='#003554', showlegend=False)

# Adding a vertical line for the current share price
current_share_price = Current_Share_Price
fig.add_vline(
    x=current_share_price,
    line_color='red',
    line_dash='dash',
    line_width=1,
    name='Current Share Price',
    annotation_text='Current Share Price'
)

fig.update_layout(
    bargap=0.2
)

# Display the histogram
st.plotly_chart(fig)
