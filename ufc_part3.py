#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 20:02:29 2018

@author: sarucins
"""

import pandas as pd
import numpy as np
import matplotlib.lines as mlines
import matplotlib.pyplot as plt


weight_classes=['Women_Strawweight', 'Women_Flyweight', 'Women_Bantamweight', 'Women_Featherweight','Flyweight','Bantamweight','Featherweight','Lightweight','Welterweight','Middleweight', 'Light_Heavyweight', 'Heavyweight']
age=[[],[],[],[],[],[],[],[],[],[],[],[]]
max_age=[[],[],[],[],[],[],[],[],[],[],[],[]]
title_age=[[],[],[],[],[],[],[],[],[],[],[],[]]
Location = r'/home/sarucins/Documents/python projects/try.csv'
df = pd.read_csv(Location, encoding='utf-8-sig')
df.info()
df.head()
'''df.replace(None, np.nan)
df.replace(' None]', np.nan)'''
df.columns.tolist()
df=df.replace('None', np.NaN)
df=df.apply(pd.to_numeric, errors='ignore')
grouped=df.groupby('weight_class')
df['reach'].max()
'''gets the ages and sorts them into groups'''
for k, i in enumerate(weight_classes):
    a= grouped.get_group(i)
    for index, row in a.iterrows():
        if str(row['age'])!='nan':
            age1=int(row['age'])
            age[k].append(age1)
            if str(row['title_holder'])== 'True':
                title_age[k].append(age1)

fig, ax1 = plt.subplots(sharey=True,figsize=(15, 15))
'''xtickNames = plt.setp(ax1, xticklabels=weight_classes) plt.setp(weight_classes, rotation=45, fontsize=8)'''
plt.boxplot(age)
'''set up the wording on graphic'''
ax1.yaxis.grid(True, linestyle='-', which='major', color='grey',
               alpha=2)
ax1.set_xlabel('Division', size=12) #xlabel
ax1.set_ylabel('Age (Years)', size=12)#ylabel
ax1.set_title('Fighter Age Box plot', size=16)

''' oldest fighter special text'''     
ax1.annotate('Alex Chambers',
            xy=(1, 39.5), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')
ax1.annotate('Barb Honchak',
            xy=(2, 38.5), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')  

ax1.annotate('Marion Reneau',
            xy=(3, 40.5), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')
ax1.annotate('Tonya Evinger',
            xy=(4, 36.5), xycoords='data',
            xytext=(-30, 0), textcoords='offset points') 

ax1.annotate('Neil Seery',
            xy=(5, 38.5), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')
ax1.annotate('"Kid" Yamamoto',
            xy=(6, 41), xycoords='data',
            xytext=(-35, 0), textcoords='offset points')  

ax1.annotate('Dennis Siver',
            xy=(7, 39.5), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')
ax1.annotate('BJ Penn',
            xy=(7, 40), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')          

ax1.annotate('Reza Madadi',
            xy=(8, 40), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')
ax1.annotate('Tiequan Zhang',
            xy=(8, 40.5), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')  

ax1.annotate('Francisco Trinaldo',
            xy=(8, 41), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')
ax1.annotate('Takanori Gomi',
            xy=(8, 41.5), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')  
 
ax1.annotate('Sexyama',
            xy=(9, 42.5), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')           


ax1.annotate('Mike Pyle',
            xy=(9, 43), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')
ax1.annotate('Anderson Silva',
            xy=(10, 42.5), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')  

ax1.annotate('Lil Nog',
            xy=(11, 41.5), xycoords='data',
            xytext=(-20, 0), textcoords='offset points')
ax1.annotate('Mark Hunt',
            xy=(12, 43.5), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')
'''youngest fighter special wording'''
        
ax1.annotate('Nadia Kassem',
            xy=(1, 21), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')
ax1.annotate('Montana De La Rosa',
            xy=(2, 21.5), xycoords='data',
            xytext=(-45, 0), textcoords='offset points')  

ax1.annotate('Aspen Ladd',
            xy=(3, 21), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')
ax1.annotate('Veronica Macedo',
            xy=(3, 20.5), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')
ax1.annotate('Kelly Velasco',
            xy=(3, 20), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')
ax1.annotate('Megan Anderson',
            xy=(4, 26.5), xycoords='data',
            xytext=(-35, 0), textcoords='offset points') 

ax1.annotate('Noaki Inoue',
            xy=(5, 19.5), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')
ax1.annotate('Ricardo Ramos',
            xy=(6, 21), xycoords='data',
            xytext=(-35, 0), textcoords='offset points')  

ax1.annotate('Humberto Bandenay',
            xy=(7, 22.5), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')
ax1.annotate('Grant Dawson',
            xy=(7, 22), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')           
ax1.annotate('Mads Burnell',
            xy=(7, 21.5), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')

ax1.annotate('Super Sage',
            xy=(8, 20.5), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')
ax1.annotate('Claudio Puelles',
            xy=(8, 20), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')  

ax1.annotate('Jake Matthews',
            xy=(9, 22.5), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')

ax1.annotate('Marvin Vettori',
            xy=(10, 23.5), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')  

ax1.annotate('Elias Urbina',
            xy=(11, 23), xycoords='data',
            xytext=(-20, 0), textcoords='offset points')
ax1.annotate('Ion Cutelaba',
            xy=(11, 22.5), xycoords='data',
            xytext=(-20, 0), textcoords='offset points')
ax1.annotate('Carlos Felipe',
            xy=(12, 22), xycoords='data',
            xytext=(-30, 0), textcoords='offset points')

'''placing median values on graph'''
ax1.annotate('29',
            xy=(1, 29.5), xycoords='data',
            xytext=(-7, 0), textcoords='offset points')
ax1.annotate('29.5',
            xy=(2, 30), xycoords='data',
            xytext=(-10, 0), textcoords='offset points')  

ax1.annotate('29',
            xy=(3, 29.5), xycoords='data',
            xytext=(-7, 0), textcoords='offset points')

ax1.annotate('30',
            xy=(4, 30.5), xycoords='data',
            xytext=(-7, 0), textcoords='offset points') 

ax1.annotate('29',
            xy=(5, 29.5), xycoords='data',
            xytext=(-7, 0), textcoords='offset points')
ax1.annotate('30',
            xy=(6, 30.5), xycoords='data',
            xytext=(-7, 0), textcoords='offset points')  

ax1.annotate('29',
            xy=(7, 29.5), xycoords='data',
            xytext=(-7, 0), textcoords='offset points')

ax1.annotate('31',
            xy=(8, 31.5), xycoords='data',
            xytext=(-7, 0), textcoords='offset points')

ax1.annotate('31',
            xy=(9, 31.5), xycoords='data',
            xytext=(-7, 0), textcoords='offset points')

ax1.annotate('31',
            xy=(10, 31.5), xycoords='data',
            xytext=(-7, 0), textcoords='offset points')  

ax1.annotate('30.5',
            xy=(11, 31), xycoords='data',
            xytext=(-7, 0), textcoords='offset points')

ax1.annotate('32',
            xy=(12, 32.5), xycoords='data',
            xytext=(-7, 0), textcoords='offset points')

'''legend config'''
blue_line = mlines.Line2D([], [], color='blue', marker='o',
                          markersize=15, label='Champion')

green_line = mlines.Line2D([], [], color='green', marker='o',
                          markersize=15, label='Tony')
red_line = mlines.Line2D([], [], color='red', marker='o',
                          markersize=15, label='Oldest in Div')

yellow_line = mlines.Line2D([], [], color='yellow', marker='o',
                          markersize=15, label='Youngest in Div')
plt.legend(handles=[blue_line, green_line, red_line, yellow_line], loc="lower right", fontsize='large')

'''added champions posistion'''
ax1.set_xticklabels(weight_classes, rotation=45)
plt.plot([1,2,3,4,5,6,7,8,9,10,11,12],title_age,'bo', markersize=7)
'''ax1.scatter(weight_classes, title_win_per)
plt.plot(title_win_per,weight_classes, 'ro')'''

'''oldest age'''         
plt.plot([None,39,38,40,36,38,40,39,39,42,42,41,43], 'ro',markersize=7)
'''youngest age'''
plt.plot([None,22,22,22,27,20,22,23,21,23,24,24,23], 'yo',markersize=7)

plt.plot([None,None,None,None,None,None,None,None,34,None,None,None,None], 'go',markersize=7)
plt.show

    
    
    
'''grouped.get_group('Welterweight').describe()
grouped.groupsc
grouped.groups.keys()
grouped.describe() 
for index, row in b.iterrows():
    print(row['reach'])
    
for i in j:
    print(i)
    print(grouped.get_group(i).describe())
q.idxmax()
df.loc[]

b=grouped.get_group('Women_Strawweight')
b.set_index("age", inplace=True)

for i in range(0,12):
    b=grouped.get_group(weight_classes[i])
    b.set_index("age", inplace=True)
    v.append(b[['first_name','last_name','nickname','weight_class']].loc[p[i]])
    

'''