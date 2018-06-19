import numpy as numpy
import matplotlib.pyplot as plot

# Loading the given values into the x and y arrays
x = numpy.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = numpy.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

# Calculating Mean of x and y
meanOfX = numpy.mean(x)
meanOfY = numpy.mean(y)

# Calculating the Slope using the numpy module
slope = numpy.sum((x-meanOfX) * (y-meanOfY)) / numpy.sum(numpy.power(x-meanOfX, 2))

# Calculating the Intercept
intercept = meanOfY-(slope * meanOfX)

# Data generated
data = (slope * x) + intercept
print(data)

#plot the x and y
plot.plot(x, y)

#plot of x and data
plot.plot(x, data)

plot.show()
