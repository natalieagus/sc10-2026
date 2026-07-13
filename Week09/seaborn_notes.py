import seaborn as sns
import pandas as pd

filename = "./housing_processed.csv"
df = pd.read_csv(filename)

# HISTOGRAM
# seaborn receives pandas dataframe as an input to the histplot, and we just to specify the x value, which is the column to make our hist from
myplot = sns.histplot(x="MEDV", data=df, bins="auto") # can write a number at the bins part, or even a list of bin edges like [0,10,20,30,...]
# set the x label, write the code below
myplot.set_xlabel("Median Value in $1000")
# set the y label, write the code below
myplot.set_ylabel("Count")

# BOXPLOT
myplot = sns.boxplot(x="MEDV", data=df)
myplot.set_xlabel("Median Value in $1000")

# SCATTER PLOT
myplot = sns.scatterplot(x="RM", y="MEDV", data=df)
# can be 3D also adding colour
myplot = sns.scatterplot(x="DIS", y="MEDV", hue="RM", data=df)
