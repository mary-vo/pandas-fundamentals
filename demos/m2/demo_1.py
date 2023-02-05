# -*- coding: utf-8 -*-
import pandas as pd
import os

# Where our data lives
# The '..' traverses up one folder
CSV_PATH = os.path.join('..', 'collection-master',
                        'artwork_data.csv')
print(CSV_PATH)

# Read just 5 rows to see what's there
df = pd.read_csv(CSV_PATH, nrows=5)
print(df)

# Take a specific column from the csv file as an Index
df = pd.read_csv(CSV_PATH, nrows=5,
                 index_col='id')

# Limit columns
df = pd.read_csv(CSV_PATH, nrows=5,
                 index_col='id',
                 usecols=['id', 'artist']) # can also pass [0,2]

# All columns that we need
COLS_TO_USE = ['id', 'artist',
               'title', 'medium', 'year',
               'acquisitionYear', 'height',
               'width', 'units']

#  Update df with new COLS_TO_USE
df = pd.read_csv(CSV_PATH,
                 usecols=COLS_TO_USE,
                 index_col='id')
print(df)

# Save for later
df.to_pickle(os.path.join('..', 'data_frame.pickle'))



