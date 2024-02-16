# repeat(): 
# The numpy.repeat() function repeats elements of the array ofthe  array 

# concatenate(): 
# numpy .concatenate() function concatenate a square of array along an existing axis 

# vstack(): 
# numpy.vstack() function is used to stack the sequance of  

# r_in numpy 

# Trancslates slice objects to concatenation  along the first  axis

# hstack()

#hsatack() function is used to stack the sequance  of input horizontal to make  a single  array

import numpy as np 
arr=np.repeat([3],5,axis=0)
print(arr)
print(arr)

arr1=np.repeat([4],5,axis=0)
print(arr1)
# print(np.repeat([[3,5]],5,axis=5))
print(np.repeat([[3,4]],5,axis=0))
print(np.repeat([[3,2]],5,axis=0))
print("ths is next one ")
print(np.repeat([[3,2]],5,axis=1))
print("#####")
arr=np.array([1,4,5,6])
arr1=np.array([4,5,6,7])
c=np.concatenate([arr,arr1])
print(c)
print("$$$")

arr=np.array([[1,2,3,4],[1,2,3,4]])
arr1=np.array([[4,5,6,7],[2,5,7,9]])
print(np.concatenate([arr,arr1],axis=1))
print(np.concatenate([arr,arr1],axis=0))

print("vstack")

v=np.vstack([arr,arr1])
print(v)

print("using r_statment")
print(np.r_[arr,arr1])

print("hstack")
h=np.hstack([arr,arr1])
print(h)

print("Ths power funciton ")
#power() It is used  to get array containing elements of the first array raised to the power elemets  of the second array
#diff(): 
#This Function is used when we calculate the the nth order disecrete diffrence along the given axis 
# cross(): 
# It  returns the cross product of two vectors sort()

# sort()
#This Function return the sorted copy of a array 

import numpy as np 
arr=np.array([1,2,3,3,4])
print(arr)

p=np.power(arr,[2])
print(p)

print(np.power(arr,[1,2,2,3,5]))


print('this is the diffrence funciton ')
arr=np.array([1,2,3,4,5,6])
arr1=np.array([2,3,4,5,5,6])
print(np.diff(arr))
print("2222")
print(np.diff(arr1))
print("333")
d=np.diff((arr,arr1),axis=1)
print(d)

# cross()

# c=np.cross((arr,arr1))
# print(c)
# c=np.cross(arr,arr1)
# print(c)

arr=np.array([1,2,3,4,5])
arr1=np.array([2,7,4,5,4])
print(arr)
print(arr1)
s=np.sort((arr,arr1),axis=0)

print("this is vertucally")

print(s)
s=np.sort((arr,arr1),axis=1)
print(s)

