import  numpy as np
arr=np.array([1,2,3,4,5])
print(arr)

#to check np version

import numpy as np
print(np.__version__)

#creating array using np
import numpy as np
array=np.array([1,2,3,4,5])
print(array)
print(type(np)) # to print  array type
#create array using np
import  numpy as np
arr=np.array((4,5,6,8))
print(arr)

#0d dimensional
import numpy as np
arr=np.array((45))
print(arr)

#1d
import numpy as np
arr=np.array([45,46,74])
print(arr)

#2d
import numpy as np
arr=np.array([[45,46,47],[76,77,78]])
print(arr)

#3d
import numpy as np
arr=np.array([[[4,5,6],[7,8,9],[9,10,11]]])
print(arr)

#to check dim
import numpy as np
a=np.array(45)
b=np.array([1,2,3])
c=np.array([[1,2,3],[3,4,5]])
print(a.ndim)
print(b.ndim)
print(c.ndim)

# to create 5 dimensional array
import  numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print(arr.ndim)



