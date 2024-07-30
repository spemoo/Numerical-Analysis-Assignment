import numpy as np

def power_iteration(A, num_simulations):
    n, d = A.shape
    b_k = np.random.rand(n)

    for _ in range(num_simulations):
        b_k1 = np.dot(A, b_k)
        b_k1_norm = np.linalg.norm(b_k1)
        b_k = b_k1 / b_k1_norm

    eigenvalue = np.dot(b_k.T, np.dot(A, b_k)) / np.dot(b_k.T, b_k)
    eigenvector = b_k

    return eigenvalue, eigenvector

# Example usage
A = np.array([[4, 1, 1],
              [1, 3, -1],
              [1, -1, 2]])

eigenvalue, eigenvector = power_iteration(A, 1000)
print("Eigenvalue:", eigenvalue)
print("Eigenvector:", eigenvector)