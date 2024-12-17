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

if __name__ == '__main__':
    A = np.array([
        [4/3, 1,  1, 0, 6],
        [1/3, 0,  2, 1, 2],
        [ -3, 0, -7, 0,-20],
    ], dtype=np.float32)
    pivot_col = choose_col(A)
    pivot_row = choose_row(A, pivot_col)
    pivoted = simplex_pivot(A, pivot_row, pivot_col)
    print(pivoted)
