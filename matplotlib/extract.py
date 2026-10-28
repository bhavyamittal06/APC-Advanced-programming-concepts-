import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ds.csv")

# Line Plot
plt.plot(df["SepalLengthCm"], label="Sepal Length")
plt.plot(df["PetalLengthCm"], label="Petal Length")
plt.legend()
plt.show()

# Scatter Plot
plt.scatter(df["SepalLengthCm"], df["PetalLengthCm"])
plt.show()

# Bar Chart
plt.bar(df.index, df["SepalLengthCm"])
plt.show()

# Histogram
plt.hist(df["PetalLengthCm"], bins=8)
plt.show()

# Pie Chart
df["Species"].value_counts().plot.pie(autopct="%1.1f%%")
plt.show()