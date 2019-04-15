import numpy as np
#import tensorflow as tf
import xlrd
import matplotlib.pyplot as plt
import os
from sklearn.utils import check_random_state

# Generating artificial data.
n = 50
XX = np.arange(n)
rs = check_random_state(0)
YY = rs.randint(-20, 20, size=(n,)) 
print('randint -20, 20, size 30*1\n',YY)

YY = rs.randint(0, 10, size=(3,4)) 
print('randint(0, 10, size=(3,4))\n',YY)
