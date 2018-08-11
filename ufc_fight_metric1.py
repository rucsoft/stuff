#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:43:37 2018

@author: sarucins
"""

import json
import pprint
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as mlines
import requests
import lxml.html
import pandas as pd
import csv
'''
PART1
'''
'''
this part of the program builds the first part of the data set pulls all 
fights from their overview page
'''
main_url='http://www.fightmetric.com/statistics/events/completed?page=all'
page = requests.get(main_url)
tree= lxml.html.fromstring(page.content)
branch_item1= tree.xpath("//i/span")
branch_item2=tree.xpath("//i/a")
branch_item3= tree.xpath("//td[@class='b-statistics__table-col b-statistics__table-col_style_big-top-padding']")
branch_item4= tree.xpath("//i/a/@href")
'''
data cleanse
''' 
   
data_1=[]
for i in range(0,len(branch_item1)):
    data_1.append([])
    data_1[i].append(branch_item1[i].text_content())
    data_1[i].append(branch_item2[i].text_content())
    data_1[i].append(branch_item3[i].text_content())
    data_1[i].append(branch_item4[i])
    
for i in data_1:
    i[0]=i[0].replace('\n                          ','')
    i[0]=i[0].replace('\n                        ','')
    i[1]=i[1].replace('\n                          ','')
    i[1]=i[1].replace('\n                        ','')
    i[2]=i[2].replace('\n                    ','')
    i[2]=i[2].replace('\n                  ','')
    i[2]=i[2].replace(",","")
    i[3]=i[3].replace('\n','')
    i[3]=i[3].replace(' ','')

   
'''
Part2
'''
'''
this part of the program uses info from data_1 to get stats from item3 data point
This is going to just pull victory methods
'''

del data_1[0]

for i in data_1:
    ko=0
    sub=0
    u_dec=0
    m_dec=0
    s_dec=0
    u_dec=0
    overturn=0
    draw=0
    page = requests.get(i[3])
    tree= lxml.html.fromstring(page.content)
    branch_item1= tree.xpath("//td/p[@class='b-fight-details__table-text']")
    for j in branch_item1:
        g=j.text_content()
        g=g.replace('\n','')
        g=g.replace(' ','')
        if g== 'win':
            tick=1
        if g== 'draw':
            tick=2
        if g== 'S-DEC':
            if tick ==1:
                s_dec=s_dec+1
                tick=0
            if tick==2:
                tick=0
                draw=draw+1
        if g== 'U-DEC':
            if tick ==1:
                tick=0
                u_dec=u_dec+1
        if g== 'M-DEC':
            if tick ==1:
                tick=0
                m_dec=m_dec+1
            if tick==2:
                tick=0
                draw=draw+1
        if g== 'Overturned':
            tick=0
            overturn=overturn+1
        if g== 'KO/TKO':
            tick=0
            ko=ko+1
        if g== 'SUB':
            tick=0
            sub=sub+1
        if g=='Other':
            if tick==2:
                tick=0
                draw=draw+1
    i.append(u_dec)
    i.append(m_dec)
    i.append(s_dec)
    i.append(ko)
    i.append(sub)
    i.append(draw)
    i.append(overturn)
        
           
    
dict_begining=['Date','Event','Location','Website','U-Dec','M-Dec','S-Dec','Ko/TKO','Sub','Draw','Overturned']

'''
reverse string to get proper order then save it
'''
data_1.append(dict_begining)
data_1.reverse()
for i in data_1:
    q=i[0]+','+i[1]+','+i[2]+','+i[3]+','+str(i[4])+','+str(i[5])+','+str(i[6])+','+str(i[7])+','+str(i[8])+','+str(i[9])+','+str(i[10])
    f=open("ufc_event.csv", "a+")
    f.write(q+'\n')
    f.close 


'''
k=[]
for i in data_1:
    top=i[8]+i[7]
    bottom=i[4]+i[5]+i[6]+i[9]+i[10]
    if bottom==0:
        k.append(1)
    else:
        ratio=(top)/(top+bottom)
        k.append(ratio)
'''
'''
PART2
'''    
'''
this part of the program uses info from data_1 to get stats from item3 data point
'''


'''notes and efforts nothing important'''
'''



next three lines just gets fighers
page = requests.get('http://www.fightmetric.com/event-details/1a49e0670dfaca31')
tree= lxml.html.fromstring(page.content)
branch_item1= tree.xpath("//td/p/a[@class='b-link b-link_style_black']")

writing and saving to str
    q=str(i[0])+','+str(i[1])+','+str(i[2])+','+str(i[3])+','+str(i[4])+','+str(i[5])+','+str(i[6])+','+str(i[7])+','+str(i[8])+','+str(i[9])+','+str(i[10])+','+str(i[11])+','+str(i[12])+','+str(i[13])+','+str(i[14])
    f=open("try.csv", "a+")
    f.write(q+'\n')
    f.close
    
for i in branch_item1:
    if 'KO/TKO' in i.text_content():
        print('hi')

data_1=data_1.reverse()
branch_items= tree.xpath("//i/a/@href")
branch_items= tree.xpath("//td[@class='b-statistics__table-col b-statistics__table-col_style_big-top-padding']")
i[0]=i[0].replace('\n                          ','')
i[0]=i[0].replace('\n                        ','')



branch_item1[1].text_content()

>>> import simplejson
>>> f = open('output.txt', 'w')
>>> simplejson.dump([1,2,3,4], f)
>>> f.close()
'''