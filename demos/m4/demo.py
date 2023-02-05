# -*- coding: utf-8 -*-
import pandas as pd
import os

# Let's load the data for the first time
df = pd.read_pickle(os.path.join('..', 'data_frame.pickle'))

# Demo 1
# Question: How many distinct artists are there in the dataset?
# These two do the same thing, returns just artists using df.artist (not advised?) and df['artist']
# print(df.artist)
artists = df['artist']
print(artists)
print(f"Return unique artists: {pd.unique(artists)}")
print(f"Return the count of distinct artists: {len(pd.unique(artists))}")

# Demo 2
# Question: How many artworks by Francis Bacon are there?
s = df['artist'] == 'Bacon, Francis'
print(s)
# Use value_count() to get a count of the records broken out by the boolean values
print(s.value_counts())
 
# # Another way to do the same as above
artist_counts = df['artist'].value_counts()
print(artist_counts['Bacon, Francis'])


# Demo 3
# Question: What is the artwork with the biggest dimensions? Dimension here is meant to be area (width x height)
# loc by labels and iloc by position
print(df.loc[1035, 'artist'])
print(df.iloc[0, 0])
print(df.iloc[0, :])
print(df.iloc[0:2, 0:2])

# Try multiplication
# print(df['height'] * df['width'])  #Errors because there are non-numeric values 
# Do some checking to see what the values look like, you will see there are some strings in the width column
print(df['width'].sort_values().head())
print(df['width'].sort_values().tail())

# Try to convert, using to_numeric method
# print(pd.to_numeric(df['width'])) #Error because pandas cannot change a string to a number

# So we can Force NaNs 
# This basically says on error, coerce the value to NaN
print(pd.to_numeric(df['width'], errors='coerce'))
df.loc[:, 'width'] = pd.to_numeric(df['width'], errors='coerce')

pd.to_numeric(df['height'], errors='coerce')
df.loc[:, 'height'] = pd.to_numeric(df['height'],
                                    errors='coerce')

print(f"Area: {df['height'] * df['width']}")
print(f"Units: {df['units'].value_counts()}")

# Create and Assign new column for area in dataframe
area = df['height'] * df['width']
df = df.assign(area=area)
print(df.head())

# Now that we have the area, we need to find the artwork with the greatest area/dimension
print(df['area'].max())
# We can determine the index/row of the artwork with the largest dimension
print(f"Print id or index of the artwork with the largest dimension: {df['area'].idxmax()}")
print(f"Print information about the the artwork using the index: {df.loc[df['area'].idxmax(), :]}")
