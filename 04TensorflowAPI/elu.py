#!/usr/bin/python3
import tensorflow as tf
import os
from math import *
print('tf versions',tf.__version__)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#https://www.tensorflow.org/api_docs/python/tf/keras/activations
e1=tf.keras.activations.elu(-1.3)
e2=tf.keras.activations.elu(1.3)
with tf.Session():
  re1 = e1.eval()
  re2 = e2.eval()

print(re1,re2, exp(-1.3)-1 )

