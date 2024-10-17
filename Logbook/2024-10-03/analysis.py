# This python file was made so we can easily get an overview of some of the statistics of our data

import matplotlib.pyplot as plt
import numpy as np
import csv
import scipy

# empty dictionaries to hold information
gdp = []
attacks_per_year = []
attacks = {}

# title of the header of which we want to get data
country_code = 'NGA'
header = 'date'

# opening pirate_attacks.csv and using utf-8 decoding to prevent Unicode characters from causing errors
with open("pirate_attacks.csv", "r", encoding='utf-8') as data:

    # transforming it into a dictionaries, this will allow for better maneuverability for counting
    reader = csv.DictReader(data)

    # counting instances
    for row in reader:
        if row[header][:4] == '2020':
            break
        attacks[row[header][:4]] = attacks.get(row[header][:4], 0)
        if row['nearest_country'] == country_code:
            # counting in a dict by using the year, which is notated in the first 4 digits from date
            attacks[row[header][:4]] = attacks.get(row[header][:4], 0) + 1

    # putting it into a list
    for entry in attacks:

        attacks_per_year.append(attacks[entry])


# opening country_indicators.csv and using utf-8 decoding to prevent Unicode characters from causing errors
with open("country_indicators.csv", "r", encoding='utf-8') as data:
    reader = csv.DictReader(data)

    for row in reader:
        # checking whether or not it is our country
        if row['country'] == country_code:
            # adding it into a list since the csv file is already sorted by year
            gdp.append((float(row['GDP'])))# / float(row['population'])))


# making some arrays to hold data
x = np.array(gdp)
y = np.array(attacks_per_year)

# making a scatter plot to see how the data looks in terms of possible correlations
plt.title('attacks plotted against gdp')
plt.xlabel("gdp")
plt.ylabel("attacks per year")
plt.scatter(x, y)
plt.show()

# printing the pearsons test
print('r-value: ', scipy.stats.pearsonr(x, y)[0], 'p-value: ', scipy.stats.pearsonr(x, y)[1])
