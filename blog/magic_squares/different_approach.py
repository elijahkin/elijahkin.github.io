'''
f
(7x_1)^6 + (7x_2)^6 + (7x_3)^6 + (7x_4)^6 + (7x_5)^6 + x_6^6 = y^6
'''

def is_sextic(n):
  if (n % 2 == 1) and (n % 3 == 1) and (n % 7 == 1):
    return round(n**(1 / 6))**6 == n
  else:
    return False

N = 30

for x1 in range(1, N):
  for x2 in range(x1, N):
    for x3 in range(x2, N):
      for x4 in range(1, N):
        for x5 in range(1, N):
          for x6 in range(1, N):
            y_pow = (42 * x1)**6 + (42 * x2)**6 + (42 * x3)**6 + (21 * x4)**6 + (7 * x5)**6 + x6**6
            if is_sextic(y_pow):
              print(x1, x2, x3, x4, x5, x6)