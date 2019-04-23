import theano
import theano.tensor as T
x = T.dmatrix('x')
s = 1/(1+T.exp(-x))
l = theano.function([x],s)

l([[0,1],[-1,-2]])
#array([[0.5       , 0.73105858],
#       [0.26894142, 0.11920292]])

from math import *
exp(3)
#20.085536923187668
exp(1)
#2.718281828459045
1/(1+exp(0))
#0.5
1/(1+exp(1))
#0.2689414213699951
1/(1+exp(-1))
#0.7310585786300049
1/(1+exp(2))
#0.11920292202211755


