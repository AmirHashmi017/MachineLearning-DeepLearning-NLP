import numpy as np
# Create 1D array
arr1=np.array([1,2,3,4,5])

# Array Attributes
print("Array:\n", arr1)
print("Shape:", arr1.shape)  
print("Number of dimensions:", arr1.ndim)  
print("Size (number of elements):", arr1.size)  
print("Data type:", arr1.dtype)  
print("Item size (in bytes):", arr1.itemsize)  

# Reshaping array (Not an inplace operation)
arr3=arr1.reshape(1,5)
print(arr3)
print(arr3.shape)

# 2D Array in numpy
arr2=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr2)
print(arr2.shape)

# Creating numpy arrays with built in functions
arr4=np.arange(0,10,2).reshape(5,1)
print(arr4)
# Create np array of 3 rows and four columns
print(np.ones((3,4)))
# Create an identity matrix or array
print(np.eye(3))

# Numpy Vectorized operations
arr1=np.array([1,2,3,4,5])
arr2=np.array([10,20,30,40,50])

#Element Wise Addition
print("Addition",arr1+arr2)
#Element Wise Subtraction
print("Subtraction",arr1-arr2)
#Element Wise Multiplication
print("Multiplication",arr1*arr2)
#Element Wise Division
print("Division",arr1/arr2)
#Element Wise Modulus
print("Modulus",arr1%arr2)

# Universal Function 
arr=np.array([2,3,4,5,6])
print(np.sqrt(arr))
print(np.exp(arr))
print(np.sin(arr))
print(np.log(arr))

# Array Slicing and indexing
arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr.size)
print("Array: \n",arr)
print(arr[0][2])
print(arr[1:,1:3])
print(arr[1:,2:])
arr[0,0]=100
arr[:,2:]=100
print(arr)

# Statistical Operations
arr=np.array([1,2,3,4,5,6,7,8,9])
print("Mean: ",np.mean(arr))
print("Median: ",np.median(arr))
print("Standard Deviation: ",np.std(arr))
print("Variance: ",np.var(arr))


# Applying logic and condition
print(arr[(arr>5)&(arr<8)])
print(arr[(arr<5)|(arr>8)])
print(arr[~(arr<5)])
