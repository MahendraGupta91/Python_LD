
newData ={}
newData['1'] ='Mahendra1' 
newData['7']='Shivani'
newData['8']='Jyotima'
newData['4']={'1':'Mahendra','2':'Anuradha','3':'Jyoti'}
with open('jsonwrite3.txt','w') as json_file:
    data = json.load(json_file)
    print(len(data))
    print(data)
    data.update(newData)
    print(len(data))
    print(data)