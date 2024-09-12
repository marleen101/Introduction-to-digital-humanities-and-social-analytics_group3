# This python file was made so we can easily get an overview of some of the statistics of our data


import csv

# empty dictionaries to hold information
attacks = {}

# title of the header of which we want to get data
header = 'eez_country'

# opening pirate_attacks.csv and using utf-8 decoding to prevent Unicode characters from causing errors
with open("pirate_attacks.csv", "r", encoding='utf-8') as data:

    # transforming it into a dictionaries, this will allow for better maneuverability for counting
    reader = csv.DictReader(data)

    # counting instances
    for row in reader:
        attacks[row[header]] = attacks.get(row[header], 0) + 1

    # print statement to show results
    print(attacks)