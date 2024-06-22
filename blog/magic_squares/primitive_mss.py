import math
from tqdm import tqdm

# Use congruence of powers to determine whether n could possibly be a square
# https://proofwiki.org/wiki/Square_Modulo_5
def is_square(n):
  if n % 5 not in [0, 1, 4]:
    return False
  else:
    return (math.isqrt(n)**2 == n)

c_lower = 2 * 10**8
c_upper = 3 * 10**8

for c in tqdm(range(c_lower - (c_lower % 24) + 1, c_upper, 24)):
  if is_square(c):
    for a in range(24, c // 2 + 1, 24):
      if is_square(c + a) and is_square(c - a):
        for b in range(a + 24, c - a, 24):
          if is_square(c + b) and is_square(c - b):
            if is_square(c + (a + b)) and is_square(c - (a + b)) and is_square(c + (a - b)) and is_square(c - (a - b)):
              print(a, b, c)
