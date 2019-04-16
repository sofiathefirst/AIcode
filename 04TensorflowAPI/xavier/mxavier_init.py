import tensorflow as tf
import os
import numpy as np
tf.enable_eager_execution()
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#https://www.tensorflow.org/versions/r1.12/api_docs/python/tf/ones
a=  tf.constant([1,1, 2,3, 3, 4, 5, 6, 7]) 
def xavier_init(fan_in,fan_out, constant = 1):
	low =-constant*np.sqrt(6.0/(fan_in+fan_out))
	high = -low
	return tf.random_uniform((fan_in,fan_out),\
 minval=low,maxval=high,dtype = tf.float32)
# Reverse iterator
#def __next__(self):

if __name__ == '__main__':	
	a = xavier_init(3,4)
	print(a.numpy())
