import json

file = open('static/table1.json')
data = json.load(file)


def fencer_bouts(pool_json, fencer1_name, fencer2_name=None):
    index_count = 0
    bout_matches = []
    bout_data = pool_json['bouts']
    if fencer2_name != fencer1_name:
        for bout in bout_data:
            fencer1_exists = (fencer1_name in bout['fencer1']) or (fencer1_name in bout['fencer2'])

            if fencer2_name:
                fencer2_exists = (fencer2_name in bout['fencer1']) or (fencer2_name in bout['fencer2'])
            else:
                fencer2_exists = True

            if fencer1_exists and fencer2_exists:
                bout_matches.append(index_count)

            index_count += 1

    return bout_matches


def fencers():
    """
    returns a list of all the fencers in a sheet in correct order
    """
    return list(data["fencers"].keys())


# return data as list of lists

def hits(sheet, attacker, victim):
    bout = fencer_bouts(sheet, attacker, victim)
    points = 0
    if len(bout) != 0:
        match = sheet["bouts"][bout[0]]
        points = 0
        for hit in match['hits']:
            if hit[attacker]['type'] != "no_hit":
                points += 1
    return points


def table_as_list():
    fencer_list = fencers()
    table = []
    for row in fencer_list:
        value = []
        for col in fencer_list:
            if row != col:
                hit = hits(data, row, col)
                value.append(hit)
            else:
                value.append("")
        table.append(value)
    return table