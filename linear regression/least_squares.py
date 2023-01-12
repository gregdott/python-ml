# This is just a basic thing for calculating the trend line for a linear regression
# There are tools that do that for you, but I wanted to understand the internals
# of what is actually going on when we calculate that line for a given set of data

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

df = pd.read_csv(dir_path + "/housing.data", delim_whitespace=True, header=None)
col_name = ['CRIM', 'ZN' , 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
df.columns = col_name
#df.head()

test = df[['LSTAT', 'MEDV']]
tuples = list(test.itertuples(index=False, name=None))
n = len(tuples)
sx = 0 # sum of x values
sy = 0 # sum of y values
sxs = 0 # sum of x squared values
sxy = 0 # sum of x*y values

# Loop through all sets of ['LSTAT', 'MEDV'] and do the required calculations
for i in range(n):
    sx += tuples[i][0]
    sy += tuples[i][1]
    sxs += np.power(tuples[i][0], 2)
    sxy += tuples[i][0]*tuples[i][1]

a = ((n*sxy) - (sx*sy))/((n*sxs) - (sx*sx))
b = (sy - (a*sx))/n

plt.scatter(*zip(*tuples)) # scatter plot of all the data points

# couldn't find a thing in matplot lib for just drawing a straight line from a formula
# so had to do it manually below
axes = plt.gca()
x_vals = np.array(axes.get_xlim())
y_vals = b + a * x_vals
plt.plot(x_vals, y_vals, '--') # plot of the line

plt.show()