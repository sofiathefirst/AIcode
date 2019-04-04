import tensorflow as tf
import os
from math import *
print('tf versions',tf.__version__)#tf versions 1.13.1
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

e1=tf.keras.activations.linear(1.3)
e2=tf.keras.activations.linear(0.1)
print(e1,e2)#1.3 0.1


