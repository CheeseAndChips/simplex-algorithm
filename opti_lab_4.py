import numpy as np

originalA = np.array([[-1,  1, -1, -1,  1, 0, 0,  8],
                      [ 2,  4,  0,  0,  0, 1, 0, 10],
                      [ 0,  0,  1,  1,  0, 0, 1,  3],
                      [ 2, -3,  0, -5,  0, 0, 0,  0]], dtype=np.float32)

A = originalA.copy()
Baze = [5, 6, 7]

def refactor_matrix(A, col, row):
    A[row, :] = A[row, :] / A[row, col]  # normalize the row
    
    for r in list(range(0, row)) + list(range(row + 1, 4)):
        multiplier = -A[r, col]
        
        A[r, :] = A[r, :] + multiplier * A[row, :]  # eliminate the row
    return A

while True:
    min_cost = np.min(A[-1, :-1])
    j = np.argmin(A[-1, :-1])
    if min_cost >= 0:
        break

    RHS = A[:-1, -1]
    A_j = A[:-1, j]
    A_j[A_j <= 0] = 0

    lambda_vals = RHS / A_j
    leave_col_rowIndex = np.argmin(lambda_vals)
    Baze[leave_col_rowIndex] = j

    A = refactor_matrix(A, j, leave_col_rowIndex)
    
print(np.round(A, 2))

Xfull = np.zeros(7)
Xfull[Baze] = A[0:3, -1]
print()
print("F(X) = 2*x1 − 3*x2 − 5*x4")
print('X* = [{:.6g}, {:.6g}, {:.6g}, {:.6g}]'.format(*Xfull[0:4]))
print(f"F(X*) = 2*{Xfull[0]} - 3*{Xfull[1]} - 5*{Xfull[3]} = {-A[-1, -1]}")
