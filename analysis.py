# analysis.py
# Author: Robert O'Brien-Monk
# Outputs a summary of each variable to a single text file,
# Saves a histogram of each variable to png files,
# Outputs a scatter plot of each pair of variables.
# Performs any other analysis

import pandas
import numpy as np
import matplotlib.pyplot as plt

# assign variables with attribute labels and read in iris dataset
iris_data_attributes = ['Sepal length','Sepal width','Petal length','Petal width', 'Class']
iris_read = pandas.read_csv("iris.csv",names = iris_data_attributes)

# head() displays first 5 rows
print("Here is an example of the dataset")
print(iris_read.head())

# describe() showing a statistical summary of the entire dataset
print("Here is a statistical summary of the dataset")
print(iris_read.describe())

# Data summary to txt file
# the summary is converted to a string using to_string()
# then its wriien to iris_data_summary.txt
iris_summary = iris_read.describe()
with open("iris_data_summary.txt","w")as f:
    f.write("This is a summary of the Iris data set of each attribute: \n")
    f.write(iris_summary.to_string(index='name'))


# histogram subplots of each of the iris attributes 
iris_read.hist(alpha=0.8, bins=50, figsize=(12,8))
#plt.show()
#plt.savefig("iris_attributes.png")


# Font style used in plots
font= {'family':'Times','color':'purple', 'size':20}
subfont = {'family':'Times','color':'green', 'size':15}

# Sepal length histogram comparing varieties

sl_setosa= iris_read.iloc[:50,[0]]
sl_versicolor= iris_read.iloc[51:101,[0]]
sl_virginica= iris_read.iloc[101:151,[0]]

plt.hist(sl_setosa, bins=25,label='setosa',color='violet')
plt.hist(sl_versicolor, bins=25,label='versicolor',color='yellow')
plt.hist(sl_virginica, bins=25,label='virginica',color='purple')
# graph styling
plt.title("Sepal length distribution of Iris varieties", fontdict=font)
plt.xlabel("cm", fontdict=subfont)
plt.ylabel("Quantity", fontdict=subfont)
plt.legend(loc='upper right')
#plt.show()
#plt.savefig("sepal_length.png")


# Sepal Width histogram comparing varieties
sw_setosa= iris_read.iloc[:50,[1]]
sw_versicolor= iris_read.iloc[51:101,[1]]
sw_virginica= iris_read.iloc[101:151,[1]]

plt.hist(sw_setosa, bins=25,label='setosa',color='violet')
plt.hist(sw_versicolor, bins=25,label='versicolor',color='yellow')
plt.hist(sw_virginica, bins=25,label='virginica',color='purple')
# graph styling
plt.title("Sepal width distribution of Iris varieties", fontdict=font)
plt.xlabel("cm", fontdict=subfont)
plt.ylabel("Quantity", fontdict=subfont)
plt.legend(loc='upper right')
#plt.show()
#plt.savefig("sepal_width.png")


# Petal length histogram comparing varieties
pl_setosa= iris_read.iloc[:50,[2]]
pl_versicolor= iris_read.iloc[51:101,[2]]
pl_virginica= iris_read.iloc[101:151,[2]]

plt.hist(pl_setosa, bins=25,label='setosa',color='violet')
plt.hist(pl_versicolor, bins=25,label='versicolor',color='yellow')
plt.hist(pl_virginica, bins=25,label='virginica',color='purple')
# graph styling
plt.title("Petal length distribution of Iris varieties", fontdict=font)
plt.xlabel("cm", fontdict=subfont)
plt.ylabel("Quantity", fontdict=subfont)
plt.legend(loc='upper right')
#plt.show()
#plt.savefig("petal_length.png")


# petal Width histogram comparing varieties
pw_setosa= iris_read.iloc[:50,[3]]
pw_versicolor= iris_read.iloc[51:101,[3]]
pw_virginica= iris_read.iloc[101:151,[3]]

plt.hist(pw_setosa, bins=25,label='setosa',color='violet')
plt.hist(pw_versicolor, bins=25,label='versicolor',color='yellow')
plt.hist(pw_virginica, bins=25,label='virginica',color='purple')
# graph styling
plt.title("Petal width distribution of Iris varieties", fontdict=font)
plt.xlabel("cm", fontdict=subfont)
plt.ylabel("Quantity", fontdict=subfont)
plt.legend(loc='upper right')
#plt.show()
#plt.savefig("petal_width.png")

# Sepal length vs Sepal width scatter plot

plt.scatter(sl_setosa,sw_setosa,label='setosa', color='violet')
plt.scatter(sl_versicolor,sw_versicolor,label='versicolor', color='yellow')
plt.scatter(sl_virginica,sw_virginica,label='virginica', color='purple')
plt.title("Sepal length vs Sepal width",fontdict=font)
plt.xlabel("Sepal length cm",fontdict=subfont)
plt.ylabel("Sepal width cm",fontdict=subfont)
#plt.show()
#plt.savefig("sepal_length_vs_sepal_width.png")


# Petal Length vs Petal width
plt.scatter(pl_setosa,pw_setosa,label='setosa', color='violet')
plt.scatter(pl_versicolor,pw_versicolor,label='versicolor', color='yellow')
plt.scatter(pl_virginica,pw_virginica,label='virginica', color='purple')
plt.title("Petal length vs Petal width",fontdict=font)
plt.xlabel("Petal length cm",fontdict=subfont)
plt.ylabel("Petal width cm",fontdict=subfont)
#plt.show()
#plt.savefig("petal_length_vs_petal_width.png")