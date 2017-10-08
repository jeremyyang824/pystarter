import pygal

from dice.die import Die

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# print(results)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# 结果可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D{0} 1000 times".format(die_1.num_sides)
hist.x_labels = [str(x) for x in range(1, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('2 * D{0}'.format(die_1.num_sides), frequencies)
hist.render_to_file('dice_visual.svg')
