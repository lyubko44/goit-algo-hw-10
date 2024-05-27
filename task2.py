import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

def f(x):
    return x ** 2

a = 0
b = 2

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

num_points = 10000

x_points = np.random.uniform(a, b, num_points)
y_points = np.random.uniform(0, max(y), num_points)

points_inside = sum(f(x_points) > y_points)

ratio = points_inside / num_points

integral_estimate = ratio * (b - a) * max(y)

integral_quad, _ = spi.quad(f, a, b)

print("Оцінка інтеграла методом Монте-Карло:", integral_estimate)
print("Значення інтеграла, отримане за допомогою quad:", integral_quad)
