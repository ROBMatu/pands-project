# **pands-project**
## Research project on the Fisher’s Iris data set.
##### Author : *Robert O'Brien-Monk*
---
### Synopsis

Fisher's Iris data set, comes from a study of 3 Iris varieties; Iris Setosa, Iris Versicolour, Iris Virginica. In a paper written by Ronald Fisher a statistician and biologist in 1936. And has become a common test case for data analysis.
The dataset consists of the following attributes:
1. sepal length in cm 
2. sepal width in cm 
3. petal length in cm 
4. petal width in cm 
5. class (the variety of Iris)

There are 150 records in the dataset, consisting of 50 records for each variety of Iris, displaying the measurements of the four attributes. This project is an analysis of this dataset,through the use of python programming to aid in observations of the data and display the data in plots.

---
### analysis.py
This script carries out my analysis of the data set, where I constructed plots of the attributes of the iris and I compared the varities to spot any variations between them.

### Assign variables with attribute labels and read in iris dataset
I started off by assigning the variables with attribute names in order to format my initial sample analysis of the iris data set.

---

### Sample analysis

I used head() to display the first 5 entries of the dataset. Then I used describe() to give me a summary of the entire dataset, with the count, mean, standard variation, minimum value, 25 & 50 & 75 percentiles and max values of the four attributes. To be displayed in the terminal.
I then ouputted a summary of the data set to a .txt file "iris_data_summary.txt" which gives some statisics of the different Iris attributes.
Then I created histogram subplots of each of the attributes, with the cm measurements on the x-axis and quantity on the y-axis.

---

### Histogram plots of attributes
I wanted to compare each variety of Iris against each other under each of the attributes to see how they differed from eachother.
So I created four histogram plots using matplotlib.pyplot as plt. and saved each as a .png file.

---

### Scatter plots of attributes
I then created two scatter plots, one to compare the Sepal length against the sepal width, and the other to compare Petal length against Petal Width. And within those scatter plots to compare the different varieties.

---

### Analysis of Iris dataset
Iris Setosa had the shortest but widest sepals, and it had the smallest petals by far. Iris Versicolor has the smallest sepal width but is quite close to Iris Virginica, Versicolor is the middle of the range for petal length and width. Iris Virginica has the widest distribution of sepal lengths and is the longest overall, its middle range for sepal width and has the largest petals overall.
So Setosa has the smallest sepals and petals and Virginica is the largest overall and Versicolour trends quite closely with Virginica.


---
### **software used and references**

 Visual Studio Code - version 1.74.3
 
 matplotlib and pandas modules used

 #### Iris data set resource: 
 
 [iris.csv](https://archive.ics.uci.edu/ml/datasets/iris)

 #### Using pandas:
  [geekforgeeks.org](https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/)

  [stackoverflow dataframe summary to .txt](https://stackoverflow.com/questions/75196592/how-to-append-the-dataframe-output-to-txt-file)

  [stackoverflow dataframe summary to .txt , index='name'](https://stackoverflow.com/questions/32835498/pandas-python-describe-formatting-output)

 #### Code reference and to understand project: 
 [angela1C github, for histogram subplots](https://github.com/angela1C/Programming-and-Scripting-Project-2019/blob/master/project_iris.py)

#### python matplotlib histograms & pandas: 
[nbshare.io](https://www.nbshare.io/notebook/204214467/How-to-Plot-a-Histogram-in-Python/)

[w3schools matplotlib labels](https://www.w3schools.com/python/matplotlib_labels.asp)

[w3schools matplotlib line](https://www.w3schools.com/python/matplotlib_line.asp)

[w3schools matplotlib grid](https://www.w3schools.com/python/matplotlib_grid.asp)

[matplotlib.org colours](https://matplotlib.org/stable/gallery/color/named_colors.html)

[matplotlib bins](https://stackoverflow.com/questions/33458566/how-to-choose-bins-in-matplotlib-histogram)

[stackoverflow plt.close()](https://stackoverflow.com/questions/61551562/how-to-avoid-2-plots-being-wrongly-mixed)

#### other sources
[wikipedia general Iris data set info ](https://en.wikipedia.org/wiki/Iris_flower_data_set)
