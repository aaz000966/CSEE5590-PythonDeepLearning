import numpy as np

myArray = np.random.randint(1, 20, 15)
print(myArray, '\n')
print("****************\n")

a2 = myArray.reshape((3, 5))

print(a2, '\n')
print("****************\n")

b = a2

b[np.arange(len(a2)), a2.argmax(1)] = 0

print(b)

# Using NumPy create random vector of size 15 having only Integers in the range 1-20.
# Then reshape the array to 3 by 5
# Then replace the max in each row by 0
# (you can NOT implement it via for loop. You need to use np.where, reshape)
