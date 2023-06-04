
# Project - Python-Powered DCF Analysis - The case of Mithra - SIBILLE  & SINGH

## Table of Contents:

- [Presentation and summary of the analysis](#presentation-and-summary-of-the-analysis)
- [Description of the uploaded files](#description-of-the-uploaded-files)
- [Package to install](#package-to-install)
- [Streamlit app](#streamlit-app)
- [Project Description](#project-description)
  - [Mithra Pharmaceuticals SA](#mithra-pharmaceuticals-sa)
  - [Free Cash Flow to Firm](#Free-Cash-Flow-to-Firm)
  - [Net Working Capital](#net-working-capital)
  - [Product](#product)
  - [Futur Free Cash Flow to Firm](#Futur-Free-Cash-Flow-to-Firm)
  - [Cost of Debt](#cost-of-debt)
  - [Cost of Equity ](#cost-of-equity)
  - [Weighted Average Cost of Capital ](#wacc)
  - [Discounted Cash Flow (DCF) Model and Monte Carlo Simulation](#discounted-cash-flow-dcf-model-and-monte-carlo-simulation)
- [Installation](#installation)
- [Usage](#usage)
- [Streamlit cloud ](#Streamlit-cloud) 
- [Contact](#contact)

## Presentation and summary of the analysis


This project aims to conduct a financial modeling analysis on Mithra, a Belgian company. It provides an intriguing framework for DCF analysis that can be adapted to analyze other companies. The framework consists of a Jupyter Notebook and a Streamlit web application.

We both serve as managing directors in different sectors of the junior enterprise HEC Investing Group. In our roles, we regularly perform DCF analysis to evaluate companies and determine whether their share prices are overpriced or underpriced. The framework we are discussing here is particularly interesting to us because it automates the analysis process and enables us to present the findings on a user-friendly website. For this project, we have conducted the DCF analysis specifically on Mithra, a company focused on providing healthcare products for women. We selected Mithra due to its substantial growth potential and its location in Liège.

The central question we seek to answer through this analysis is: "Is Mithra's stock currently overpriced or underpriced?"

To carry out this project, we rely on several data sources. We retrieve relevant data from an Excel file named ```Mithra_statement.xlsx"``` and utilize the yfinance API to gather information on the number of outstanding shares and other relevant data points. Additionally, we used Quandl to access financial data from other American companies. To retrieve specific information, we employ web scraping techniques using tools such as ```Beautiful Soup``` and ```Selenium```, targeting websites such as Damodaran ```https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.html```, slickcharts
```https://www.slickcharts.com/``` and World Government Bonds ```http://www.worldgovernmentbonds.com/```


In terms of data works, we primarily use pandas to help us organize and process the data, while the statistics module enables us to perform basic statistical calculations like medians and means. For more advanced analysis, we employ the statsmodels package, which allows us to conduct multiple linear regressions. Additionally, we use ```NumPy``` and its Normal function for conducting Monte Carlo analysis.

As a final step, we convert the DataFrame into an Excel file using xlsxwriter, as this format is more accessible for the junior enterprise members who may not be experienced with Python. We also create a public website using Streamlit, where the analysis and its results are presented.

```
https://mithra-valuation.streamlit.app/
```

The key findings of our analysis highlight Mithra's exceptional growth potential. We estimate a potential gain of nearly 400%, indicating that, based on our estimations, an investment in Mithra could potentially multiply by nearly four times.

In conclusion, the financial modeling analysis conducted on Mithra, a Belgian healthcare company, reveals significant growth potential. The framework's automation and user-friendly presentation through a web application make it valuable for respectively determining and representing the overpriced or underpriced nature of stocks. Based on our estimations, an investment in Mithra has the potential to yield substantial returns, multiplying the initial investment by almost 4.

## Description of the uploaded files

Here is the description of the several files you can find on GitHub:

1. ```Mithra_statement.xlsx``` is an Excel file that contains the cash flow statement, the income statement, and the balance sheet of Mithra. This Excel file is important since it is where the main financial data related to the company is retrieved.

2. ```Mithra Valuation.ipynb``` is a Jupyter Notebook where all the different computations have been carried out, allowing us to export all the results into an Excel file. This Excel file will be created and exported in the same directory as the Jupyter Notebook.

3. ```Streamlit_app``` is the main file that contains all the necessary files to deploy the Streamlit app.

## Packages to Install

To run the analysis and the Streamlit web application, the following packages need to be installed:

```
pip install pandas
pip install numpy
pip install xlsxwriter
pip install yfinance
pip install requests
pip install beautifulsoup4
pip install selenium
pip install quandl
pip install statsmodels
pip install matplotlib
```

## Streamlit app

This part concern the Streamlit app. It provides an overview of the project, installation instructions, usage guidelines, customization options, and licensing information.
```https://mithra-valuation.streamlit.app/```

Our app goes beyond simply displaying metrics. It operates using a file ```Valuation.py``` that calculates all the necessary data beforehand. This means that when the user navigate between different pages, the app doesn't waste any time loading or processing information.

By having a separate file for calculations, our app becomes dynamic and responsive. It ensures that the user can quickly access the data needed without any delays or slowdowns. The ```Valuation.py``` file does all the heavy lifting in the background, so the user can enjoy a smooth and efficient user experience.

### Project Description

The Mithra-valuation app is a collection of python files used in Streamlit, a Python web framework for creating interactive data applications. Each application focuses on a specific domain and provides visualizations, data analysis, and insights related to that domain.

#### Mithra Pharmaceuticals SA

This page provide an overview of Mithra Pharmaceuticals SA, a leading Belgian pharmaceutical company specializing in women's and genital health. The application includes sections on the company's overview, activities, strategies, and closing stock price.

#### Free Cash Flow to Firm    

It displays the Free Cash Flow to Firm (FCFF) and visualizes it using bar charts. It utilizes the `pandas` library for data manipulation and the `plotly` library for interactive charting.

#### Net Working Capital 

This Streamlit dashboard displays and visualizes net working capital data. It includes a styled table, an interactive bar chart, and a metrics table.

#### Product

This dashboard visualizes product revenue data. It provides interactive visualizations and highlights specific rows in a revenue DataFrame.

#### Futur Free Cash Flow to Firm

It displays the futur Free Cash Flow to Firm (FCFF) and visualizes it using bar charts. It utilizes the `pandas` library for data manipulation and the `plotly` library for interactive charting.

#### Cost of Debt 

This Streamlit dashboard analyzes the cost of debt and related financial metrics. It displays various statistics and visualizations to help understand the debt profile and risk factors.

#### Cost of Equity 

This Streamlit application calculates and displays various statistical values related to the cost of equity. It utilizes market data and statistical values to determine the cost of equity and displays related information.

#### Weighted Average Cost of Capital

This page calculates the Weighted Average Cost of Capital (WACC). It assesses the average cost of capital for a company, considering its capital structure and the cost of different sources of financing.

#### Discounted Cash Flow (DCF) Model and Monte Carlo Simulation

This project implements a Discounted Cash Flow (DCF) model and Monte Carlo simulation. It provides visualizations and metrics related to the valuation of a company based on discounted future cash flows and share price forecasts.

### Installation

To install and run these web applications locally, follow the steps below:

1. Clone the repository:

```
git clone https://github.com/Paulsibille/Project_SIBILLE-PAUL_SINGH-GURMINDER.git
```

2. Navigate to the project directory:

```
cd Streamlit_app/Company.py
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```
4. Do not forget to change the necessary file paths in files if it is necessary 

### Usage

To run the web applications, execute the following command in your terminal:

```
streamlit run path/Company.py
```
 
Open your web browser and access the provided URL to interact with the application.


https://github.com/Paulsibille/Project_SIBILLE-PAUL_SINGH-GURMINDER/assets/127745669/038f4562-01b5-42fe-b171-6a96939e27e0

### Streamlit cloud 

If you prefer not to deploy the app using your terminal, you can simply click on the link below. We have launch of our website and accessible to everyone. This accomplishment was made possible by utilizing Streamlit Cloud for hosting the web application.
```https://mithra-valuation.streamlit.app/```

### Contact

For any questions or inquiries, please contact [gurminsingh15@gmail.com](mailto:your-email@example.com) & [paulsibille303@gmail.com](mailto:your-email@example.com).
