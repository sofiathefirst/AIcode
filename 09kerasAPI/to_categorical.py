from keras.utils import np_utils
#Using TensorFlow backend.
import numpy as np
a = range(10)
a
range(0, 10)
a = np.array(a)
print(np_utils.to_categorical(a,10))

#array([[1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
#       [0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
#       [0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
#       [0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
#       [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
#       [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
#       [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
#       [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
#       [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
#       [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.]], dtype=float32)


