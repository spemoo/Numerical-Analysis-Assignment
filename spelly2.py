
import numpy as np
from scipy.integrate import quad

# Define the function to integrate
def f(x):
  return x**2 + 2*x - 1

# Integrate the function from 0 to 2
result, error = quad(f, 0, 2)

print("Result of integration:", result)
print("Estimated error:", error)