import numpy as np

q = 8

def quadratic_residues(n):
  return set([a**2 % n for a in range(n)])

# Convert n to base b and pad to 6 digits
def base(n, b):
  digits = [0] * 6
  for k in range(5, -1, -1):
    d = n // b**k
    if d != 0:
      n -= d * b**k
      digits[3 - k] = d
  return digits

for n in range(8**4):
  top = np.array(base(n, 8)).reshape(2, 3)
  print(top)

'''
a b c
d e f
g h i
'''

for a in range(q):
  for b in range(q):
    for c in range(q):
      s = a + b + c
      # TODO
      for d in range(q):
        g = s - a - d
        e = s - c - g
        f = s - d - e
        h = s - b - e
        i = s - g - h

        # All of the sums are immediate except
        if a + e + i == s:
          print(a, b, c, d)
