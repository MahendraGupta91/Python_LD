import json

data = {}
data['1'] ='Mahendra' 
data['2']='Shivam'
data['3']='Jyoti'
data['4']={'1':'Mahendra','2':'Anuradha','3':'Jyoti'}
data2={'23':'kjhsahsssssgg','51':'sas'}
data.update(data2)

with open('jsonwrite3.txt', 'w') as outfile:
    data.update(data2)
    json.dump(data, outfile)