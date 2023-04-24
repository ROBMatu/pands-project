# **pands-project**
## Research project on the Fisher’s Iris data set.
##### Author : *Robert O'Brien-Monk*
---
## Synopsis

Fisher's Iris data set, comes from a study of 3 Iris varieties; Iris Setosa, Iris Versicolour and Iris Virginica. In a paper written by Ronald Fisher, a Statistician and Biologist in 1936. It has become a common test case for data analysis. The datset is available from [UCI Machine learning repository](https://archive.ics.uci.edu/ml/datasets/iris) as a csv file.

The dataset consists of the following attributes:
1. Sepal Length in cm 
2. Sepal Width in cm 
3. Petal Length in cm 
4. Petal Width in cm 
5. Class (the variety of Iris)

There are 150 records in the dataset, consisting of 50 records for each variety of Iris, displaying the measurements of the four attributes in each row. This project is an analysis of this dataset,through the use of python programming, to aid in observations of the data and to display the data in plots. My analyis of the dataset is found below along with a description of the script used for the analyis.

---
## analysis.py
This script carries out my analysis of the data set, where I constructed plots of the attributes of the Iris's, and I also compared the varities to spot any variations between them.

 To run it dowload iris.csv and analysis.py to vscode, then run, python ./analysis.py ,in the terminal. It will produce some data summaries in the terminal, and iris_data_summary.txt containing a summary of the Iris attributes, and six png files of the plots constructed in analysis.py.

---

### Assign attribute labels and read in iris dataset
I started off by assigning the variables with attribute names in order to format my initial sample analysis of the iris data set. The pandas module was very useful for doing this and for doing sample analysis and plots.

---

### Sample analysis

I used the pandas functions, head() to display the first 5 entries of the dataset and describe() to give me a summary of the entire dataset, with the count, mean, standard variation, minimum value, 25 & 50 & 75 percentiles and max values of the four attributes. Which are displayed in the terminal. I then added a data summary, which was written to a .txt file. Then I created histogram subplots of each of the attributes, with the cm measurements on the x-axis and quantity on the y-axis.

---

### iris_data_summary.txt
Using the pandas function describe() again, I ouputted a summary of the data set to a .txt file "iris_data_summary.txt" which gives some statisics of the different Iris attributes. I had to use pandas to_string() to convert the dataframe in the variable iris_summary to a string, so write() could write it to the txt file.

---

### Histogram plots of attributes
I wanted to compare each variety of Iris against each other under each of the attributes to see how they differed from eachother.
So I created four histogram plots using matplotlib.pyplot as plt. and saved each as a .png file. It was useful to compare the varieties this way as I could see the range of values more clearly than in the csv file.

---

### Scatter plots of attributes
I then created two scatter plots, one to compare the Sepal length against the sepal width, and the other to compare Petal length against Petal Width. And within those scatter plots to compare the different varieties. These were useful to see the comparisons of the overall main attributes of the dataset sepals and petals.

---

## Analysis of Iris dataset
Iris Setosa had the shortest but widest sepals, and it had the smallest petals by far. Iris Versicolor has the smallest sepal width but is quite close to Iris Virginica, Versicolor is the middle of the range for petal length and width. Iris Virginica has the widest distribution of sepal lengths and is the longest overall, its middle range for sepal width and has the largest petals overall.
So Setosa has the smallest sepals and petals and Virginica is the largest overall and Versicolour trends quite closely with Virginica.

I also found the python module's, matplotlib and pandas, very useful for making the data more understanable and aiding in analysis to show these comparisions between the Iris varieties.


---
## software used and references

 Visual Studio Code - version 1.74.3
 
 matplotlib and pandas modules used

 #### Iris data set resource: 
 
 [iris.csv](https://archive.ics.uci.edu/ml/datasets/iris)

 #### Python matplotlib histograms & using pandas:
  [geekforgeeks.org](https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/)

  [stackoverflow dataframe summary to .txt](https://stackoverflow.com/questions/75196592/how-to-append-the-dataframe-output-to-txt-file)

  [stackoverflow dataframe summary to .txt , index='name'](https://stackoverflow.com/questions/32835498/pandas-python-describe-formatting-output)

[nbshare.io](https://www.nbshare.io/notebook/204214467/How-to-Plot-a-Histogram-in-Python/)

[w3schools matplotlib labels](https://www.w3schools.com/python/matplotlib_labels.asp)

[w3schools matplotlib line](https://www.w3schools.com/python/matplotlib_line.asp)

[w3schools matplotlib grid](https://www.w3schools.com/python/matplotlib_grid.asp)

[matplotlib.org colours](https://matplotlib.org/stable/gallery/color/named_colors.html)

[matplotlib bins](https://stackoverflow.com/questions/33458566/how-to-choose-bins-in-matplotlib-histogram)

[stackoverflow plt.close()](https://stackoverflow.com/questions/61551562/how-to-avoid-2-plots-being-wrongly-mixed)

#### Code reference and to understand project: 
 [angela1C github, expectations](https://github.com/angela1C/Programming-and-Scripting-Project-2019/blob/master/project_iris.py)

 [pydata.org, dataframe.hist()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html)

 #### other sources
[wikipedia general Iris data set info ](https://en.wikipedia.org/wiki/Iris_flower_data_set)
