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


def make_ordinal(num):

    base = num % 10
    if base in [0,4,5,6,7,8,9] or num in [11,12,13]:
        ext = "th"
    elif base == 1:
        ext = "st"
    elif base == 2:
        ext = "nd"
    else:
        ext = "rd"
    return str(num) + ext

# tryouts
def test_make_ordinal():
    for i in range(1,46):
        print(make_ordinal(i))

def search_the_list(list):
    for item in list:
        if "Whig" in item['Party']:
            print(item['President'] + " was a Whig.")
    for k in list[0].keys():
        print(k)

# run tryouts
if __name__ == '__main__':
    test_make_ordinal()
    presidents_list = convert_to_dict("presidents.csv")
    search_the_list(presidents_list)
    print(make_ordinal(12))
    print(make_ordinal(32))
