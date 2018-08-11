#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 19:55:11 2018

@author: sarucins
"""

import json
import pprint
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as mlines

ufc_data= json.load(open('fighters_raw_data.json'))
weight_classes=['Women_Strawweight', 'Women_Flyweight', 'Women_Bantamweight', 'Women_Featherweight','Flyweight','Bantamweight','Featherweight','Lightweight','Welterweight','Middleweight', 'Light_Heavyweight', 'Heavyweight']

win_percentage=[[],[],[],[],[],[],[],[],[],[],[],[]]
title_win_per=[[],[],[],[],[],[],[],[],[],[],[],[]]
'''
for i in ufc_data:
    if i['weight_class'] not in weight_classes and i['weight_class'] != None:
        weight_classes.append(i['weight_class'])
        win_percentage.append([])
welter_data=[]
'''
for i in ufc_data:
    if i['fighter_status']=='Active' and i['first_name'] !='.' and i['weight_class'] != None and i['losses'] != None:
        for j in range(0,len(weight_classes)):
            if i['weight_class']== weight_classes[j]:
                losses=int(i['losses'])
                wins=int(i['wins'])
                if i['draws'] == None:
                    draw=0
                else:
                    draw= int(i['draws'])
                if losses==0:
                    win_percentage[j].append(1)
                else:
                    win_percentage[j].append(wins/(wins+losses+draw))
                if i['title_holder'] is True:
                    title_win_per[j].append(wins/(wins+losses+draw))

  

fig, ax1 = plt.subplots(sharey=True,figsize=(12, 10))
'''xtickNames = plt.setp(ax1, xticklabels=weight_classes) plt.setp(weight_classes, rotation=45, fontsize=8)'''
plt.boxplot(win_percentage)

ax1.yaxis.grid(True, linestyle='-', which='major', color='grey',
               alpha=2)
ax1.set_xlabel('Division', size=12) #xlabel
ax1.set_ylabel('Win Percentage %', size=12)#ylabel
ax1.set_title('Win Percentage Box plot', size=16)

blue_line = mlines.Line2D([], [], color='red', marker='o',
                          markersize=15, label='Champ')

green_line = mlines.Line2D([], [], color='green', marker='o',
                          markersize=15, label='Tony')
plt.legend(handles=[blue_line, green_line], loc="lower right", fontsize='large')

ax1.set_xticklabels(weight_classes, rotation=45)
plt.plot([1,2,3,4,5,6,7,8,9,10,11,12],title_win_per,'ro', markersize=7)
'''ax1.scatter(weight_classes, title_win_per)
plt.plot(title_win_per,weight_classes, 'ro')'''
plt.plot([None,None,None,None,None,None,None,None,.8846,None,None,None,None], 'go',markersize=7)
plt.show
   

  

division_age=[[],[],[],[],[],[],[],[],[],[],[],[]]
title_age=[[],[],[],[],[],[],[],[],[],[],[],[]]
er_data=[]

for i in ufc_data:
    if i['fighter_status']=='Active' and i['first_name'] !='.' and i['weight_class'] != None and i['losses'] != None:
        for j in range(0,len(weight_classes)):
            if i['weight_class']== weight_classes[j]:
                losses=int(i['losses'])
                wins=int(i['wins'])
                if i['draws'] == None:
                    draw=0
                else:
                    draw= int(i['draws'])
                if losses==0:
                    win_percentage[j].append(1)
                else:
                    win_percentage[j].append(wins/(wins+losses+draw))
                if i['title_holder'] is True:
                    title_win_per[j].append(wins/(wins+losses+draw))        
