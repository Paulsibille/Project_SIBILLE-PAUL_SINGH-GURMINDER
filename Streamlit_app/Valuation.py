#!/usr/bin/env python
# coding: utf-8

# ## Cleaning and Import of the CF Statement, the Income Statement and the Balance Sheet 

# This part of the code aim to clean the data. For instance, in the excel file, you may note that there is some blank line. This part of the code has a goal to delete those empty lines. 

# In[21]:


import pandas as pd
import numpy as np

all_statements_path = 'streamlit-multipage-app-example-master/Classeur3.xlsx'

def load_and_clean_statement_df(statements_path, sheet_name):
    df = pd.read_excel(statements_path, sheet_name=sheet_name, engine='openpyxl', index_col=0)
    df = df.replace('-', np.nan)
    df = df.dropna(how='all')
    df = df.fillna(0) 
    return df

inc_df = load_and_clean_statement_df(all_statements_path, 'Income Statement')
ca_df = load_and_clean_statement_df(all_statements_path, 'Cash Flow')
bs_df = load_and_clean_statement_df(all_statements_path, 'Balance Sheet')


# In[2]:


inc_df.head()


# In[ ]:


ca_df.head()


# In[ ]:


bs_df.head()


# ## Visualisation of the past FCFF : basic and vertical analysis

# This part will be divided into 3 sections: 
# 
#     - Computation and visualisation of the Change in NWC. This step is important to compute the past FCFF of the firm
#     - Basic analysis of the FCFF: this step gives us a clear visualisation of the past FCFF, computed thanks to the change in NWC among others
#     - Vertical analysis of the FCFF: this step allow us to see clearly the importance of the different element that compose the FCFF

# ### 1. Change in NWC: computation and visualisation
# 

# This first part of the code compute the change in net working capital of the company. The more the NWC is big, the more the company needs cash to finance the liquidity requirement. In other words, the more the NWC is big, the more the current operating liabities are liquid compared to the current operating assets

# In[22]:


Currents_Assets=""
Currents_Liabilities=""
ocl_list=bs_df.loc['Other Current Liabilities']
if 'Unearned Revenue, Current' in bs_df.index:
    ocl_list += bs_df.loc['Unearned Revenue, Current'] 
Net_current_assets=bs_df.loc['  Total Receivables']+bs_df.loc['Inventory']+bs_df.loc['Prepaid Exp.']+bs_df.loc['Other Current Assets']
Net_Current_Liabilities=bs_df.loc['Accounts Payable']+bs_df.loc['Accrued Exp.']+bs_df.loc['Curr. Income Taxes Payable']+ocl_list
NWC=Net_current_assets - Net_Current_Liabilities
Change_nwc = NWC - NWC.shift(1)
Change_nwc = Change_nwc.fillna(0)
Change_nwc


# This second part of the code is there to compute some ratios related to this NWC. Those ratio are important to compute the future NWC of the company. 

# In[23]:


revenue_list=inc_df.loc['Revenue']
ar_list=bs_df.loc['  Total Receivables']
inv_list=bs_df.loc['Inventory']
peoca_list=bs_df.loc['Prepaid Exp.']

ap_list=bs_df.loc['Accounts Payable']
if 'Unearned Revenue, Current' in bs_df.index:
    ocl_list += bs_df.loc['Unearned Revenue, Current']
cost_list=inc_df.loc['Cost Of Goods Sold']
ae_list=bs_df.loc['Accrued Exp.']
oca_list=bs_df.loc['Other Current Assets']
taxe_list=bs_df.loc['Curr. Income Taxes Payable']
dso_list = []
for i in range(len(revenue_list)):
    if revenue_list[i] == 0:
        dso_list.append(0)
    else:
        dso_list.append(365*(ar_list[i]/revenue_list[i]))
        
dih_list = []
for i in range(len(cost_list)):
    if cost_list[i] == 0:
        dih_list.append(0)
    else:
        dih_list.append(365*(inv_list[i]/cost_list[i]))

Other_Current_Assets_list = []
for i in range(len(revenue_list)):
    if revenue_list[i] == 0:
        Other_Current_Assets_list.append(0)
    else:
        Other_Current_Assets_list.append((oca_list[i]/revenue_list[i]))

dpo_list = []
for i in range(len(cost_list)):
    if cost_list[i] == 0:
        dpo_list.append(0)
    else:
        dpo_list.append(365*(ap_list[i]/cost_list[i]))

Accrued_Liabilites_list = []
for i in range(len(revenue_list)):
    if revenue_list[i] == 0:
        Accrued_Liabilites_list.append(0)
    else:
        Accrued_Liabilites_list.append((ae_list[i]/revenue_list[i]))

Other_Current_Liabilities_list = []
for i in range(len(revenue_list)):
    if revenue_list[i] == 0:
        Other_Current_Liabilities_list.append(0)
    else:
        Other_Current_Liabilities_list.append((ocl_list[i]/revenue_list[i]))

Taxes_Payable_list = []
for i in range(len(revenue_list)):
    if revenue_list[i] == 0:
        Taxes_Payable_list.append(0)
    else:
        Taxes_Payable_list.append((taxe_list[i]/revenue_list[i]))

inv_turnover_list = []
for i in range(len(revenue_list)):
    if inv_list[i] == 0:
        inv_turnover_list.append(0)
    else:
        inv_turnover_list.append(inv_list[i]/cost_list[i])

receivable_turnover_list = []
for i in range(len(revenue_list)):
    if ar_list[i] == 0:
        receivable_turnover_list.append(0)
    else:
        receivable_turnover_list.append(ar_list[i]/revenue_list[i])

        
payable_turnover_list = []
for i in range(len(revenue_list)):
    if ap_list[i] == 0:
        payable_turnover_list.append(0)
    else:
        payable_turnover_list.append(ap_list[i]/cost_list[i])
        
prepaid_turnover_list=[]
for i in range(len(revenue_list)):
    if ap_list[i] == 0:
        prepaid_turnover_list.append(0)
    else:
        prepaid_turnover_list.append(peoca_list[i]/revenue_list[i])


# This third part provide a clear visualisation of the Change in NWC and of the additional ratios

# In[24]:


NWC_df = pd.DataFrame({'Revenue': inc_df.loc['Revenue'],
        'COGS': inc_df.loc['Cost Of Goods Sold'],
        'Currents Assets':Currents_Assets,
        'Accounts Receivable': bs_df.loc['  Total Receivables'],
        'Inventory': bs_df.loc['Inventory'],
        'Prepaid Exp.': bs_df.loc['Prepaid Exp.'],
        'Other Current Assets': bs_df.loc['Other Current Assets'],
        'Net current assets':Net_current_assets,
        'Currents_Liabilities':Currents_Liabilities,
        'Accounts Payable':bs_df.loc['Accounts Payable'],
        'Accrued Exp.':bs_df.loc['Accrued Exp.'],
        'Curr.Income Taxes Payable':bs_df.loc['Curr. Income Taxes Payable'],
        'Other Current Liabilities':ocl_list,
        'Net Current Liabilities':Net_Current_Liabilities,
        'NWC':NWC,       
        'Change nwc':Change_nwc,
       })

NWC_df = NWC_df.T.reset_index(drop=True)
NWC_df.columns = inc_df.columns
NWC_df.index=['Revenue','COGS',
                'Currents Assets','Accounts Receivable',
                'Inventory','Prepaid Exp.','Other Current Assets','Net current assets',
                'Currents Liabilities','Accounts Payable','Accrued Exp.','Curr.Income Taxes Payable',
              'Other Current Liabilities','Net Current Liabilities','NWC','Change nwc']
NWC_df


# In[25]:


metrics = pd.DataFrame({
    'Account receivables in % of Sales': receivable_turnover_list,
    'DSO': dso_list,
    'Inventory Turnover': inv_turnover_list,
    'DIH': dih_list,
    'Prepaid Expenses in % of Sales':prepaid_turnover_list,
    'Other Current Assets': Other_Current_Assets_list,
    'Account payable in % of COGS': payable_turnover_list,            
    'DPO': dpo_list,
    'Accrued Liabilites in % of Sales':Accrued_Liabilites_list,
    'Other Current Liabilities in % of Sales':Other_Current_Liabilities_list,
    'Taxes Payable in % of Sales':Taxes_Payable_list
})

metrics = metrics.T.reset_index(drop=True)
metrics.columns = inc_df.columns[:len(metrics.columns)]  # Adjust the number of columns to match inc_df
metrics.index = [
    'Account receivables in % of Sales',
    'DSO',
    'Inventory Turnover',
    'DIH',
    'Prepaid Expenses in % of Sales',
    'Other Current Assets in % of Sales',
    'Account payable in % of COGS',
    'DPO',
    'Accrued Liabilites in % of Sales',
    'Other Current Liabilities in % of Sales',
    'Taxes Payable in % of Sales'
]

metrics


# ### 2. Computation of the FCFF : visualisation and vertical analysis
# The first part of the code aims to compute the FCFF algebrically. 

# In[26]:


Gross_profit=(inc_df.loc['Revenue']-inc_df.loc['Cost Of Goods Sold'])
Opex = inc_df.loc['Selling General & Admin Exp.'] + inc_df.loc['R & D Exp.'] + inc_df.loc['Other Operating Expense/(Income)'] 
Ebit_= Gross_profit - Opex
NOPAT= Ebit_-(inc_df.loc['Income Tax Expense'])
CFO=NOPAT - Change_nwc + ca_df.loc['Depreciation & Amort., Total']


if 'Stock-Based Compensation' in ca_df.index:
    CFO += ca_df.loc['Stock-Based Compensation']

if '(Gain) Loss On Sale Of Invest.' in ca_df.index:
    CFO += ca_df.loc['(Gain) Loss On Sale Of Invest.']
    
if 'Asset Writedown & Restructuring Costs' in ca_df.index:
    CFO += ca_df.loc['Asset Writedown & Restructuring Costs']
    
if 'Other Operating Activities' in ca_df.index:
    CFO += ca_df.loc['Other Operating Activities']
FCFF=CFO- ca_df.loc['Capital Expenditure']


# This second part of the code aims to include the series into a dataframe to visualise clearly the FCFF computation. 

# In[27]:


FCFF_bis_df = pd.DataFrame({'Revenue': inc_df.loc['Revenue'],
        'COGS': inc_df.loc['Cost Of Goods Sold'],
        'Gross_profit':Gross_profit,
        'SGA': inc_df.loc['Selling General & Admin Exp.'],
        'RD': inc_df.loc['R & D Exp.'],
        'Other_Operating_Expense': inc_df.loc['Other Operating Expense/(Income)'],
        'DA': ca_df.loc['Depreciation & Amort., Total'],
        'Opex':Opex,
        'Ebit_':Ebit_,
        'Income_Tax_Expense': inc_df.loc['Income Tax Expense'],
        'Net_income':NOPAT,
        'Depreciation_and_Amortization': ca_df.loc['Depreciation & Amort., Total'],
        'Stock-BasedCompensation': ca_df.loc['Stock-Based Compensation'],
        'OtherOperatingActivities': ca_df.loc['Other Operating Activities'],
        '(Gain)LossOnSaleOfInvest.': ca_df.get('(Gain) Loss On Sale Of Invest.', 0),
        'Asset_Writedown_Restructuring_Costs': ca_df.get('Asset Writedown & Restructuring Costs', 0),
        'Change_nwc':Change_nwc,
        'CFO': CFO,
        'Capital_Expenditure':ca_df.loc['Capital Expenditure'],
        'FCFF':FCFF
       })
FCFF_bis_df=FCFF_bis_df.T
FCFF_df = FCFF_bis_df.reset_index(drop=True)
FCFF_df.columns = inc_df.columns
FCFF_df.index=['Revenue','COGS','Gross profit','SG&A','R&D','Other Operating Expense','D&A','Opex',
                'EBIT','Income tax expenses','Net Income','D&A',
                'Stock Based Compensation','Other Operating Activities',
                '(Gain) Loss On Sale Of Invest',
                'Asset Writedown Restructuring Costs',
                'Change nwc','CFO','Capital Expenditure','FCFF']

FCFF_df



# ### 3. FCFF Vertical Analysis: Computation and Visualisation

# This first part aims to compute the vertical analysis. This is done by simply dividing the different label by the revenue of the corresponding year

# In[28]:


list_variables = ['Revenue', 'COGS', 'Gross_profit', 'SGA', 'RD',
       'Other_Operating_Expense', 'DA', 'Opex', 'Ebit_', 'Income_Tax_Expense',
       'Net_income', 'Depreciation_and_Amortization',
       'Stock-BasedCompensation', 'OtherOperatingActivities',
       '(Gain)LossOnSaleOfInvest.', 'Asset_Writedown_Restructuring_Costs',
       'Change_nwc', 'CFO', 'Capital_Expenditure', 'FCFF']
variables = []

for variable in list_variables:
    x = FCFF_bis_df.loc[variable]/FCFF_bis_df.loc['Revenue']
    variables.append(x)
    


# This second part put the series into a dataframe to afford a clear visualisation

# In[29]:


FCFF_bis_vertical=pd.DataFrame(variables)
FCFF_bis_vertical.index=['Revenue', 'COGS', 'Gross_profit', 'SGA', 'RD',
       'Other_Operating_Expense', 'DA', 'Opex', 'Ebit_', 'Income_Tax_Expense',
       'Net_income', 'Depreciation_and_Amortization',
       'Stock-BasedCompensation', 'OtherOperatingActivities',
       '(Gain)LossOnSaleOfInvest.', 'Asset_Writedown_Restructuring_Costs',
       'Change_nwc', 'CFO', 'Capital_Expenditure', 'FCFF']
FCFF_vertical=FCFF_bis_vertical.reset_index(drop=True)
FCFF_vertical.columns = inc_df.columns
FCFF_vertical.index=['Revenue','COGS','Gross profit','SG&A','R&D','Other Operating Expense','D&A','Opex',
                'EBIT','Income tax expenses','Net Income','D&A',
                'Stock Based Compensation','Other Operating Activities',
                '(Gain) Loss On Sale Of Invest',
                'Asset Writedown Restructuring Costs',
                'Change nwc','CFO','Capital Expenditure','FCFF']

FCFF_vertical


# ## Statistics on past FCFF

# 3 statistics tables will be given in this part: 
# 
#     - A statistic table concerning the NWC ratios
#     - A statistic table concerning the FCFF basic analysis
#     - A statistic table concerning the FCFF vertical analysis

# ### NWC ratios statistics

# In[30]:


import statistics as stat
avg_acr = stat.mean(receivable_turnover_list)
avg_dso = stat.mean(dso_list)
avg_inv = stat.mean(inv_turnover_list)
avg_dih = stat.mean(dih_list)
avg_pre = stat.mean(prepaid_turnover_list)
avg_oca = stat.mean(Other_Current_Assets_list)
avg_acp = stat.mean(payable_turnover_list)
avg_dpo = stat.mean(dpo_list)
avg_acl = stat.mean(Accrued_Liabilites_list)
avg_ocl = stat.mean(Other_Current_Liabilities_list)
avg_taxe = stat.mean(Taxes_Payable_list)

median_acr = stat.mean(receivable_turnover_list)
median_dso = stat.median(dso_list)
median_inv = stat.median(inv_turnover_list)
median_dih = stat.median(dih_list)
median_pre = stat.median(prepaid_turnover_list)
median_oca = stat.median(Other_Current_Assets_list)
median_acp = stat.mean(payable_turnover_list)
median_dpo = stat.median(dpo_list)
median_acl = stat.median(Accrued_Liabilites_list)
median_ocl = stat.median(Other_Current_Liabilities_list)
median_taxe = stat.median(Taxes_Payable_list)

last_acr = receivable_turnover_list[-1]
last_dso = dso_list[-1]
last_inv = inv_turnover_list[-1]
last_dih = dih_list[-1]
last_pre = prepaid_turnover_list[-1]
last_oca = Other_Current_Assets_list[-1]
last_acp = payable_turnover_list[-1]
last_dpo = dpo_list[-1]
last_acl = Accrued_Liabilites_list[-1]
last_ocl = Other_Current_Liabilities_list[-1]
last_taxe = Taxes_Payable_list[-1]
stat_NWC_df = pd.DataFrame({
    'Average': [avg_acr,avg_dso, avg_inv, avg_dih,avg_pre, avg_oca, avg_acp, avg_dpo, avg_acl, avg_ocl, avg_taxe],
    'Median': [median_acr, median_dso, median_inv, median_dih, median_pre, median_oca, median_acp, median_dpo, median_acl, median_ocl, median_taxe],
    'Last Value': [last_acr, last_dso, last_inv, last_dih, last_pre, last_oca, last_acr, last_dpo, last_acl, last_ocl, last_taxe]
})
stat_NWC_df.index=['Account receivables in % of Sales','DSO','Inventory Turnover','DIH', 'Prepaid Expenses in % of Sales', 'Other Current Assets in % of Sales','Account payable in % of COGS','DPO','Accrued Liabilites in % of Sales',
                'Other Current Liabilities in % of Sales','Taxes Payable in % of Sales']
stat_NWC_df


# In[31]:


M = pd.concat([metrics, stat_NWC_df], axis=1)
M


# ### Gross Analysis statistics

# In[32]:


list_variables = ['Revenue', 'COGS', 'Gross_profit', 'SGA', 'RD',
       'Other_Operating_Expense', 'DA', 'Opex', 'Ebit_', 'Income_Tax_Expense',
       'Net_income', 'Depreciation_and_Amortization',
       'Stock-BasedCompensation', 'OtherOperatingActivities',
       '(Gain)LossOnSaleOfInvest.', 'Asset_Writedown_Restructuring_Costs',
       'Change_nwc', 'CFO', 'Capital_Expenditure', 'FCFF']
avg_variable=[]
median_variable=[]
last_variable=[]
for variables in list_variables: 
    variables_list=FCFF_bis_df.loc[variables]
    avg_variable.append(stat.mean(variables_list))
    median_variable.append(stat.median(variables_list))
    last_variable.append(variables_list[-1])
stat_FCFF_df = pd.DataFrame({
    'Average': avg_variable,
    'Median': median_variable,
    'Last Value': last_variable
}) 
stat_FCFF_df.index=['Revenue','COGS','Gross profit','SG&A','R&D','Other Operating Expense','D&A','Opex',
                'EBIT','Income tax expenses','Net Income','D&A',
                'Stock Based Compensation','Other Operating Activities',
                '(Gain) Loss On Sale Of Invest',
                'Asset Writedown Restructuring Costs',
                'Change nwc','CFO','Capital Expenditure','FCFF']
stat_FCFF_df


# ### Vertical analysis statistics

# In[33]:


list_variables = ['Revenue', 'COGS', 'Gross_profit', 'SGA', 'RD',
       'Other_Operating_Expense', 'DA', 'Opex', 'Ebit_', 'Income_Tax_Expense',
       'Net_income', 'Depreciation_and_Amortization',
       'Stock-BasedCompensation', 'OtherOperatingActivities',
       '(Gain)LossOnSaleOfInvest.', 'Asset_Writedown_Restructuring_Costs',
       'Change_nwc', 'CFO', 'Capital_Expenditure', 'FCFF']
avg_pct_variable=[]
median_pct_variable=[]
last_pct_variable=[]
for variables in list_variables: 
    variables_list=FCFF_bis_vertical.loc[variables]
    avg_pct_variable.append(stat.mean(variables_list))
    median_pct_variable.append(stat.median(variables_list))
    last_pct_variable.append(variables_list[-1])
stat_FCFF_vertical_df = pd.DataFrame({
    'Average': avg_pct_variable,
    'Median': median_pct_variable,
    'Last Value': last_pct_variable
}) 
stat_FCFF_vertical_df.index=['Revenue','COGS','Gross profit','SG&A','R&D','Other Operating Expense','D&A','Opex',
                'EBIT','Income tax expenses','Net Income','D&A',
                'Stock Based Compensation','Other Operating Activities',
                '(Gain) Loss On Sale Of Invest',
                'Asset Writedown Restructuring Costs',
                'Change nwc','CFO','Capital Expenditure','FCFF']
stat_FCFF_vertical_df


# ## Assumptions

# This part aims to create the assumptions that will support the future forecast we make. Ususally, many labels are forecasted by taking the mean or the median of the past labels value per revenue (average of the past values of the vertical analysis for each labels). However, for some other labels, such as the Revenues, the cogs and the operating expenses, more realistic and complex assumptions must be made. 

# In other words, this part is much more considered as a draft and is really specific to the company. You may want to keep the average of the past years to determine the future values for your company. This is up to you and to the qualitative analysis you have made. 
# 
# For mithra, we will take the mean as a clever assumption for the future of the company. But some other assumption, such as the one on the revenues and on the COGS are linked to the qualitative analysis that has been performed. Moreover, for some other labels such as the D&A, the operating expenses, and the Capex, the mean or the median has been performed but for some specific past years rather than the whole past years. 

# In[34]:


Assumption_revenues_list=[]
Assumption_revenues_df=pd.DataFrame(Assumption_revenues_list)
Assumption_revenues_df.index=['2023','2024','2025','2026','2027','2028']
labels_revenues=['Sales Estelle','License Estelle','Sales Donesta','License Donesta','Sales Myring','License Myring','Others']
Assumption_revenues_df['Sales Estelle']=[47.93,64.14,113.51,92.43,132.64,192.96]
Assumption_revenues_df['Sales Donesta']=[15,12.8,34.9,14.2,31.1,33.3]
Assumption_revenues_df['Sales Myring']=[7.14,8.94,14.92,10.64,11.79,12.74]
Assumption_revenues_df['Sales Other']=[0.92,1.41,2.15,3.29,5.04,7.72]
total_sales_list=[]
for year in Assumption_revenues_df.index:
    total_sales_list.append(sum(Assumption_revenues_df.T[year]))
    
Assumption_revenues_df['Total']=total_sales_list
Assumption_revenues_df=Assumption_revenues_df.T
Assumption_revenues_df


# In[42]:


choice_list=[]
draft_futurV_FCFF_df=pd.DataFrame(choice_list)

draft_futurV_FCFF_df.index=['Revenue','COGS','Gross profit','SG&A','R&D','Other Operating Expense','D&A1','Opex',
                'EBIT','Income tax expenses','Net Income','D&A2',
                'Stock Based Compensation','Other Operating Activities',
                '(Gain) Loss On Sale Of Invest',
                'Asset Writedown Restructuring Costs',
                'Change nwc','CFO','Capital Expenditure','FCFF']
year_to_forecast=['2023','2024','2025','2026','2027','2028']
reduction_RD=0.02
reduction_SGA=0.02
for year in year_to_forecast:
    draft_futurV_FCFF_df[year]=avg_pct_variable
    draft_futurV_FCFF_df[year]['SG&A']=stat.mean(FCFF_vertical.loc['SG&A',['2017-12-31','2018-12-31','2019-12-31','2021-12-31','2022-12-31']])-reduction_SGA
    draft_futurV_FCFF_df[year]['R&D']=stat.mean(FCFF_vertical.loc['R&D',['2018-12-31','2019-12-31']])-reduction_RD
    draft_futurV_FCFF_df[year]['Other Operating Expense']=stat.mean(FCFF_vertical.loc['Other Operating Expense',['2017-12-31','2018-12-31','2019-12-31','2021-12-31','2022-12-31']])
    draft_futurV_FCFF_df[year]['Opex']=sum([draft_futurV_FCFF_df[year]['SG&A'],draft_futurV_FCFF_df[year]['R&D'],draft_futurV_FCFF_df[year]['Other Operating Expense']])
    draft_futurV_FCFF_df[year]['Capital Expenditure']=stat.mean(FCFF_vertical.loc['Capital Expenditure',['2017-12-31','2018-12-31','2019-12-31','2021-12-31','2022-12-31']])
    draft_futurV_FCFF_df[year]['D&A1']=stat.mean(FCFF_bis_vertical.loc['DA',['2019-12-31','2020-12-31','2021-12-31',]]/-FCFF_vertical.loc['Capital Expenditure',['2019-12-31','2020-12-31','2021-12-31']])
    draft_futurV_FCFF_df[year]['D&A2']=stat.mean(FCFF_bis_vertical.loc['DA',['2019-12-31','2020-12-31','2021-12-31',]]/-FCFF_vertical.loc['Capital Expenditure',['2019-12-31','2020-12-31','2021-12-31']])
    reduction_RD+=0.01
    reduction_SGA+=0.02
draft_futurV_FCFF_df.loc['COGS']=[0.2874, 0.2662, 0.1834, 0.2083, 0.1627, 0.1289]
draft_futurV_FCFF_df.loc['Income tax expenses']=stat.median(np.absolute(FCFF_df.loc['Income tax expenses',['2017-12-31','2018-12-31','2019-12-31','2020-12-31','2021-12-31']]/FCFF_df.loc['EBIT',['2017-12-31','2018-12-31','2019-12-31','2020-12-31','2021-12-31']]))



draft_futurV_FCFF_df


# In[43]:


forecasted_revenue_list=Assumption_revenues_df.loc['Total']
forecasted_cost_list=draft_futurV_FCFF_df.loc['COGS']*Assumption_revenues_df.loc['Total']
forecasted_ar_list=stat_NWC_df.loc['Account receivables in % of Sales','Average']*forecasted_revenue_list
forecasted_inv_list=stat_NWC_df.loc['Inventory Turnover','Average']*forecasted_cost_list
forecasted_peoca_list=stat_NWC_df.loc['Prepaid Expenses in % of Sales','Average']*forecasted_revenue_list
forecasted_ap_list=stat_NWC_df.loc['Account payable in % of COGS','Average']*forecasted_cost_list
forecasted_ae_list=stat_NWC_df.loc['Accrued Liabilites in % of Sales','Average']*forecasted_revenue_list
forecasted_oca_list=stat_NWC_df.loc['Other Current Assets in % of Sales','Average']*forecasted_revenue_list
forecasted_taxe_list=stat_NWC_df.loc['Taxes Payable in % of Sales','Average']*forecasted_revenue_list
forecasted_ocl_list=stat_NWC_df.loc['Other Current Liabilities in % of Sales','Average']*forecasted_revenue_list
forecasted_net_current_assets=forecasted_ar_list+forecasted_inv_list+forecasted_peoca_list+forecasted_oca_list
forecasted_net_current_liabilities=forecasted_ap_list+forecasted_ae_list+forecasted_taxe_list+forecasted_ocl_list
forecasted_NWC=forecasted_net_current_assets-forecasted_net_current_liabilities
forecasted_change_NWC= forecasted_NWC - forecasted_NWC.shift(1)
forecasted_change_NWC_2023=forecasted_NWC['2023']-NWC['2022-12-31']
forecasted_change_NWC=forecasted_change_NWC.fillna(forecasted_change_NWC_2023)
forecasted_NWC_df = pd.DataFrame({'Revenue': forecasted_revenue_list,
        'COGS': forecasted_cost_list,
        'Currents Assets':Currents_Assets,
        'Accounts Receivable': forecasted_ar_list,
        'Inventory': forecasted_inv_list,
        'Prepaid Exp.': forecasted_peoca_list,
        'Other Current Assets': forecasted_oca_list,
        'Net current assets':forecasted_net_current_assets,
        'Currents Liabilities':Currents_Liabilities,
        'Accounts Payable':forecasted_ap_list,
        'Accrued Exp.':forecasted_ae_list,
        'Curr.Income Taxes Payable':forecasted_taxe_list,
        'Other Current Liabilities':forecasted_ocl_list,
        'Net Current Liabilities':forecasted_net_current_liabilities,
        'NWC':forecasted_NWC,       
        'Change nwc':forecasted_change_NWC})
forecasted_NWC_df=forecasted_NWC_df.T
forecasted_NWC_df


# In[45]:


list_variables = ['Revenue','COGS','Gross profit','SG&A','R&D','Other Operating Expense','D&A1','Opex',
                'EBIT','Income tax expenses','Net Income','D&A2',
                'Stock Based Compensation','Other Operating Activities',
                '(Gain) Loss On Sale Of Invest',
                'Asset Writedown Restructuring Costs',
                'Change nwc','CFO','Capital Expenditure','FCFF']
variables = []

for variable in list_variables:
    x = draft_futurV_FCFF_df.loc[variable]*Assumption_revenues_df.loc['Total']
    variables.append(x)
Futur_FCFF_df=pd.DataFrame(variables)
Futur_FCFF_df.columns = draft_futurV_FCFF_df.columns

Futur_FCFF_df.index=['Revenue','COGS','Gross profit','SG&A','R&D','Other Operating Expense','D&A1','Opex',
                'EBIT','Income tax expenses','NOPAT','D&A2',
                'Stock Based Compensation','Other Operating Activities',
                '(Gain) Loss On Sale Of Invest',
                'Asset Writedown Restructuring Costs',
                'Change nwc','CFO','Capital Expenditure','FCFF']
Futur_FCFF_df.loc['D&A1']=draft_futurV_FCFF_df.loc['D&A1']*Futur_FCFF_df.loc['Capital Expenditure']*-1
Futur_FCFF_df.loc['D&A2']=draft_futurV_FCFF_df.loc['D&A2']*Futur_FCFF_df.loc['Capital Expenditure']*-1
Futur_FCFF_df.loc['Change nwc']=forecasted_NWC_df.loc['Change nwc']
Futur_FCFF_df.loc['Gross profit']=Futur_FCFF_df.loc['Revenue']-Futur_FCFF_df.loc['COGS']
Futur_FCFF_df.loc['EBIT']=Futur_FCFF_df.loc['Gross profit']-Futur_FCFF_df.loc['Opex']
Futur_FCFF_df.loc['NOPAT']=Futur_FCFF_df.loc['EBIT']-Futur_FCFF_df.loc['Income tax expenses']
Futur_FCFF_df.loc['CFO']=Futur_FCFF_df.loc['NOPAT']+Futur_FCFF_df.loc['D&A2']+Futur_FCFF_df.loc['Stock Based Compensation']+Futur_FCFF_df.loc['Other Operating Activities']+Futur_FCFF_df.loc['(Gain) Loss On Sale Of Invest']+Futur_FCFF_df.loc['Asset Writedown Restructuring Costs']-Futur_FCFF_df.loc['Change nwc']
Futur_FCFF_df.loc['FCFF']=Futur_FCFF_df.loc['CFO']+Futur_FCFF_df.loc['Capital Expenditure']
Futur_FCFF_df.loc['Income tax expenses']=draft_futurV_FCFF_df.loc['Income tax expenses']*Futur_FCFF_df.loc['EBIT']

Futur_FCFF_df.index=['Revenue','COGS','Gross profit','SG&A','R&D','Other Operating Expense','D&A','Opex',
                'EBIT','Income tax expenses','NOPAT','D&A',
                'Stock Based Compensation','Other Operating Activities',
                '(Gain) Loss On Sale Of Invest',
                'Asset Writedown Restructuring Costs',
                'Change nwc','CFO','Capital Expenditure','FCFF']

Futur_FCFF_df


# In[46]:


combined_df = pd.concat([NWC_df, forecasted_NWC_df], axis=1)
combined_df


# In[47]:


Futur_FCFF_df.loc['D&A'].iloc[0]


# ## WACC Computation

# The WACC, for Weighted Average Cost of Capital, is important in financial modeling, specifically in DCF computation. Indeed, it can be seen as the cost the company face for holding its capital. 
# 
# There are 2 main kinds of stakholders that holds capital in a company: The debtholders and the shareholders who both "own" the company by a % corresponding to the amount of capital they have in the company.
# 
# The WACC can be separated in 2 different rates: the cost of debt and the cost of equity. To refer to what have been said above, the cost of equity determine the cost the company face for using the capital provided by the shareholders. On the other hand, the cost of debt correspond to the cost the company faces for using the capital offered by the debtholders. 
# 
# Logically, both cost are weighted by the corresponding amount of debt and equity to compute the Weighted Average Cost of Capital. 
# 

# ### The cost of Debt 

# #### The risk free rate 
# The first important variable that compose a cost of debt is the risk free rate. This risk free rate can be seen as a yield you get on the treasury bond. Indeed, treasury bonds are by definition risk free since a state cannot go bankruptcy. Consequently, debtholders could invest their money in a trasury bond rather than in the company and get a sure annual return equals to the annual yield you get on this treasury bond. 

# In[48]:


import yfinance as yf
import requests
from bs4 import BeautifulSoup
url = "http://www.worldgovernmentbonds.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
country='Belgium'
table = soup.find("table", {"class": "homeBondTable"})
for row in table.find_all("tr"):
    if country in row.text:
        rf = row.find("td", {"class": "w3-right-align w3-bold"}).text.strip()
        rf = (float(rf.strip("%")))/100
        break 
print ("the risk free rate for",country, "is",rf)


# #### The Default Spread
# the default rate can be seen as a premium. Indeed, debtholders are risk averse and they need to be compensated for the investment they make in the company. As a result, they will require a premium, in addition to the risk free rate, according to the rating of the company and so the solvency, liquidity and profitability of the enterprise. Note that this can be measured by the Interest Coverage ratio of the company, that measures how many times I can pay my current interest with my Earnings Before Interest and Taxes (EBIT). 

# In[49]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ratings.html"
response = requests.get(url,verify=False)

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table')

rows = table.find_all('tr')

data = []
for row in rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)
df = pd.DataFrame(data)
df.columns=(df.iloc[0])
df=df.drop(index=[0,16])
df.iloc[:, 0:1] = df.iloc[:, 0:1].astype(float)
df.iloc[:, 3] = (df.iloc[:, 3].astype(str).str.replace('%', '').astype(float))/100


# In[50]:


interest=inc_df.loc['  Net Interest Exp.']
ratio=Ebit_[-1]/interest[-1]
print ("The interest Coverage Ratio of the company is ",ratio)


# In[51]:


i=0
while i < len(df.index):
    if float(df.iloc[i, 0]) < ratio < float(df.iloc[i, 1]):
        spread = df.iloc[i, 3]
    i+=1
print("for this Interest Coverage Ratio, debtholders are requiring a default spread of", spread)


# #### The Market value of debt
# This part aims to determine what's the market value of debt. Shortly, the market value of debt is the factor that will weight the cost of debt to compute the WACC. Researchers use the market value of debt rather than the book value of debt because we want to look at the value of the debt once it has been discounting (market value of debt = discounted book value of debt). 
# 
# Note that this concept is clearly not important, and the difference between the book value of debt and the market value of debt is usually small. 

# In[52]:


tot_debt=510330000
year=2023
debts = [
    [2023, 25796],
    [2024, 22996],
    [2025, 105761],
    [2028, 301637],
    [2033, 53141],
]
total_debt = sum(debt[1] for debt in debts)
w_avg_maturity = sum((debt[0] - year) * (debt[1] / total_debt) for debt in debts)
int_exp=inc_df.loc['Interest Expense']
int_exp = abs(int_exp[-1])
cost_of_debt=rf + spread
step_1 = (1 - (1/(1+cost_of_debt)**w_avg_maturity))/cost_of_debt
step_2 = tot_debt/(1+cost_of_debt)**w_avg_maturity
mv_debt = int_exp * step_1 + step_2
taxe=draft_futurV_FCFF_df.loc['Income tax expenses'][0]
print ("the market value of debt is ", mv_debt)


# ### The cost of equity

# #### The Equity Risk Premium

# The equity risk premium can be seen as the default spread, but for the equity side. Indeed, shareholders will require a premium for investing in a company, which is by definition more risky than a treasury bond. In other words, investors will require a premium in addition to the risk free rate they would get if they invested a risk free asset (= treasury bond)
# 
# Note that this equity risk premium give you only the premium investors will require for investing in a company of a specific country. Therefore, an shareholder investing in a high-risk company will require the same premium then for investing in a low-risk company of the same country. This is why the BETA is important, it's to take into account that, for a same country, companies can have a different risk according to their sensitivity to the market. 

# In[53]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html"
response = requests.get(url,verify=False)
soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find("table", {"width": "919"})
for row in table.find_all("tr"):
    if country in row.text:
        erp = row.find_all("td")[2].text.strip()
        erp = (float(erp.strip("%")))/100
        break
print ("the erp for", country, "is", erp)


# In[54]:


your_company='MITRA.BR'
shares_outstanding=yf.Ticker(your_company).get_shares_full(start="2022-01-01", end=None)[-1]
Current_Share_Price=yf.Ticker(your_company).history(period='5y')['Close'][-1]
definitive_coef_0= 0.7839533865431152
definitive_coef_2= -0.5874647472085721
stati_mean_SMB = -0.0010829996202718756
definitive_coef_1= 0.0
stati_mean_HML= 0.00012143476287178781


# In[55]:


marketCap=shares_outstanding*Current_Share_Price
cost_of_equity =definitive_coef_0*erp+definitive_coef_1*stati_mean_HML+definitive_coef_1*stati_mean_SMB+rf
cost_of_debt = rf + spread
cap_structure = marketCap + mv_debt
w_cost_equity = marketCap / cap_structure
w_cost_debt = mv_debt / cap_structure
wacc = cost_of_equity * w_cost_equity + cost_of_debt * w_cost_debt


# In[56]:


WACC_df = pd.DataFrame({
    'Cost of equity':[cost_of_equity],
    'Beta market': definitive_coef_0,
    'Erp market': [erp],
    'Beta SMB': definitive_coef_2,
    'Erp SMB' : stati_mean_SMB,
    'Beta HML': definitive_coef_1,
    'Erp HML': stati_mean_HML,
    'Market Value of Equity': [marketCap],
    'Weight of Equity':[w_cost_equity],
    'Cost of debt':[cost_of_debt],
    'Rf': [rf],
    'Spread': [spread],
    'Taxe rate':[taxe],
    'Market Value of Debt':[mv_debt],
    'Weight of Debt':[w_cost_debt],
    'WACC':[wacc]
})

WACC_df.T.style.format("{:.3f}")


# In[57]:


i=1
DCF=[]
for FCFF in Futur_FCFF_df.loc['FCFF']:
    discount_FCFF=FCFF/((1+wacc)**i)
    DCF.append(discount_FCFF)
    i+=1
Futur_FCFF_df.loc['DCF']=DCF
sum_DCF = sum(Futur_FCFF_df.loc['DCF'])


# In[58]:


long_term_growth_rate=0.02
last_FCFF=Futur_FCFF_df.loc['FCFF'][-1]
Terminal_Value=(last_FCFF*(1+long_term_growth_rate))/(wacc-long_term_growth_rate)
Discounted_Terminal_Value=Terminal_Value/((1+wacc)**len(Futur_FCFF_df.columns))


# In[59]:


Forecasted_Enterprise_Value=Discounted_Terminal_Value+sum_DCF


# In[60]:


Discounted_Terminal_Value


# In[61]:


Forecasted_Enterprise_Value


# In[62]:


last_cash=bs_df.loc['  Total Cash & ST Investments'][-1]
Forecasted_Market_Cap=Forecasted_Enterprise_Value*(10**6)+last_cash*(10**6)-mv_debt #In million
Forecasted_Share_Price=Forecasted_Market_Cap/shares_outstanding
Forecasted_Share_Price


# In[63]:


Current_Share_Price


# In[64]:


gap=Forecasted_Share_Price/Current_Share_Price


# In[65]:


gap_in_pct=round(gap*100)


# In[66]:


print('The potential gains(loss) on', your_company, 'is', gap_in_pct, '%')


# In[67]:


sum_DCF*(10**6)


# In[68]:


DCF_df=pd.DataFrame({'Wacc': [wacc],
              'sum Dicounted Cash Flows (without Terminal Value)' :[sum_DCF*(10**6)],
              'Discounted Terminal Value': [Discounted_Terminal_Value*(10**6)], 
              'Forecasted Enterprise Value': [Forecasted_Enterprise_Value*(10**6)],
              'Market Value of Debt': [mv_debt],
              'Cash & Short Term Equivalents' : [last_cash*(10**6)],
                     'Forecasted Market Capitalization':[Forecasted_Market_Cap],
              'Forecasted Share Price': [Forecasted_Share_Price],
              'Current Share Price' : [Current_Share_Price],
              'Gap (in %)': [gap_in_pct],
             })
DCF_df=DCF_df.T
DCF_df.columns=['Data']
DCF_df


# In[69]:


fcff_2023_data= [np.random.normal(Futur_FCFF_df.loc['FCFF'][0], 3, size=1000)]
fcff_2024_data= [np.random.normal(Futur_FCFF_df.loc['FCFF'][1], 6, size=1000)]
fcff_2025_data= [np.random.normal(Futur_FCFF_df.loc['FCFF'][2], 9, size=1000)]
fcff_2026_data= [np.random.normal(Futur_FCFF_df.loc['FCFF'][3], 12, size=1000)]
fcff_2027_data= [np.random.normal(Futur_FCFF_df.loc['FCFF'][4], 15, size=1000)]
fcff_2028_data= [np.random.normal(Futur_FCFF_df.loc['FCFF'][5], 18, size=1000)]
g=[np.random.normal(long_term_growth_rate, 0.010, size=1000)]
wacc_mt=[np.random.normal(wacc, 0.010, size=1000)]
share_price_mt=[]
i=0
while i<len(fcff_2023_data[0]):
    dcf_2023_data=fcff_2023_data[0][i]/((1+wacc_mt[0][i])**1)
    dcf_2024_data=fcff_2024_data[0][i]/((1+wacc_mt[0][i])**2)
    dcf_2025_data=fcff_2025_data[0][i]/((1+wacc_mt[0][i])**3)
    dcf_2026_data=fcff_2026_data[0][i]/((1+wacc_mt[0][i])**4)
    dcf_2027_data=fcff_2027_data[0][i]/((1+wacc_mt[0][i])**5)
    dcf_2028_data=fcff_2028_data[0][i]/((1+wacc_mt[0][i])**6)
    terminal_value_mt=(fcff_2028_data[0][i]*(1+g[0][i]))/(wacc_mt[0][i]-g[0][i])
    discount_terminal_value_mt=terminal_value_mt/((1+wacc_mt[0][i])**6)
    entreprise_value_mt=sum([dcf_2023_data,dcf_2024_data,dcf_2025_data,dcf_2026_data,dcf_2027_data,dcf_2028_data,discount_terminal_value_mt])
    forecast_market_cap_mt=entreprise_value_mt*(10**6)+last_cash*(10**6)-mv_debt
    forecast_share_price_mt=forecast_market_cap_mt/shares_outstanding
    share_price_mt.append(forecast_share_price_mt)
    i+=1


# In[70]:


import matplotlib.pyplot as plt


# In[71]:


plt.hist(share_price_mt, bins=range(-10,40), align='left', rwidth=0.8, density=True)
plt.xlabel('Share prices')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.axvline(x=Current_Share_Price, color='red', linestyle='--', label='Current Share Price')
plt.legend()
plt.grid(True)

