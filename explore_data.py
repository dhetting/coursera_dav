# -*- coding: utf-8 -*-

"""
Load and evaluate GapMinder dataset

@author: dhetting
"""

import matplotlib.pyplot as plt
import pandas as pd

# load data from csv
data = pd.read_csv('./data/gapminder.csv', low_memory=False)

# check number of records
num_records = len(data)
print('Number of records: %s' % (num_records,))

num_columns = len(data.columns)
print('Number of columns: %s' % (num_columns,))

# convert variables to numeric data types
for column in data.columns:
    try:
        data[column] = pd.to_numeric(data[column], errors='coerce')
    except ValueError:
        pass

# describe columns of interest
columns_of_interest = ('co2emissions', 'employrate', 'femaleemployrate')
for column_of_interest in columns_of_interest:
    # general summary
    print '\n'
    print(data[column_of_interest].describe())

    # create histogram plot
    fig, ax = plt.subplots()
    data.hist(column_of_interest, bins=100, ax=ax)
    fig.savefig('./images/%s_histogram.png' % (column_of_interest,))
    plt.close(fig)

print('\Complete')
