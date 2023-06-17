#To calculate mean,meadian and mode in machine learning

import numpy as np
import scipy
from scipy import stats
speed=np.array([99,86,87,88,103,87,94,78,77,85,86])
print(np.mean(speed)) # To calculate mean
print(np.median(speed)) #To calculate median

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)
print(x)

