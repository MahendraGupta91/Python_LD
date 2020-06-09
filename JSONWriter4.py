import json

data = {}
data['1'] ='Mahendra' 
data['2']='Shivam'
data['3']='Jyoti'
data['4']={'1':'Mahendra','2':'Anuradha','3':'Jyoti'}
    

with open('jsonwriteJSon.json', 'w') as outfile:
    json.dump(data, outfile)