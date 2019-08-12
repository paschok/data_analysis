import matplotlib
import pandas as pd
import numpy as np
#  visualization packages "Matplotlib" and "Seaborn"
import matplotlib.pyplot as plt
import seaborn as sns


path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(path)

# listing the data types for each column to understand the method o visualization we will be using
print(df.dtypes, '\n')

print('correlation between variables of type "int64" or "float64": \n', df.corr())

print('correlation between the following columns: bore, stroke,compression-ratio , and horsepower: \n',
      df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr())


# Positive linear relationship
# Let's find the scatterplot of "engine-size" and "price"
# Works in Jupyter Notebooks
sns.regplot(x="engine-size", y="price", data=df)
print(plt.ylim(0,))

# the correlation between 'engine-size' and 'price'
print(df[["engine-size", "price"]].corr())

# the correlation between 'highway-mpg' and 'price'
print(df[['highway-mpg', 'price']].corr())

# Weak Linear Regression
sns.regplot(x="peak-rpm", y="price", data=df)
#  the correlation between 'peak-rpm' and 'price'
print(df[['peak-rpm','price']].corr())

# Descriptive Statistical Analysis
# The describe function automatically computes basic statistics for all continuous variables. Any NaN values are automatically skipped in these statistics.
#
# This will show:
#
# the count of that variable
# the mean
# the standard deviation (std)
# the minimum value
# the IQR (Interquartile Range: 25%, 50% and 75%)
# the maximum value
print(df.describe())

# Value-counts is a good way of understanding how many units of each characteristic/variable we have.
print(df['drive-wheels'].value_counts())
print(df['drive-wheels'].value_counts().to_frame())
