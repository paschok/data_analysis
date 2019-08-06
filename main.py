# Import pandas library
import pandas as pd
# importing display, since without it nothing does display
from IPython.display import display

# Reading the online file and assigning it to variable "df"
path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
# identical dataset but from another source
# url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'

# in this dataset we have no headers of columns and pandas automatically set the header by an integer from 0
# let's create headers list to better describe the data
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv(path, header=None)
# replacing headers
df.columns = headers
# we can drop missing values along the column "price" as follows
df.dropna(subset=["price"], axis=0)

# showing the first 10 rows using dataframe.head() method
display(df.head(10))

# printing the names of the columns of the dataframe
print(df.columns)

# saving the dataframe df as autos.csv to my local machine
df.to_csv("autos.csv", index=False)

# checking the data type of data frame "df" by .dtypes
print(df.dtypes)
# This shows the statistical summary of all numeric-typed (int, float) columns.
print(df.describe())

# describe all the columns in "df"
# df.describe(include = "all")

# selecting the columns of a data frame by indicating the name of each column
print(df[['symboling', 'make']])

print(df[['length', 'compression-ratio']].describe())
# provides a concise summary of my  DataFrame
print(df.info)



