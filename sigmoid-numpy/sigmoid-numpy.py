import numpy as np

def sigmoid(x):
    x = np.array(x)
    return 1/(1+np.exp(-x))

x1 = [0, 2, -2]
x2 = [[-1, 0], [1, 2]]

print(sigmoid(x1))
print(sigmoid(x2))