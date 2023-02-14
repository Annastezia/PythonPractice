my_list = [
    {
        "Country": "Russia",
        "Capital": "Moscow"
    }, {
        "Country": "USA",
        "Capital": "Washington"
    }, {
        "Country": "France",
        "Capital": "Paris"
    }, {
        "Country": "Germany",
        "Capital": "Berlin"
    }, {
        "Country": "Italy",
        "Capital": "Rome"
    }, {
        "Country": "Spain",
        "Capital": "Madrid"
    }, {
        "Country": "Sweden",
        "Capital": "Stockholm"
    }
]

import csv

fields = ['Country', 'Capital']
with open('countries.csv', 'a', newline='') as my_file:
    writer = csv.DictWriter(my_file, fields)
    writer.writerows(my_list)





