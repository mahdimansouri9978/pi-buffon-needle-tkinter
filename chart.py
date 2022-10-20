import matplotlib.pyplot as pl
import numpy as np
from calculate import calculate


def base_chart():
    d = 6
    x = np.linspace(- 0.5 * d, 2.5 * d, 300)
    y_1 = [0 for i in x]
    y_2 = [d for i in x]

    # pl.plot(x, y_1)
    # pl.plot(x, y_2)
    return x, y_1, y_2


def needles(x_in, y_in, x_out, y_out):
    for i in range(len(x_in)):
        pl.plot(x_in[i], y_in[i], color="b")

    for j in range(len(x_out)):
        pl.plot(x_out[j], y_out[j], color="r")

    pl.show()


# arrays = calculate(50)
# base_chart()
# needles(arrays[1], arrays[2], arrays[3], arrays[4])
