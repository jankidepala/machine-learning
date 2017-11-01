import tensorflow as tf
import numpy as np
import matplotlib
import pylab

#Create inp data using numpy y =x*0.1 + 0.3 + noise
x_data = np.random.rand(100).astype(np.float32)
noise = np.random.normal(scale=0.01, size=len(x_data))
y_data = x_data *0.1 +0.3 +noise

pylab.plot(x_data, y_data, ".")

#u