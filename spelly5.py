import numpy as np

# Define the function to be integrated
def f(x):
    return np.sin(x)  # Example function

# Implement the trapezoidal rule
def trapezoidal_rule(a, b, n):
    h = (b - a) / n  # Width of each subinterval
    integral = 0.5 * (f(a) + f(b))  # Add the first and last terms

    for i in range(1, n):
        integral += f(a + i * h)

    integral *= h
    return integral

# Main function to test the trapezoidal rule
def main():
    # Define the integration limits and number of subintervals
    a = 0  # Lower limit
    b = np.pi  # Upper limit
    n = 1000  # Number of subintervals

    # Calculate the integral using the trapezoidal rule
    result = trapezoidal_rule(a, b, n)

    # Print the result
    print(f"The integral of sin(x) from {a} to {b} is approximately: {result}")

if _name_ == "_main_":
    main()