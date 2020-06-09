import json

with open('jsonwrite3.txt') as json_file:
    data = json.load(json_file)
    #data1=data['people']
    print(len(data))
    print(data)
    print('.............................................')
    data['5']='Vineet'
    data['1']='Sumit'
    print(data)
with open('jsonwrite3.txt', 'w') as outfile:
    json.dump(data, outfile)
with open('jsonwrite3.txt') as json_file:
    data = json.load(json_file)
    #data1=data['people']
    print(len(data))
    print(data)
  