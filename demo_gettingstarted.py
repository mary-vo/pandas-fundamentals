import numpy as np
import pandas as pd

# Return an array of random values
my_numpy_array = np.random.rand(3)
print(type(my_numpy_array))
print(my_numpy_array[0])

# Return a series using existing array
my_series = pd.Series(my_numpy_array)
print(my_series[0])

# Change the index in series
my_series = pd.Series(my_numpy_array, index=["First", "Second", "Third"])
print(my_series)

# We can index using labels and integer
print(my_series[0] == my_series["First"])

# Print the index for Series
print(my_series.index)

# Creating random array with two columns
array_2d = np.random.rand(3,2)
print(array_2d)
# Pass two indexes to retrive specific element
print(array_2d[0,1]) #[row,column]

# Create dataframe
df = pd.DataFrame(array_2d)
# print(df[0,1]) #Error, not how we index dataframes
# Create labels for columns similiarly to rows (index) but instead we specify columns property
df.columns = ["First","Second"]
df.index = ["First", "Second", "Third"]
print(df)
# Return second column of Dataframe
print(df["Second"])