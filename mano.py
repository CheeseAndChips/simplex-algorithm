import numpy as np


def simplex_pivot(A, pivot_row, pivot_col):
    num_rows = A.shape[0]
    Aprime = A.copy()
    pivot_element = A[pivot_row, pivot_col]
    Aprime[pivot_row, :] /= pivot_element
    for i in range(num_rows):
        if i != pivot_row:
            row_factor = Aprime[i, pivot_col]
            Aprime[i, :] -= row_factor * Aprime[pivot_row, :]
    return Aprime

if __name__ == '__main__':
    A = np.array([
        [ -3, 0, -7, 0,-20],
        [4/3, 1,  1, 0, 6],
        [1/3, 0,  2, 1, 2]
    ], dtype=np.float32)
    print(simplex_pivot(A, 2, 2))
