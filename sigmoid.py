import numpy as np

def sigmoid(x):
    # TODO: Implement sigmoid function
    return 1/(1 + np.exp(-x))


inputs = np.array([0.7, -0.3])
weights = np.array([0.1, 0.8])
bias = -0.1

# TODO: Calculate the output
#output = sigmoid(np.dot(weights, inputs) + bias)
output = (inputs[0] * weights[0]+ inputs[1] * weights[1]) + bias
# output = sigmoid(np.dot(weights, inputs) + bias)
output =  sigmoid(output)

print('Output:')
print(output)
