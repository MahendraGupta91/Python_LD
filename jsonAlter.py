import json

with open('jsonwrite2.txt') as json_file:
    data = json.load(json_file)
    for p in data['people']:
        #print(p)
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')