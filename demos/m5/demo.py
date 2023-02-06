""" In this demo:
- Iterative over artist groups
- Find the data of the first acquisition for each artist
- Fill some missing values
"""

# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import os

df = pd.read_pickle(os.path.join('..', 'data_frame.pickle'))

# ITERATION - Iterate over artist groups
# Pick a small sample size to work from, this will return row index from 49980-50019 (slicing) and all columns
small_df = df.iloc[49980:50019, :].copy()
# Use groupby method to group by a specific column (i.e. artist)
grouped = small_df.groupby('artist')
# print(type(grouped))
# print(f"Printing grouped: {grouped.head()}")

for name, group_df in grouped:
    print(name)
    print(f"Printing group_df: {group_df}")
    break

# Aggregate - Find the first/min acquistion date for each artist
# Mins
for name, group_df in small_df.groupby('artist'): 
    min_year = group_df['acquisitionYear'].min()
    print("{}: {}".format(name, min_year))

# Transform
# Equivalent of editing by hand:
# Make a case when there is no data to infer
print(small_df)
small_df.loc[[11838, 16441], 'medium'] = np.nan
print(f"Printing small_df after change: {small_df}")


### I have no idea what he's doing in this portion
def fill_values(series):
    values_counted = series.value_counts()
    if values_counted.empty:
        return series
    most_frequent = values_counted.index[0]
    new_medium = series.fillna(most_frequent)
    return new_medium

def transform_df(source_df):
    group_dfs = []  
    for name, group_df in source_df.groupby('artist'):
        filled_df = group_df.copy()
        filled_df.loc[:, 'medium'] = fill_values(group_df['medium'])
        group_dfs.append(filled_df)
    
    new_df = pd.concat(group_dfs)
    return new_df

# Now check the result
filled_df = transform_df(small_df)
print(f"Printing filled_df: {filled_df}")

# BUILT-INS
# Transform
# We can do the following to transform medium field to fill the nan values
grouped_mediums = small_df.groupby('artist')['medium']
small_df.loc[:, 'medium'] = grouped_mediums.transform(fill_values)

# Aggreations
grouped_acq_year = df.groupby('artist')['acquisitionYear']
min_acquisition_years = grouped_acq_year.agg(np.min)
# or do the following
min_acquisition_years = grouped_acq_year.min()

# Min
df.groupby('artist').agg(np.min)
# This is python's built in min function
df.groupby('artist').min()

# Filter
# Look for duplicated titles
grouped_titles = df.groupby('title')
# title_counts = grouped_titles.size().sort_values(ascending=False)
# Why is the condition using x.index? That is the row not the title, right?
condition = lambda x: len(x.index) > 1
dup_titles_df = grouped_titles.filter(condition)
# dup_titles_df.sort_values('title', inplace=True)
    