import math

def possibly_square(n):
  if n % 8 not in [0, 1, 4]:
    return False
  elif n % 5 not in [0, 1, 4]:
    return False
  elif n % 3 == 2:
    return False
  else:
    return True

def is_square(n):
  if not possibly_square(n):
    return False
  else:
    return (math.isqrt(n)**2 == n)

N = 2 * 10**6

for a in range(1, N):
  if is_square(a):
    for b in range(24, a, 24):
      if is_square(a - b) and is_square(a + b) and b not in [a]:
        for c in range(24, a, 24):
          if is_square(a - c) and is_square(a + c) and c not in [a, b]:
            for j in range(24, a, 24):
              if is_square(a - j) and is_square(a + j) and j not in [a, b, c]:
                for k in range(24, a, 24):
                  if is_square(a - k) and is_square(a + k) and k not in [a, b, c, j]:
                    f = b + c + j - k
                    if f < a and is_square(a - f) and is_square(a + f) and f not in [a, b, c, j, k]:
                      print(a, b, c, j, k, f)

# import numpy as np

# while True:
#   square = np.random.randint(1, 80, size=(4, 4))**2
#   # print(square)

#   col_sums = square.sum(axis = 0)
#   row_sums = square.sum(axis = 1)

#   if np.all(col_sums == row_sums):
#     print(square)
#     print(col_sums)
#     print(row_sums)
