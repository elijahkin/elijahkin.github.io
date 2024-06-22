def quadratic_residues(n):
  return set([a**2 % n for a in range(n)])

def is_square(n):
  if n % 16 not in [0, 1, 4, 9]:
    return False
  elif n % 9 not in [0, 1, 4, 7]:
    return False
  elif n % 7 not in [0, 1, 2, 4]:
    return False
  elif n % 5 not in [0, 1, 4]:
    return False
  else:
    # Need to do rounding stuff here
    return True

def cubic_residues(n):
  return set([a**3 % n for a in range(n)])

def is_cube(n):
  if n % 9 not in [0, 1, 8]:
    return False
  elif n % 7 not in [0, 1, 6]:
    return False
  elif n % 13 not in [0, 1, 5, 8, 12]:
    return False
  elif n % 8 not in [0, 1, 3, 5, 7]:
    return False
  else:
    # Need to do rounding stuff here
    return True

count = 0
for a in range(10**8):
  count += is_square(a)
print(100 * count / 10**8)