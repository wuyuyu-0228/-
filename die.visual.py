from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die
#15-7
# 创建一个D6
die1 = Die()
die2 = Die()
die3 = Die()
# 掷几次骰子并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll() + die3.roll()
    results.append(result)

# 分析结果
frequencies = []
max_results = die1.num_sides + die2.num_sides + die3.num_sides
for value in range(3, max_results + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
# 对结果进行可视化
x_values = list(range(3, max_results + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'result', 'dtick': 1}
y_axis_config = {'title': 'frequencies of result'}
my_layout = Layout(title='results for rolling 1000 D6_D6_D6', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_d6.html')
