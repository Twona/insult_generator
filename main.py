#!/usr/bin/env python3

import csv
from random import randrange

def Insult_Gen(filepath):
    x = []
    y = []
    z = []

    # Open CSV file
    with open(filepath, 'r') as csvfile:
        readobject = csv.DictReader(csvfile)
        run = True

        # Loop through headers
        for row in readobject:
                x.append(row['begin'])
                y.append(row['begin'])
                z.append(row['end'])

        # Remove empty entries
        while '' in x:
            x.remove('')
        while '' in y:
            y.remove('')

        # Set up repeat and pick three words
        while run == True:
            x1 = x[randrange(1, len(x))]
            y2 = y[randrange(1, len(y))]
            z3 = z[randrange(1, len(z))]

            # Check for duplicate
            while x1 == y2:
                y2 = y[randrange(1, len(y))]

            print('Your insult is: {} {} {}'.format(x1, y2, z3))

            runcheck = input("Run again? (y/n): ")
            if runcheck == "y":
                run = True
            else:
                run = False


Insult_Gen('csvfile\insult_list.csv')
