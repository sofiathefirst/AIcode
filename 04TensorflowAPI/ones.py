import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#https://www.tensorflow.org/versions/r1.12/api_docs/python/tf/ones
a= tf.ones((4,3))

b = tf.ones((2,3))

with tf.Session():
  result = a.eval()
  rb = b.eval()
  tf.assert_negative (a)

print(result,rb )

