#!/usr/bin/python3
# -*- coding:UTF-8 -*-  
import tensorflow as tf

import scipy.misc
import matplotlib
mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
scipy.misc.imsave('pic'+str(y_test[1])+'.png',x_test[1,:,:])#将数组保存成图片
scipy.misc.imsave('pic'+str(y_test[2])+'.png',x_test[2,:,:])
x_train, x_test = x_train / 255.0, x_test / 255.0


import cv2
#imread(filename[, flags]) -> retval
imgPath = '3.jpg' #图片路径
#默认读取的是RGB三色图,得到三维矩阵
img = cv2.imread(imgPath,cv2.IMREAD_GRAYSCALE)
cv2.imshow(str(y_test[1]),x_test[1,:,:])
cv2.waitKey(1)
cv2.imshow(str(y_test[3]),x_test[3,:,:])
cv2.waitKey(1)
cv2.destroyAllWindows()

#temp = cv2.imread('/home/q/Desktop/8.jpg',cv2.IMREAD_GRAYSCALE)
#等价于img = cv2.imread('test01.jpg',cv2.IMREAD_COLOR)
#查看图像维数(719,1280,3)
#print(img)

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28,28)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.save('my_minis.h5')#save model
new_model = tf.keras.models.load_model('my_minis.h5')#load model
temp = cv2.imread('n5.png',cv2.IMREAD_GRAYSCALE)
temp = 1-temp/255.0
t3 = temp.reshape(1,28,28)
print('n5.png is:',model.predict_classes(t3,1)[0])

temp = cv2.imread('n7.png',cv2.IMREAD_GRAYSCALE)
temp = 1-temp/255.0
t3 = temp.reshape(1,28,28)
print('n7.png is:',new_model.predict_classes(t3,1)[0])

