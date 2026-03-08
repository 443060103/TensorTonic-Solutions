import numpy as np

def tanh(x):
    x = np.array(x)
    return(np.exp(x)- np.exp(-x))/(np.exp(x)+np.exp(-x))
    x = [0,1,-1,3]
    print("Tanh for x is :")
    print(tanh(x))
    pass