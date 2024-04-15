import numpy as np


def pseudoinverse(A):
    # Compute the SVD
    U, s, Vt = np.linalg.svd(A)

    # Invert the singular values
    s_inv = np.zeros(A.shape).T
    for i in range(len(s)):
        s_inv[i, i] = 1 / s[i]

    # Compute the pseudoinverse
    return Vt.T @ s_inv @ U.T


# Testing the function
def test_pseudoinverse():
    # Generate random matrices for testing
    for _ in range(10):
        A = np.random.rand(4, 4)

        # Ensure matrix is invertible
        while np.linalg.det(A) == 0:
            A = np.random.rand(4, 4)

        A_inv = np.linalg.inv(A)
        A_pseudo_inv = pseudoinverse(A)
        error = np.linalg.norm(A_inv - A_pseudo_inv)

        assert error < 1e-10, f"Failed for matrix {A}"

    print("All pseudoinverse equals the actual inverse up to numerical precision")


test_pseudoinverse()