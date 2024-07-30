# QR Algorithim
def qr_algorithm(A, num_simulations):
    A_k = np.copy(A)
    for _ in range(num_simulations):
        Q, R = np.linalg.qr(A_k)
        A_k = np.dot(R, Q)

    eigenvalues = np.diag(A_k)
    return eigenvalues

# Example usage
eigenvalues = qr_algorithm(A, 1000)
print("Eigenvalues:", eigenvalues)