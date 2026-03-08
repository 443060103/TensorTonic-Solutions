import numpy as np
def f(x,a,b,c):
    return a*x**2+b*x+c
def grad(x,a,b):
    return 2*a*x + b
def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    
    # Write code here
    
    x =x0
    for i in range(steps):
        x = x-lr *grad(x,a,b)
    return x
a = 2
b = 8
c = 0
x0 = 10
lr = 0.05
steps = 200

x_min = gradient_descent_quadratic(a,b,c,x0,lr,steps)
print("Minimum x:", x_min)
print("Minimum f(x):", f(x_min, a, b, c))