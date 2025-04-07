import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# 将绘图字体全局更改为times new roman
plt.rc("font", family = "Times New Roman")
# 启用对tex的支持，此项设置存在问题，其会影响其他位置字体
# plt.rcParams['text.usetex'] = True

data = np.loadtxt("data.csv", skiprows=2, delimiter=",")
x = data[:,0]
ysin = data[:,1]
ycos = data[:,2]

fig, ax = plt.subplots()
# 散点图
# ax.scatter(x, ysin, label = "scatter plot")
ax.plot(x, ysin, color = "black", marker = "s", markevery = 1, 
        markersize = 8, linestyle = "-", linewidth=2.0, 
        label = "y = sin(2*x)")
# 颜色："black", "red", "blue", "purple", "orange", "green", "yellow"
# 标记："s"方块, "o"实心圆, "^"正三角, "v"反三角, "+"加号, "*"星号, "p"五边形 
# 线型："-"实线, "--"虚线, "none"无线
ax.plot(x, ycos, color = "red", marker = "o", markevery = 1, 
        markersize = 8, linestyle = "dashed", linewidth=2.0, 
        label = "y = cos(2*x)")
# 设置坐标轴名称
ax.set_xlabel("x")
ax.set_ylabel("y")
# 设置坐标轴范围
plt.xlim(-0.1, 10.1)
plt.ylim(-1.1,1.5)
ax.legend()

plt.show()
# 将所绘制图保存为png格式图片
fig.savefig("Line.png", dpi=1200)