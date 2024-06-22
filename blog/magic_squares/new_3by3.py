from tqdm import tqdm
import math

def is_square(n):
  if n % 5 not in [0, 1, 4]:
    return False
  else:
    return (math.isqrt(n)**2 == n)

N = 10**5
count = 0

for c in tqdm(range(1, N)):
  if (c % 2 != 0) and (c % 3 != 0) and (c % 7 != 0) and (c % 11 != 0):
    # Iterating by a and b by 24 ensures all entries are congruent to 1 mod 24
    for a in range(24, c**2 // 2 + 1, 24):
      if is_square(c**2 - a) and is_square(c**2 + a):
        for b in range(a + 24, c**2 - a, 24):
          if is_square(c**2 - b) and is_square(c**2 + b):
            # print(a, b, c)
            count += 1

print(count)
