#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 19:54:18 2018

@author: sarucins
"""


import pandas as pd
import numpy as np
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
from scipy import stats

Location = r'/home/sarucins/Documents/python projects/ufc_event.csv'
df = pd.read_csv(Location, encoding='utf-8-sig')
df.info()
df.head()
'''
sub_percent=(df['Sub']+df['Ko/TKO'])/(df['U-Dec']+df['M-Dec']+df['S-Dec']+df['Ko/TKO']+df['Sub']+df['Draw']+df['Overturned'])
'''
sub_percent=[]
xaxis=[]
x_count=[]
events=[]
for i in range(len(df['Event'])):
    events.append(df['Event'][i])
    x_count.append(i)
    xaxis.append(df['Event'][i])
    sub_percent.append((df['Sub'][i]+df['Ko/TKO'][i])/(df['U-Dec'][i]+df['M-Dec'][i]+df['S-Dec'][i]+df['Ko/TKO'][i]+df['Sub'][i]+df['Draw'][i]+df['Overturned'][i]))

        
fig, ax1 = plt.subplots(sharey=True,figsize=(30, 15))
ax1.set_xticklabels(xaxis, rotation=45)
plt.scatter(x_count,sub_percent)
plt.show()
slope, intercept, r_value, p_value, std_err = stats.linregress(x_count,sub_percent)
general_stats=stats.describe(sub_percent)
fig, ax1 = plt.subplots(sharey=True,figsize=(15, 15))
ax1.set_xticks([.1,.2,.3,.4,.5,.6,.7,.8,.9,1.0,1.1], minor=True)
ax1.set_xticks([.1,.2,.3,.4,.5,.6,.7,.8,.9,1.0], minor=False)
'''ax1.set_xmargin(.2)'''
plt.hist(sub_percent,bins=[.1,.2,.3,.4,.5,.6,.7,.8,.9,1.0,1.1],rwidth=.9,align="left")
plt.show()
'''df.replace(None, np.nan)
df.replace(' None]', np.nan)
df.columns.tolist()
df=df.replace('None', np.NaN)
df=df.apply(pd.to_numeric, errors='ignore')
grouped=df.groupby('weight_class')
df['reach'].max()
'''
'''gets the ages and sorts them into groups'''
'''
for k, i in enumerate(weight_classes):
    a= grouped.get_group(i)
    for index, row in a.iterrows():
        if str(row['age'])!='nan':
            age1=int(row['age'])
            age[k].append(age1)
            if str(row['title_holder'])== 'True':
                title_age[k].append(age1)
'''