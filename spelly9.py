# Gradient Descent for Function Minimization
def f(x, y):
    return x*2 + y*2 - xy + x - y + 1

def grad_f(x, y):
    df_dx = 2*x - y + 1
    df_dy = 2*y - x - 1
    return np.array([df_dx, df_dy])

def gradient_descent(learning_rate, num_iterations, initial_guess):
    x, y = initial_guess
    for _ in range(num_iterations):
        grad = grad_f(x, y)
        x = x - learning_rate * grad[0]
        y = y - learning_rate * grad[1]
    return x, y

# Example usage
learning_rate = 0.1
num_iterations = 1000
initial_guess = (0, 0)

x_min, y_min = gradient_descent(learning_rate, num_iterations, initial_guess)
print("Minimum at x:", x_min)
print("Minimum at y:", y_min)