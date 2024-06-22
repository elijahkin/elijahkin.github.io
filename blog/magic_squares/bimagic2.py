import numpy as np

params = np.zeros(())


# Convert n to base b and pad to 10 digits
def base(n, b):
  digits = [0] * 10
  for k in range(9, -1, -1):
    d = n // b**k
    if d != 0:
      n -= d * b**k
      digits[9 - k] = d
  return digits

# We try to figure out the structure mod 8 of the squared square
count = 0
for n in range(3**10):
  # Convert to base 3 since there are 3 quadratic residues mod 8
  top = np.array(base(n, 3)).reshape(2, 5)