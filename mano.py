import numpy as np

EPS = 1e-6

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

def choose_col(A):
    cost_row = A[-1][:-1]
    negative_cost_cols = np.where(cost_row < -EPS)[0]
    if len(negative_cost_cols) == 0:
        return None
    return negative_cost_cols[np.argmin(cost_row[negative_cost_cols])]

def choose_row(A, enter_col):
    assert enter_col is not None
    col = A[:-1, enter_col]
    positive_rows = np.where(col > EPS)[0]
    if len(positive_rows) == 0:
        raise ValueError('No positive rows')
    ratios = A[positive_rows, -1] / col[positive_rows]
    row_idx = np.argmin(ratios)
    return positive_rows[row_idx]

def get_basis_indices(A):
    num_cols = A.shape[1]
    basis_indices = []
    for col in range(num_cols - 1):
        column = A[:, col]
        if np.count_nonzero(column) == 1 and np.sum(column) == 1:
            basis_indices.append(col)
    return basis_indices

if __name__ == '__main__':
    A = np.array([
        [-1,  2, -1, -1, 1, 0, 0,  8],
        [ 2,  4,  0,  0, 0, 1, 0, 10],
        [ 0,  0,  1,  1, 0, 0, 1,  3],
        [ 2, -3,  0, -5, 0, 0, 0,  0],
    ], dtype=np.float32)

    while True:
        pivot_col = choose_col(A)
        if pivot_col is None:
            break
        pivot_row = choose_row(A, pivot_col)
        pivoted = simplex_pivot(A, pivot_row, pivot_col)
        A = pivoted

    print(A)
    print(get_basis_indices(A))
