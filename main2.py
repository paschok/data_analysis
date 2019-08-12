import pandas as pd
import matplotlib.pylab as plt
import numpy as np

filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df = pd.read_csv(filename, names=headers)
# To see what the data set looks like, we'll use the head() method.
print(df.head())

# replace "?" to NaN, which is Python's default missing value marker,
df.replace("?", np.nan, inplace=True)
print(df.head(5))

# There are two methods to detect missing data:
#
# .isnull()
# .notnull()
missing_data = df.isnull()
# The output is a boolean value indicating whether the value that is passed into the argument
# is in fact missing data. "True" stands for missing value, while "False" stands for not missing value.
print('missing data: \n', missing_data.head(5))