import tensorflow as tf
import os
tf.enable_eager_execution()
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#https://www.tensorflow.org/versions/r1.12/api_docs/python/tf/ones
a=  tf.constant([[1,1, 2],[3, 3, 4], [5, 6, 7]]) 
a1= tf.reshape(a,[1,9])
print(tf.shape(a1),a1.numpy())
print(tf.shape(a),'\n',a.numpy())

b = tf.expand_dims(a,0)
print(tf.shape(b))

b = tf.expand_dims(a,1)
print(tf.shape(b))

b = tf.expand_dims(a,2)
print(tf.shape(b))
b = tf.expand_dims(a,-1)
print(tf.shape(b))
 


