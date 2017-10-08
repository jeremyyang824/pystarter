import matplotlib.pyplot as plt

# plt.scatter(2, 4, s=200)

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.scatter(x_values, y_values, s=100)

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]
# plt.scatter(x_values, y_values, s=5, c=(0, 0, 0.8), edgecolors='none')
plt.scatter(x_values, y_values, s=5, edgecolors='none', c=y_values, cmap=plt.cm.Reds)

# 设置图表标题并给坐标加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Square of Value", fontsize=24)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置坐标轴取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()
# plt.savefig('squares_plot.png', bbox_inches='tight')
