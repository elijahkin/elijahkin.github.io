def sextic_residues(n):
  return set([a**6 % n for a in range(n)])

def is_sextic(n):
  if n % 27 not in [0, 1, 10, 19]:
    return False
  elif n % 32 not in [0, 1, 9, 17, 25]:
    return False
  elif n % 31 not in [0, 1, 2, 4, 8, 16]:
    return False
  elif n % 19 not in [0, 1, 11, 7]:
    return False
  elif n % 13 not in [0, 1, 12]:
    return False
  elif n % 7 not in [0, 1]:
    return False
  elif n % 5 not in [0, 1, 4]:
    return False
  else:
    return (round(n**(1 / 6))**6 == n)

# for n in range(2 * 10**5):
#   if is_sextic(n):
#     print(n)

N = 1000

for x1 in range(42, N, 42):
  for x2 in range(42, N, 42):
    for x3 in range(42, N, 42):
      for x4 in range(42, N, 42):
        for x5 in range(1, N):
          if is_sextic(x1**6 + x2**6 + x3**6 + x4**6 + x5**6):
            print(x1, x2, x3, x4, x5)