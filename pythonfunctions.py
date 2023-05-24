import json

file = open('static/table1.json')
data = json.load(file)


def give_data():
    return data

def fencers(sheet):
    """
    returns a list of all the fencers in a sheet
    """
    return list(sheet["fencers"].keys())


# TODO: test each function,
# TODO: make a function to pass a dict with keys cell, row and value hits for that row against that col
# TODO: figure out the refreshment of the page