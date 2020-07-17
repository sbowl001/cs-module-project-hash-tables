# given a list of records ,be able to quickly report everyone in a particular category



records = [
    ("Corey", "iOS"),
    ("Tyler", "DS"),
    ("Anika", "DS"),
    ("Jenna", "web"),
    ("Leighton", "web"),
    ("Nico", "web"),
    ("Nico", "BIRTHDAY"),
    ("Carl", "web"),
    ("Michael", "iOS"),
]
# iOS_folks = []
# web_folks = []
# for record in records:
#     if record[1] == 'iOS':
#         iOS_folks.append(record[0])
#     elif record[1] == 'web':
# return [student for student in records if student[1] == "web"]
def build_index(records):
    index = {}
# {"web": ["Jenna", "Leighton"]}
    # loop over our records
    for record in records:
        name, track = record
    ## key is track
    ### if key isn't in dictionary, add it
        if track not in index:
            index[track] = []
        index[track].append(name)
    ## value: list of names
    return index
index = build_index(records)

for track in index:
    print(track)
print(index["web"])
print(index["iOS"])
# How to handle updated records?
## Update index directly, as each record or batch of records
## Or loop over the records every once in awhile, and handle deduplication