import json

file = open('static/table1.json')
data = json.load(file)


def remove_person(name, sheet):
    """
    remove_person(name,sheet)
    name as a string
    """
    sheet["fencers"].pop(name)
    bouts = find_bouts(name, sheet)
    for x in bouts:
        sheet("bouts").pop(x)


def fencers(sheet):
    """
    returns a list of all the fencers in a sheet
    """
    return list(sheet["fencers"].keys())


def save():
    json_object = json.dumps(data, indent=4)
    with open("new.json", "w") as outfile:
        outfile.write(json_object)


def find_bouts(name, sheet):
    """
    finds all bouts someone is in as a list
    """
    output = []
    if name in fencers(sheet):
        count = 0
        for bouts in sheet["bouts"]:
            if name in bouts:
                output.append(count)
            count += 1
    return output


def select_hits(name1, name2, sheet):
    match = []
    bouts = find_bouts(name1, sheet)
    # list of bouts opponent has been in
    for x in bouts:
        if name2 in sheet["bouts"][x]:
            try:
                match = sheet["bouts"][x]["hits"]
            finally:
                pass
    return match


def add_person(name, sheet):
    """
    adds a person to the sheet
    adds their bouts to the sheet
    """
    people = fencers(sheet)
    # sets the variable people to the list of existing fencers
    name_info = {
                    "victories": 0,
                    "hits_given": 0,
                    "hits_received": 0,
                    "indicator": 0
                },
    sheet["fencers"][name] = name_info
    # adds name into fencers

    for x in people:
        # all the people that are there need a match

        # combined = combine(name,x)
        # makes the a list in the match

        structure = {
            "fencer1": name,
            "fencer2": x,
            "hits": []
        }
        sheet["bouts"].append(structure)


def howmanyhits(name, opponent, sheet):
    hits = 0
    match = select_hits(name, opponent, sheet)
    for i in match:
        if match[i][name]["type"] != "no_hit":
            hits += 1
    return hits


def addhit(sheet, location, timeleft, p1, p1_type, p1_target, p2, p2_type, p2_target):
    match = select_hits(p1, p2, sheet)
    hit = {
        "location": location,
        "time_left": timeleft,
        p1: {"type": p1_type, "target": p1_target},
        p2: {"type": p2_type, "target": p2_target}
    }
    match.append(hit)


def give_data():
    return data


# TODO: test each function,
# TODO: make a function to pass a dict with keys cell, row and value hits for that row against that col
# TODO: figure out the refreshment of the page