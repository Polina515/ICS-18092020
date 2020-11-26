import numpy as np
from numpy import*
import matplotlib.pyplot as plt
fig = plt.figure()
def f(x):
    return 2**x*sin(10*x)
x=linspace(-3,3,110)
y=f(x)
plt.plot(x,y, "c-")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Y(x)=2^x*sin(10x), x=[-3...3] ')
plt.grid(True) 
plt.show()
fig.savefig('sin.png')







         
