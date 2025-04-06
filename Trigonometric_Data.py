import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100).reshape(100,1)
print(x.shape)
# z = x.transpose()   # 需特别指出的是这个语句并不对x向量产生任何影响
ysin = np.sin(2 * x)
ycos = np.cos(2 * x)
data = np.hstack((x,ysin,ycos))
print(data.shape)
np.savetxt("data.csv", data, delimiter=",", header="x,sin,cos", \
       comments="# arrays of x and ysin and ycos\n")