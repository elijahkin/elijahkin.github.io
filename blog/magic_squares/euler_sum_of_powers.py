def is_sextic(n):
  if (n % 2 == 1) and (n % 3 == 1) and (n % 7 == 1):
    return round(n**(1 / 6))**6 == n
  else:
    return False

N = 200

# Version 1 of 5
for x1 in range(1, N):
  for x2 in range(x1, N):
    for x3 in range(x2, N):
      for x4 in range(x3, N):
        for x5 in range(1, N, 2):
          x6_sextic = (42 * x1)**6 + (42 * x2)**6 + (42 * x3)**6 + (42 * x4)**6 + x5**6
          if is_sextic(x6_sextic):
            print(x1, x2, x3, x4, x5)