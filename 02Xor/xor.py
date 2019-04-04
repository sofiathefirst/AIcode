#!/usr/bin/env python3   
# -*- coding:UTF-8 -*-  
import tensorflow as tf
import numpy as np
from tensorflow.python import debug as tf_debug

#tf.keras.backend.set_session(tf_debug.LocalCLIDebugWrapperSession(tf.Session()))
import scipy.misc
data = tf.placeholder(tf.float32, shape=(4, 2))
label = tf.placeholder(tf.float32, shape=(4, 1))



import matplotlib
mnist = tf.keras.datasets.mnist

x_train = np.array([[1,1],[0,0],[0,1],[1,0]]);
y_train = np.array([0,0,1,1])
model = tf.keras.models.Sequential([
  #tf.keras.layers.Flatten(),

  #tf.keras.layers.Dense(2,input_shape=(2,)),
  tf.keras.layers.Dense(2, activation='sigmoid'),

  tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam',
              loss='mean_squared_error',
              metrics=['binary_accuracy'])

model.fit(x_train, y_train, epochs=5000)
model.save('my_xor.h5')
new_model = tf.keras.models.load_model('my_xor.h5')

print(new_model.predict(x_train))
print(new_model.predict_classes(x_train))

