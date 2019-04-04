#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import numpy as np
np.random.seed(1337)  # for reproducibility
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt 
# 可视化模块
X = np.linspace(-1, 1, 200)
np.random.shuffle(X)    # randomize the data
Y = 0.9 * X + 2 + np.random.normal(0, 0.05, (200, ))
# plot data
#plt.scatter(X, Y)
#plt.show()
 
X_train, Y_train = X[:160], Y[:160]     # train 前 160 data points
X_test, Y_test = X[160:], Y[160:]       # test 后 40 data points
#plt.plot(X_train, Y_train,'.')
#plt.show()
model = Sequential()
l1 = Dense(output_dim = 1,input_dim = 1)
model.add(l1)

model.compile(loss = 'mse',optimizer = 'sgd')
model.fit(X_train,Y_train,epochs= 3000)

print(l1.get_weights())
Xe = np.linspace(-1, 2, 20)
Ye = model.predict(Xe)

plt.plot(X_train, Y_train,'.',Xe,Ye,'.')
plt.show()



