import tensorflow as tf
import os
tf.enable_eager_execution()
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#https://www.tensorflow.org/versions/r1.12/api_docs/python/tf/ones
a=  tf.squared_difference(5,9) 
a1= tf.squared_difference(9,4) 
print(tf.shape(a1),a1.numpy())
print(tf.shape(a),'\n',a.numpy())


 


