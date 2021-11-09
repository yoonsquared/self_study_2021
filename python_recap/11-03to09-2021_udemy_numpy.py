# 11-03-2021_udemy_numpy
## numpy array
my_list = [1,2,3]
print(my_list)
import numpy as np

arr = np.array( my_list )
print(arr)

## numpy matrix
my_mat = [[1,2,3],[4,5,6],[7,8,9]]
print(my_mat)

arr = np.array(my_mat)
print(arr)

## arange
### from 0 to less than 10 by 1
print(np.arange(0,10))
### from 0 to less than 11 by two.
print(np.arange(0,11,2))

##  array of zeros or ones
print( np.zeros(3) )
print( np.ones(4) )

## matrix of ones
print( np.ones( (3,4) ) )

## linspace()
### 15 evenly spaced numbers from 0 to 5
print( np.linspace(0,5,15) )

## eye(), creates a identity matrix, square with diagonal 1's and rest 0.
print( np.eye(4) ) #4x4 matrix

## random numbers
print( np.random.rand(5) )
print( np.random.rand(3,3) ) #3x3 matrix

## gaussian random
print( np.random.randn(2) )

## random integers
print( np.random.randint(1, 100, 10) ) #100 is not inclusive.

## reshape()
### Make sure the number of elements (row*col) are equal. 1*25 == 5*5
arr = np.arange(25) # 1x25
print( arr )
reshape_arr = arr.reshape(5,5) # 5x5
print( reshape_arr )

ranarr = np.random.rand(16)
print( ranarr )
print( ranarr.max() )
print( ranarr.min() )
print( ranarr.argmax() )
print( ranarr.argmin() )
print( ranarr.shape )
print( ranarr.reshape(4,4) )

## calling functions within numpy directly
from numpy.random import randint
print( randint(2,10) )

# Numpy Array Indexing and Selection
print("numpy array indexing and selection")
arr = np.arange(0,11)
print(arr)

print( arr[8] )
print( arr[1:5] )
print( arr[0:5] )
print( arr[:5] ) #from start (which is 0) to 5
print( arr[2:] ) #from 2 to end

arr[0:5] = 100
print( arr )

## example of Broadcasting.
### slice of an array change will apply to it's mother array.
### basically like a *symlink in linux!*
arr = np.arange(0,11)
print(arr)
slice_of_arr = arr[0:6]
print(slice_of_arr[:])
slice_of_arr[:] = 99
print(slice_of_arr) 
print(arr) # we never edited arr, but changing the 'slice_of_arr', which broadcasts a part of 'arr' is changed, the 'arr' is changed

## 2d array
arr_2d = np.array([[5,10,15],[20,25,30], [35,40,45]])
print( arr_2d )
print( arr_2d[0][0] )
print( arr_2d[0] )
print( arr_2d[0,0] )
print( arr_2d[:2,1:] )
print( arr_2d[:3,2] )
print( arr_2d[:3,1] )

## boolean arrays
arr = np.arange(1,11)

### only returns instances where that boolean array is true.
bool_arr = arr >5
print( bool_arr )
print( arr[bool_arr] )
#### same as
#### this is something you will use a lot in pandas.
print( arr[arr>5] )

## NumPy Operations
"""
These will be added to all items in the arrays.
"""
arr = np.arange(0,11)
print( arr )
print( arr + arr )
print( arr - arr )
print( arr * arr )
print( arr + 100 )

print( arr / arr ) # note that 0 / 0 will get a 'nan' with a warning.
print( 1 / arr ) # note that 1 / 0 will give you a 'inf' with a warning.

### universal functions ufunc
print( arr ** 2 ) # square on all items
print( np.sqrt(arr) ) # square root
np.exp( np.exp(arr) ) # exponential
np.max( arr ) # same thing as arr.max()
np.sin( arr ) # sine, can do cosine, tangent.


## Exercise answers
### array of 10 zeros, 10 ones, 10 5s
print( np.zeros(10) )
print( np.ones(10) )
print( np.ones(10) * 5 ) #or np.zeros + 5

### create an array of integers from 10 to 50
print( np.arange(10,51) )

### create an array of all the even integers from 10 to 50
print( 10,51,2 )

### create a 3x3 matrix with values ranging from 0 to 8
print( np.arange(9).reshape(3,3) )

### create a 3x3 identity matrix
print( np.eye(3) )

### generate a random number between 0 and 1
print( np.random.rand(1) )

### NumPy to generate a 25 random numbers sampled from standard normal distribution
print( np.random.randn(25) )

### Create a specific matrix 0.01 -> 1 in a 0.01 stepsize
#### has to be 10x10 matrix
print( np.arange (1, 101).reshape(10,10)  / 100 )
print( np.linspace(0.01,1,100).reshape(10,10) )

### create a 20 linearly spaced points between 0,1
print( np.linspace(0,1,20) )

### create the resulting matrix from a given matrix here.
mat = np.aranage(1,26).reshape(5,5)
print( mat ) 

#### we need to get rows from 3 on
#### and columns from 2 on
print( mat[2:,1:] )

### From the same mat, get the number 20 using indexes
print( mat[3,4] )

### grab 2,7,12 in double-bracket mode.
#### compare the formats.
print( mat[:2, 1])
print( mat[:2,1:2] ) # make sure that ,1 and ,1:2 will give you different dimensional array.

### get the last row
print( mat[4,:] )
print( mat[-1,:] ) #when you know it's the last, using the negative indexing.

### get last two rows double brackets
print( mat[3:5,:] )

### get sum of all values in mat
print( np.sum(mat) )
print( mat.sum() )

### standard deviation of a mat
print( mat.std() )
print( np.std(mat) )

### get sum of all the columns in mat
print( mat.sum(axis=0) ) #axis=0 is column, 1 is row.