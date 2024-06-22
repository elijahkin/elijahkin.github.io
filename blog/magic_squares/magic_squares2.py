import math

# Use congruence of powers to determine whether n could possibly be a square
# https://proofwiki.org/wiki/Square_Modulo_8
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

def count_squares(arr):
  return sum([is_square(n) for n in arr])

c_lower = 1
c_upper = 2 * 10**5

for c in range(c_lower, c_upper):
  # Periodically print c for progress tracking
  if c % 10**5 == 0:
    print(f'c={c}')

  if is_square(c):
    # From Lucas we know 0 < 2a < c
    for a in range(1, c // 2 + 1):
      if is_square(c + a) or is_square(c - a):
        # Again from Lucas we know a < b < c - a
        for b in range(a + 1, c - a):
          if count_squares([c, c + a, c - a, c + b, c - b, c + (a + b), c - (a + b), c + (a - b), c - (a - b)]) >= 7:
            print(a, b, c)