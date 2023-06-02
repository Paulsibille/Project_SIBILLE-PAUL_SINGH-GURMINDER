# Project - Financial modeling using Python - The case of Mithra - SIBILLE & SINGH

## 1. Presentation and summary of the analysis

This project aims to conduct a financial modeling analysis on Mithra, a Belgian company. It provides an intriguing framework for DCF analysis that can be adapted to analyze other companies. The framework consists of a Jupyter Notebook and a Streamlit web application.

We both serve as managing directors in different sectors of the junior enterprise HEC Investing Group. In our roles, we regularly perform DCF analysis to evaluate companies and determine whether their share prices are overpriced or underpriced. The framework we are discussing here is particularly interesting to us because it automates the analysis process and enables us to present the findings on a user-friendly website. For this project, we have conducted the DCF analysis specifically on Mithra, a company focused on providing healthcare products for women. We selected Mithra due to its substantial growth potential and its location in Liège.

The central question we seek to answer through this analysis is: "Is Mithra's stock currently overpriced or underpriced?"

To carry out this project, we rely on several data sources. We retrieve relevant data from an Excel file named "Mithra_statement.xlsx" and utilize the yfinance API to gather information on the number of outstanding shares and other relevant data points. Additionally, we used Quandl to access financial data from other American companies. To retrieve specific information, we employ web scraping techniques using tools such as Beautiful Soup and Selenium, targeting websites such as Damodaran's (https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm) and slickcharts (https://www.slickcharts.com/).

In terms of data works, we primarily use pandas to help us organize and process the data, while the statistics module enables us to perform basic statistical calculations like medians and means. For more advanced analysis, we employ the statsmodels package, which allows us to conduct multiple linear regressions. Additionally, we use the NumPy and its Normal function for conducting Monte Carlo analysis.

As a final step, we convert the DataFrame into an Excel file using xlsxwriter, as this format is more accessible for the junior enterprise members who may not be experienced with Python. We also create a public website using Streamlit, where the analysis and its results are presented. [INSERT THE WEBSITE ADDRESS HERE]

The key findings of our analysis highlight Mithra's exceptional growth potential. We estimate a potential gain of nearly 400%, indicating that, based on our estimations, an investment in Mithra could potentially multiply by nearly four times. 

In conclusion, the financial modeling analysis conducted on Mithra, a Belgian healthcare company, reveals significant growth potential. The framework's automation and user-friendly presentation through a web application make it valuable for respectively determining and representing the overpriced or underpriced nature of stocks. Based on our estimations, an investment in Mithra has the potential to yield substantial returns, multiplying the initial investment by almost 4. 

## 2. Description of the uploaded files

Here is the description on the severall files you can find on the github: 

1. 'Mithra_statement.xlsx' is an Excel file that contains the cash flow statement, the income statement, and the balance sheet of Mithra. This Excel file is important since it is where the main financial data related to the company is retrieved.

2. 'Mithra Valuation.ipynb' is a Jupyter Notebook where all the different computations have been carried out, allowing us to export all the results into an Excel file. This Excel file will be created and exported in the same directory as the Jupyter Notebook.

3. METTRE LE DOSSIER POUR L'APP

## 3. Package to install

There are different packages that we have used in order to make perform the analysis: 

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
METTRE LES PACKAGE POUR STREAMLIT
