import numpy as np

def lagrange_interpolation(x_points, y_points, x):
    n = len(x_points)
    P_x = 0
    for i in range(n):
        L_i = 1
        for j in range(n):
            if j != i:
                L_i *= (x - x_points[j]) / (x_points[i] - x_points[j])
        P_x += y_points[i] * L_i
    return P_x

# Example usage:
x_points = [1, 2, 3, 4]
y_points = [1, 4, 9, 16]

x_values = np.linspace(1, 4, 100)
lagrange_values = [lagrange_interpolation(x_points, y_points, x) for x in x_values]

import matplotlib.pyplot as plt

plt.plot(x_points, y_points, 'ro', label='Data points')
plt.plot(x_values, lagrange_values, label='Lagrange Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()