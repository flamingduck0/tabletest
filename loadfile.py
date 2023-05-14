import json

file = open('static/table1.json')
data = json.load(file)


def give_data():
    return data
