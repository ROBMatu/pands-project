# **pands-project**
## Research project on the Fisher’s Iris data set.
##### Author : Robert O'Brien-Monk
---
### Synopsis

Fisher's Iris data set, comes from a study of 3 Iris varieties; Iris Setosa, Iris Versicolour, iris Virginica.
The dataset consists of the following attributes:
1. sepal length in cm 
2. sepal width in cm 
3. petal length in cm 
4. petal width in cm 
5. class (the variety of Iris)

There are 150 records, consisting of 50 records for each variety of Iris.

This project is an analysis of this dataset.

---
### analysis.py
This script carries out my analysis of the data set, where I constructed plots of the attributes of the iris' and I compared the varities to spot any variations between them.

### Assign variables with attribute labels and read in iris dataset
I started off by assigning the variables with attribute names in order to format my initial sample analysis of the iris data set.

---

### Sample analysis

I used head() to display the first 5 entries of the dataset. Then i used describe() to give me a summary of the entire dataset, with the count, mean, standard variation, minimum value, 25 & 50 & 75 percentiles and max values of the four attributes.
Then I created some subplots of each of the attributes.

---

### Histogram plots of attributes
I wanted to compare each variety of iris against each other under each of the attributes to see how they differed from eachother.
So I created four histogram plots using matplotlib.pyplot as plt. and saved each as a .png file.

---

### Scatter plots of attributes
I then created two scatter plots, one to compare the Sepal length against the sepal width, and the other to compare Petal length against Petal Width. And within those scatter plots to compare the different varieties.

---
### **software used and references**

 Visual Studio Code - version 1.74.3

 #### Iris data set resource: 
 [iris.csv](https://archive.ics.uci.edu/ml/datasets/iris)
 #### Using pandas:
  [geekforgeeks.org](https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/)
 #### Code reference and to understand project: 
 [angela1C github](https://github.com/angela1C/Programming-and-Scripting-Project-2019/blob/master/project_iris.py)
#### python matplotlib histograms & pandas: 
[nbshare.io](https://www.nbshare.io/notebook/204214467/How-to-Plot-a-Histogram-in-Python/)

[w3schools matplotlib labels](https://www.w3schools.com/python/matplotlib_labels.asp)

[w3schools matplotlib line](https://www.w3schools.com/python/matplotlib_line.asp)

[w3schools matplotlib grid](https://www.w3schools.com/python/matplotlib_grid.asp)

[matplotlib.org colours](https://matplotlib.org/stable/gallery/color/named_colors.html)

[matplotlib bins](https://stackoverflow.com/questions/33458566/how-to-choose-bins-in-matplotlib-histogram)
