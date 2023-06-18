import numpy as np

arr=np.array([4,5,6,7,8])
print(arr[0]) #first element of index of array
print(arr[1]) #second element of array
print(arr[2],arr[3])

#Accessing 2D - Array
import numpy as np
array=np.array([[1,2,3,4],[4,5,6,7]])
print("The first row of second column:",array[0,1])


x=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("The 5th column of second element is:",x[1,4])

y=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(y[0,1,2])
#3D dimensional

z=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(z[0,2,1])
#negative index
print(z[0,2,-1])

