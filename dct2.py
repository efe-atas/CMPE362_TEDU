import math

def dct1d(signal):
    N = len(signal)
    result = [0] * N
    for k in range(N):
        sum_s = 0
        for n in range(N):
            # Calculate the sum for DCT
            sum_s += signal[n] * math.cos(math.pi * k * (2 * n + 1) / (2 * N))
        # Normalize the result
        if k == 0:
            result[k] = sum_s * math.sqrt(1 / N)
        else:
            result[k] = sum_s * math.sqrt(2 / N)
    return result

def transpose(matrix):
    # Transpose the given matrix (swap rows with columns)
    return list(map(list, zip(*matrix)))

def pad_matrix(matrix, target_rows, target_cols):
    # Get current dimensions of the matrix
    current_rows = len(matrix)
    current_cols = len(matrix[0]) if matrix else 0
    # Pad each row to the target number of columns
    new_matrix = [row[:] + [0] * (target_cols - current_cols) for row in matrix]
    # Add additional rows filled with zeros if necessary
    if current_rows < target_rows:
        for _ in range(target_rows - current_rows):
            new_matrix.append([0] * target_cols)
    return new_matrix

def dct2(a, mrows=None, ncols=None):
    if not a:
        return []

    # Check if dimensions are provided as tuple/list and unpack them
    if isinstance(mrows, (tuple, list)):
        mrows, ncols = mrows[0], mrows[1]
    # Pad the matrix if target dimensions are provided
    if mrows is not None and ncols is not None:
        a = pad_matrix(a, mrows, ncols)
    
    # Apply 1D DCT to each row
    dct_rows = [dct1d(row) for row in a]
    
    # Transpose the matrix and apply 1D DCT to each row (originally each column)
    dct_cols = transpose(dct_rows)
    dct_cols = [dct1d(row) for row in dct_cols]
    
    # Transpose the matrix back to the original orientation
    result = transpose(dct_cols)
    return result

def print_matrix(matrix):
    # Print the matrix with each value formatted to four decimal places
    for row in matrix:
        for val in row:
            print(f"{val:.4f}", end=" ")
        print()  # Move to the next row


'''''
A = [
    [0.6, 0.2, 0.8, 0.5],
    [0.9, 0.7, 0.6, 0.1],
    [0.4, 0.3, 0.5, 0.9],
    [0.1, 0.8, 0.2, 0.7]
]

# Perform 2D DCT on the matrix A
B = dct2(A)
print('DCT of A:')
print_matrix(B)

# Perform 2D DCT on matrix A with padding to 8x8
C = dct2(A, 8, 8)
print('DCT of A with padding to 8x8:')
print_matrix(C)

'''''