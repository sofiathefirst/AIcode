import tensorflow as tf
import os
tf.enable_eager_execution()
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#https://www.tensorflow.org/versions/r1.12/api_docs/python/tf/ones
a=  tf.constant([1,1, 2,3, 3, 4, 5, 6, 7]) 

b = tf.data.Dataset.from_tensor_slices(a)
for e in b .take(17):
	print(e.numpy())

#with tf.Session():
  #result = a.eval()
  #rb = b.eval()
  #tf.assert_negative (a)

#print(result)

