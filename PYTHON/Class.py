# Libraries used
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Python Basics
""" i = 5
j = 7
k = i + j
print(k)
# comments

print('THE TERMINAL WORKS!!!!!!!!!') """

# Intro to Numpy
""" a = [1, 2, 3, 4]
b = np.array(a)
b = np.array([1, 2])
print(b)
 """

# Two dimensional array
""" b = [1, 0, 0, 1]
a = np.array(b)
a = a.reshape(2, 2)
print(a) """

# Operations using dictionaries
""" d = dict()
d = {
    "name": "John",
    "age": 20,
    "height": "1.7m",
    "color": "black"
}

d["age"] = 21
d["height"] = "1.9m"
d["color"] = "brown"

print(d) """

# Intro to Matplotlib
""" x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
xp = np.array(x)
yp = np.array(y)

y = 2*x

plt.plot(xp, yp)
plt.show()
 """

# Intro to Pandas
""" data = {
    'x': [1, 2, 3, 4, 5],
    'y': [2, 4, 6, 8, 10]
}

df = pd.DataFrame(data)           # pd is the pandas library
print(df['x'])
print(df.loc[0])

# df= pd.read_csv("data.csv")     # Reads a file to the dataframe

a = df.to_numpy()                 # converts the dataframe to numpy
c = a.reshape(2, 5)
print(a)
print(c) """

"""Create a new repository for this python class"""
"""Use python to connect it to your mongoDB"""
