#Author: Dhwani Patel
#Using Activation Function to computute output from layers
import numpy as np
import nnfs
from nnfs.datasets import spiral_data
nnfs.init()

X = [[1,2,3,2.5], [2.0,5.0, -1.0, 2.0], [-1.5, 2.7,3.3, -0.8]]

X, y = spiral_data(100,3)#here X is input dataset and y is output


class Layer_Dense:
    def __init__(self, n_inputs,n_neurons):
        self.weights = 0.1*(np.random.randn(n_inputs,n_neurons))
        self.baises = np.zeros((1,n_neurons))
    def forward(self,inputs):
        self.output = np.dot(inputs, self.weights) + self.baises

class Activation_ReLU:
    def forward(self,inputs):
        self.output = np.maximum(0,inputs)

layer1 = Layer_Dense(2,5)
activation1 = Activation_ReLU()
# layer2 = Layer_Dense(5,2) #Note here input of second layer should be same as outputs of previous

layer1.forward(X)
#print(layer1.output)
activation1.forward(layer1.output)
print(activation1.output)
