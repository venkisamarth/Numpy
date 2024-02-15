import numpy as np 
arr=np.array([1,2,4,5,6])
print(arr)
print(type(arr))

arr1=np.array([1,2,3,4,6,7,8,9])
print(arr1)
print(type(arr))
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

# zero dimational array 
arr=np.array(12)
print(arr)
print(arr.shape)
print(arr.size)
print(np.ndim)
print(arr.shape)

#Three  dimentional array 
arr=([[1,2,3,4],[1,2,3,4]],[[1,2,2,3],[1,2,3,4]])
print(arr)

print(arr[0:2])

arr=np.array([10,20,30,40])
print(arr[0:2])
print(arr[2:])
print(arr[::])
print([arr[::2]])
print(arr[::-1])

arr2=np.array([[10,20,30,40],[50,60,70,80],[10,20,30,40]])
print(arr2)

print(arr2[0:2,0:2])
print(arr2[0:2,0:2])
print(arr2[0:,1:])
print(arr2[0])
print(arr2[0,0:2])
print(arr2[1,0:2])
print(arr2[2,2:])

#Attribute 
arr=np.array([[10,20,30,40],[50,60,70,80],[10,30,50,70]])
print(np.shape(arr))
print(np.size(arr))
print(np.ndim(arr))

print(arr.dtype)

# create a numpy with numpy array module and a data type integer and float 
arrint=(np.array([1,2,3,4,5]))
print(arrint)
print(arrint.dtype)
print(arrint.shape)
print(arrint.size)
print(arrint.ndim)

arrf=np.array([1,2,3,4,5],dtype=float)
print(arrf)
# create numpy array that have zero one,two three foure dimention respectively  also 
# print the shape and dimention  of the numpy array shape and dimention of the numpy 
print(arrf.shape)
print(np.size(arrf))
print(np.ndim(arrf))
print(arrf.dtype)

# create a 2x3 ,3x3 and 4x4 identity matrix  using numpy  
a=np.identity(2)
b=np.identity(3,dtype=int)
b=np.identity(4,dtype=int)

# create numpy arry with shape 2x5 that has all elements as zero 
arr=np.zeros((2,5))
print(arr)

# creat a numpy array that has the shape 3x5 and all the elements  are 5  
arr5=np.ones((3,5),dtype=int)*5
print(arr5)
