# Data Analysis
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import re

df_acq = pd.read_csv('data_acq')
df_perf = pd.read_csv('data_perform')

# Drop Missing and Unnecessary Performance Data
df_perf.dropna(axis=1, thresh=9000,inplace=True)
df_perf.dropna(axis=0,inplace=True)
df_perf = df_perf[df_perf['loanDelinquencyStatus'] != 'X']
df_perf['loanDelinquencyStatus'].value_counts()

df_perf['modificationFlag'].value_counts()
df_perf.drop('modificationFlag',axis=1,inplace=True)

# Cleaning the Acquisition Data
JPNames = ['JPMORGAN CHASE BANK, NA','JPMORGAN CHASE BANK, NATIONAL ASSOCIATION','JP MORGAN CHASE BANK, NA']
df_acq['sellerName'].replace(JPNames ,'JP MORGAN',inplace=True)
df_acq['sellerName'].replace('FIRST TENNESSEE BANK NATIONAL ASSOCIATION' ,'FIRST TENNESSEE',inplace=True)

df_acq['firstPaymentDate'] = pd.to_datetime(df_acq['firstPaymentDate'])
df_acq['originationDate'] = pd.to_datetime(df_acq['originationDate'])

# Turn Acquistion Data into DateTime DataFrame
df_time = df_acq.set_index('originationDate')
df_time.dropna(axis=1, how='any',inplace=True)
df_time = df_time['1999-01-01':'2000-09-01']

# Graphing the Acquisition Data
data = df_acq.groupby('sellerName').filter(lambda x:len(x)>100)
ax = sns.violinplot(x='sellerName',y='originalLoanToValue',data=data,cut=0)
plt.xticks(rotation=45)
plt.show()

ax = sns.violinplot(x='sellerName',y='originalInterestRate',data=data,cut=0)
plt.xticks(rotation=45)
plt.show()

ax = sns.pairplot(df_acq, vars=['originalInterestRate','originalLoanToValue'],hue='channel')
plt.show()
ax = sns.countplot(data=data, y='channel',hue='sellerName')
plt.xticks(rotation=45)
plt.show()

ax = sns.violinplot(x='occupancyStatus',y='debtToIncomeRatio',data=data,cut=0)
plt.show()

ax = sns.violinplot(x='sellerName',y='debtToIncomeRatio',data=data,cut=0)
plt.xticks(rotation=80)
plt.show()

ax = sns.pairplot(data, vars=['originalInterestRate','originalUnpaidPrincipalBalance'],hue='channel')
plt.show()

ax= sns.barplot(y='propertyGeographicalState',x='originalInterestRate',data=data,orient='h')
plt.show()


data.groupby(['sellerName','channel'])['originalInterestRate'].mean()



df_day = df_time.resample('M').mean().ffill()
df_day['originalLoanToValue'].plot()
plt.show()
