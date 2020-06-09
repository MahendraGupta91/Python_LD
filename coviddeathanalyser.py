# -*- coding: utf-8 -*-
"""
Created on Sat May 23 17:50:28 2020

@author: Mahendra
"""
import json
import array
import numpy as np
with open('deaths_recoveries.json') as dict_readerold:
        olddata=json.load(dict_readerold)
        patient=olddata["deaths_recoveries"]
        print(len(patient))
        print(patient[2])

age_count_death=[0]*100
age_count_recovered=[0]*100

for i in patient:
    if i["agebracket"]=='':
        {
                #print("")
                }
    elif i["patientstatus"]=='Deceased': 
        age=int(i["agebracket"])
        age_count_death[age]+=1
    elif i["patientstatus"]=='Recovered': 
        age=int(i["agebracket"])
        age_count_recovered[age]+=1
        
#print(np.histogram(age_count))
#print(age_count.np.std())       


            