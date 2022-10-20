import random
import numpy as np


def calculate(number):
    d = 6
    length = 3
    count = 0
    x_in = []
    y_in = []
    x_out = []
    y_out = []

    for i in range(number):
        y_c = random.random() * d
        theta = random.random() * np.pi / 2
        x_c = random.random() * 2 * d
        x = np.sqrt(length / 2) * np.cos(theta)
        y = np.sqrt(length / 2) * np.sin(theta)
        x_array = np.linspace(x_c - x, x_c + x, 50)
        y_array = np.linspace(y_c - y, y_c + y, 50)

        if length * np.sin(theta) / 2 >= y_c or (d - y_c) <= length * np.sin(theta) / 2:
            count += 1
            x_in.append(x_array)
            y_in.append(y_array)

        else:
            x_out.append(x_array)
            y_out.append(y_array)

    pi = 2 * length * number / (count * d)
    return pi, x_in, y_in, x_out, y_out
