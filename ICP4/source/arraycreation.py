import numpy as np

# Creating 10*10 array
array = np.random.random((10,10))
print(array)

# Lowest and Highest Values in each row
maxRow = 1
print("Rows Maximum Values")

for maxVal in array.max(axis=1):
    print("Row%d max value is : " % maxRow, float(maxVal))
    maxRow += 1


minRow = 1
print("Rows Minimum Values")

for minVal in array.min(axis=1):
    print("Row%d min value is : " % minRow, float(minVal))
    minRow += 1


