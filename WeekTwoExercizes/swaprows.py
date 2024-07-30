import numpy as np

def swap_rows(M, a, b):
    
    if not (0 <= a < M.shape[0]) or not (0 <= b < M.shape[0]):
        raise IndexError("Row indices are out of bounds")
    
    M[[a, b], :] = M[[b, a], :]
    return M

def swap_cols(M, a, b):
  
    if not (0 <= a < M.shape[1]) or not (0 <= b < M.shape[1]):
        raise IndexError("Column indices are out of bounds")
    
    M[:, [a, b]] = M[:, [b, a]]
    return M


M = np.array([[6, -9, 1], 
              [4, 24, 8]])

print("Original matrix:")
print(M)


M_swapped_rows = swap_rows(M, 0, 1)
print("\nMatrix after swapping rows 0 and 1:")
print(M_swapped_rows)


M_swapped_cols = swap_cols(M, 0, 2)
print("\nMatrix after swapping columns 0 and 2:")
print(M_swapped_cols)
