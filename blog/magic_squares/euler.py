def is_sextic(n):
  if (n % 2 == 1) and (n % 3 == 1) and (n % 7 == 1):
    return round(n**(1 / 6))**6 == n
  else:
    return False

# for i in range(10**8):
#   if is_sextic(i):
#     print(i)

N = 50

for x1 in range(1, N):
  for x2 in range(x1, N):
    for x3 in range(1, N):
      for x4 in range(1, N):
        for x5 in range(1, N):
          tmp = (42 * x1)**6 + (42 * x2)**6 + (21 * x3)**6 + (7 * x4)**6 + x5**6
          if is_sextic(tmp):
            print(x1, x2, x3, x4, x5)
            print(tmp, tmp**(1 / 6))