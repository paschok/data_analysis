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

# figuring out the number of missing values in each column.
# In the body of the for loop the method ".value_counts()" counts the number of "True" values.
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")

# dealing with missing data : 1. Replace by mean. 2. Replace by frequency or 3. Drop the whole row
# average of the column
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:", avg_norm_loss)

# Replace "NaN" by mean value in "normalized-losses" column
df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)

# Calculate  the mean value for 'bore' column
avg_bore = df['bore'].astype('float').mean(axis=0)
print("Average of bore:", avg_bore)

# df["bore"].replace(np.nan, avg_bore, inplace=True)
df["bore"].replace(np.nan, avg_bore, inplace=True)

# calculate the mean value for "stroke" column
avg_stroke = df["stroke"].astype("float").mean(axis = 0)
print("Average of stroke:", avg_stroke)

# replace NaN by mean value in "stroke" column
df["stroke"].replace(np.nan, avg_stroke, inplace = True)
# inplace = True : changes the value. If inplace is not spacified then the ndew df is created

print('df["num-of-doors"].value_counts(): ', df['num-of-doors'].value_counts())
# ".idxmax()" method to calculate for us the most common type automatically:
df['num-of-doors'].value_counts().idxmax()

# replace the missing 'num-of-doors' values by the most frequent
df["num-of-doors"].replace(np.nan, "four", inplace=True)

# simply drop whole row with NaN in "price" column
df.dropna(subset=["price"], axis=0, inplace=True)

# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)

print(df.head())

# listing datatypes for each column
print('data types of columns: ', df.dtypes)