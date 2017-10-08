import matplotlib.pyplot as plt

from random_walk.rw_data_builder import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
# while True:

rw = RandomWalk(num_points=5000)
rw.fill_walk()

# 设置绘图窗口尺寸
plt.figure(dpi=128, figsize=(8, 5))

point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=5)

# 突出起点和终点
plt.scatter(0, 0, c='green', edgecolors='none', s=50)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)

# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()

# keep_running = input("Make another walk? (y/n): ")
# if keep_running == 'n':
#     break
