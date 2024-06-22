n = 5

for k1 in range(n):
  for k2 in range(n):
    for k3 in range(n):
      for k4 in range(n):
        for k5 in range(n):
          x1 = (42 * k1)**6 % n
          x2 = (42 * k2)**6 % n
          x3 = (42 * k3)**6 % n
          x4 = (7 * k4)**6 % n
          x5 = (6 * k5)**6 % n
          x6 = (x1 + x2 + x3 + x4 + x5) % n
          if x6 in [0, 1, 4]:
            print(x1, x2, x3, x4, x5, (x1 + x2 + x3 + x4 + x5) % n)
