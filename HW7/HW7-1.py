import matplotlib.pyplot
import numpy 
import matplotlib


x = numpy.linspace(0, 10, 100)
y_sin = numpy.sin(x)
y_log = numpy.log(x + 1)

fig, ax_1 = matplotlib.pyplot.subplots()
ax_1.plot(x, y_sin, 'b-', label = 'SIN X')
ax_1.set_xlabel('X')
ax_1.set_ylabel('SIN X', color = 'b')
ax_1.tick_params('y', colors = 'b')

ax_2 = ax_1.twinx()
ax_2.plot(x, y_log, 'r-', label = 'LOG X-1')
ax_2.set_ylabel('y', color = 'r')

fig.tight_layout()
matplotlib.pyplot.title (' Same text ')
matplotlib.pyplot.show()