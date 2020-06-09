import json

with open('jsonwite2.txt') as json_file:
    data = json.load(json_file)
    data1=data['people']
    print(len(data1))
    print(data1[0]['name'])
    for p in data['people']:
        print(len(p))
        
        
        #print('Website: ' + p['website'])
        #print('From: ' + p['from'])
        #print('')