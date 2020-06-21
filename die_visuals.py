from die import Die
import pygal

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll_die() + die_2.roll_die()
    results.append(result)

frequencies = []
max_results = die_1.num_sides + die_2.num_sides
for value in range(2, max_results + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualiza results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = list(range(2, max_results + 1))
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')