import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go


# Set page config
st.set_page_config(
    page_title="Mithra"
)


# Page title
st.markdown('<h1 style="color: #003554; text-align: center">Mithra Pharmaceuticals SA</h1>', unsafe_allow_html=True)

# Overview section
st.markdown("""
    <div style='text-align: justify'>
    <h3 style="color: #003554; text-align: center">Overview</h3>
    Mithra is a leading Belgian pharmaceutical company specializing in women's and genital health. Founded in 1999 and headquartered in Liège, Belgium, the company is publicly listed on Euronext Brussels and Euronext Amsterdam.

    Mithra focuses on researching, developing, and commercializing innovative health products to meet the unmet needs of women and men worldwide. The company has a broad range of products, including hormonal contraceptives and treatments for menopause, fertility products, and treatments for infectious and inflammatory diseases.

    One of Mithra's flagship products is Estelle®, a combined contraceptive pill based on estetrol, a natural hormone produced by the fetus during pregnancy. Mithra has also developed a patented technology platform called Estetra®, which allows for the economic production of estetrol on a large scale.

    In addition to its research and development activities, Mithra is actively involved in promoting women's health and gender equality. Through its commitment to innovation, sustainability, and its broad range of health products for women and men worldwide, Mithra continues to advance the healthcare industry and strengthen its position as a global leader in women's and genital health.
    </div>
""", unsafe_allow_html=True)

# Activities section
st.markdown("""
    <div style='text-align: justify'>
    <h3 style="color: #003554; text-align: center">Activities</h3>
    Mithra is a Belgian pharmaceutical company that focuses on researching, developing, and commercializing innovative health products to meet the unmet needs of women and men worldwide. The company's activities include:
    <ol>
        <li>Research and development: Mithra invests heavily in research and development of new health products, particularly in women's and genital health. The company uses cutting-edge technologies to develop innovative products, such as hormonal contraceptives, menopause treatments, fertility products, and treatments for infectious and inflammatory diseases.</li>
        <li>Production: Mithra has state-of-the-art production facilities in Belgium to manufacture its pharmaceutical products. The company is committed to sustainable and environmentally friendly production, using production processes that minimize environmental impact.</li>
        <li>Commercialization: Mithra markets its pharmaceutical products in many countries around the world, working closely with local commercial partners and distributors. The company aims to expand its presence in emerging markets to meet the growing health needs of consumers.</li>
        <li>Commitment to women's health: Mithra is committed to promoting women's health and gender equality. The company participates in awareness campaigns, events, and initiatives to help improve women's health worldwide.</li>
    </ol>
    </div>
""", unsafe_allow_html=True)

# Strategies section
st.markdown("""
    <div style='text-align: justify'>
    <h3 style="color: #003554; text-align: center">Strategies</h3>
    Mithra's strategy, as presented in the report on the results of the first semester of 2022, is focused on growth, innovation, and geographical expansion.
    <ol>
        <li>Growth: Mithra continues to experience strong revenue growth, which increased by 39% in the first semester of 2022 compared to the same period the previous year. This growth is mainly due to increased demand for the company's existing products in its key markets.</li>
        <li>Innovation: The company conducts research projects in therapeutic areas such as contraception, menopause, and male genital health. Mithra has also launched Estelle®, a new oral contraceptive product, in several European countries and plans to introduce it to other markets in the coming months.</li>
        <li>Geographical expansion: Mithra has established strategic partnerships with international pharmaceutical companies to expand its presence in emerging markets such as Latin America, Asia, and the Middle East. These partnerships allow Mithra to market its products in new high-growth potential markets.</li>
        <li>Product portfolio diversification: Mithra aims to meet its customers' health needs by developing innovative products in therapeutic areas such as male genital health and dermatology.</li>
    </ol>
    In summary, Mithra's strategy is focused on growth, innovation, and geographical expansion, with strong demand for its existing products in key markets, ongoing research in new therapeutic areas, strategic partnerships to expand its geographical presence, and diversification of its product portfolio to meet its customers' health needs.
    </div>
""", unsafe_allow_html=True)

# Closing Price section
st.markdown("""
    <h3 style="color: #003554; text-align: center">Closing Price</h3>
""", unsafe_allow_html=True)

# Fetch data from Yahoo Finance
data = yf.Ticker("MITRA.BR").history(period='5y')
df = pd.DataFrame(data)

# Create the plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['Close'], marker_color='#003554'))
fig.update_layout(xaxis_title='Date', yaxis_title='Price')

# Display the plot in Streamlit app
st.plotly_chart(fig, use_container_width=True)



