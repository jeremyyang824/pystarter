import pygal

from dice.die import Die

die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# print(results)

# 分析结果
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# 结果可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D{0} 1000 times".format(die.num_sides)
hist.x_labels = [str(x) for x in range(1, die.num_sides + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D{0}'.format(die.num_sides), frequencies)
hist.render_to_file('die_visual.svg')
