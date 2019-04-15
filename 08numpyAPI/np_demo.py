#!/usr/bin/python3
# -*- coding:UTF-8 -*-  

import numpy as np
a = np.zeros((3,4))
b = np.ones((3,2))
c = np.ones([2,4])

x = np.hstack([a,b])
y = np.vstack([a,c])
print('x,y',x.shape, y.shape)

m = a
n = np.ones([3,4])
np.stack([m,n], axis=0)
np.stack([m,n], axis=1)
#change type

a=range(34)
a = np.array(a)
a = a.astype('int')
a = a.astype('str')
a = a.astype('float32')

