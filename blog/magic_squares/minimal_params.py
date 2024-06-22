import numpy as np

# Check whether there exists a n variables parameterization for 5-by-5 magic squares

def is_solvable(A):
  while True:
    # A = A + np.flip(A)

    col_sums = np.sum(A, axis = 0)
    row_sums = np.sum(A, axis = 1)
    diag1 = np.trace(A)
    diag2 = np.trace(np.flip(A, axis = 0))

    if np.any(row_sums == 4):
      A[row_sums == 4, :] = 1
    elif np.any(col_sums == 4):
      A[:, col_sums == 4] = 1
    elif diag1 == 4:
      for l in range(5):
        A[l, l] = 1
    elif diag2 == 4:
      for l in range(5):
        A[l, 4 - l] = 1
    else:
      break

  return np.all(A == 1)

for _ in range(10**4):
  # Generate random setup with 7 variables
  square = np.zeros(25, dtype=bool)
  sample = np.random.choice(range(25), size=14, replace=False)
  square[sample] = 1
  square = square.reshape(5, 5)

  # print(square)

  # Check if it is solvable
  if is_solvable(square):

    print(sample.reshape(5, 5))
    print(square)