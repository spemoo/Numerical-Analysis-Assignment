
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Sample data
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([0, 0.8, 0.9, 0.1, -0.8, -1])

# Define the function to fit (example: a quadratic function)
def func(x, a, b, c):
  return a * x**2 + b * x + c

# Perform curve fitting
popt, pcov = curve_fit(func, x_data, y_data)

# Extract the fitted parameters
a_fit, b_fit, c_fit = popt

# Generate points for the fitted curve
x_fit = np.linspace(x_data.min(), x_data.max(), 100)
y_fit = func(x_fit, a_fit, b_fit, c_fit)

# Plot the data and the fitted curve
plt.plot(x_data, y_data, 'o', label='Data')
plt.plot(x_fit, y_fit, '-', label='Fit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()