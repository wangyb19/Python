import numpy as np
import pandas as pd
# 生成100*3的数组
data = np.random.randn(100, 3)
# 将data数组写入data.csv文件，分隔符为",""，添加注释和各栏信息文本
np.savetxt("data.csv", data, delimiter=",", header="x,y,z", \
       comments="# Random x, y, z coordinates\n") 
# 从data.csv文件中读取数据，跳过前两行非数值数据
data_load = np.loadtxt("data.csv", skiprows=2, delimiter=",")
# 将读取的data_load数组重新写入另一个文件，可核对读出和写入的效果
np.savetxt("data_2.csv", data_load, delimiter=",", header="x,y,z", \
       comments="Readed x, y, z coordinates\n")