import csv

def convert_to_dict(filename):
    # open a CSV file - note - must have column headings in top row
    datafile = open(filename, newline='')
    # create DictReader object
    reader = csv.DictReader(datafile)
    # create a regular Python list containing dicts
    dicts = list(reader)
    # close original csv file
    datafile.close()
    # return the list
    return dicts

def get_zips(source):
    zips = []
    for row in source:
        name = row["zip"]
        zips.append(zip)
    return zips

def get_id(source, name):
    for row in source:
        if name == row["zip"]:
            id = row["id"]
            id = str(id)
            return id
    return "Unknown"
