import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/iris/iris.data", header=None) #It loads the iris dataset into a pandas DataFrame called df.

df.columns = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width",
    "species"
]  #It assigns column names to the DataFrame for better readability.

df = df.dropna()  #It removes any rows with missing values from the DataFrame to ensure data quality for analysis.
print("\nShape:", df.shape)  #It shows the number of rows and columns.

print("\nColumns:", df.columns.tolist())  #It lists the column(features) names in the DataFrame.

print("\nFirst few rows:",df.head())  #It displays the first few rows of the DataFrame to give an overview of the data.

df.info()#It provides a concise summary of the DataFrame, including data types and non-null counts.

print("\nDescriptive Statistics:",df.describe()) #It generates descriptive statistics(mean(avg), standard deviation, min, max, and quartiles.) for the numerical columns in the DataFrame.

# data visualization

#scatterplot
sns.scatterplot(data =df, x="sepal_length", y="petal_length", hue="species")  #It creates a scatter plot to visualize the relationship between sepal length and petal length, colored by species.
plt.title("Sepal Length vs Petal length") 
plt.show()  

#histogram
plt.figure(figsize=(10, 6))   
sns.histplot(data=df, x="sepal_length") 
plt.show()


#boxplot
sns.boxplot(data=df)#It creates a box plot.
plt.xticks(rotation=45)  #It rotates the x-axis labels by 45 degrees for better readability.
plt.show()
