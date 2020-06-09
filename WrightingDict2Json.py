import json

data = {'Eleven1': 'Millie3',
        'Mike3': 'Finn3',
        'Will5': 'Noah5'}
with open('app.json', 'w') as fp:
    json.dump(data, fp)