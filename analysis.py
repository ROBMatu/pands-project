# analysis.py
# Author: Robert O'Brien-Monk
# Outputs a summary of each variable to a single text file,
# Saves a histogram of each variable to png files,
# Outputs a scatter plot of each pair of variables.
# Performs any other analysis

import pandas
import numpy as np
import matplotlib.pyplot as plt

# read in iris dataset
iris_data_attributes = ['Sepal length','Sepal width','Petal length','Petal width', 'Class']
iris_read = pandas.read_csv("iris.csv",names = iris_data_attributes)

# head() displays first 5 rows
print("Here is an example of the dataset")
print(iris_read.head())

print("Here is a statistical summary of the dataset")
print(iris_read.describe())

# histogram subplots of each of the iris attributes 
iris_read.hist(alpha=0.8, bins=50, figsize=(12,8))
plt.show()