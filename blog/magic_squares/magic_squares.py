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

# c_lower = 113 * 10**6
# c_upper = 200 * 10**6
c_lower = 1
c_upper = 10**6

for c in range(c_lower, c_upper):
  # Periodically print c for progress tracking
  if c % 10**5 == 0:
    print(f'c={c}')

  # Using Lucas' construction, c must be square
  if is_square(c):
    # From Lucas we know 0 < 2a < c
    for a in range(1, c // 2 + 1):
      if a % 12 == 0:
          if is_square(c + a) and is_square(c - a):
            # Again from Lucas we know a < b < c - a
            for b in range(a + 1, c - a):
              if b % 12 == 0:
                if (is_square(c + b) + is_square(c - b) + is_square(c + (a + b)) + is_square(c - (a + b)) + is_square(c + (a - b)) + is_square(c - (a - b)) >= 4):
                  print(a, b, c)
                # if is_square(c + b) and is_square(c - b):
                  # if is_square(c + (a + b)) and is_square(c - (a + b)) and is_square(c + (a - b)) and is_square(c - (a - b)):
                  #   print(a, b, c)
