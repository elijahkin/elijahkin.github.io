import random

'''
a b c d e
f g h i j
k l m n o
p q r s t
u v w x y
'''

1 + 2 + 3 + 4 + 5

'''
G G G G G
G G G G E
G G G ? ?
G E ? ? ?
E E ? ? ?
'''

N = 100

while True:
  a = random.randint(1, N)
  b = random.randint(1, N)
  if b not in [a]:
    c = random.randint(1, N)
    if c not in [a, b]:
      d = random.randint(1, N)
      if d not in [a, b, c]:
        e = random.randint(1, N)
        if e not in [a, b, c, d]:
          magic_sum = a + b + c + d + e
          squared_magic_sum = a**2 + b**2 + c**2 + d**2 + e**2
          f = random.randint(1, magic_sum - a - 2)
          if f not in [a, b, c, d, e]:
            k = random.randint(1, magic_sum - a - f - 1)
            if k not in [a, b, c, d, e, f]:
              # Need to ensure u is at least 1
              p = random.randint(1, magic_sum - a - f - k)
              if p not in [a, b, c, d, e, f, k]:
                u = magic_sum - a - f - k - p
                if u not in [a, b, c, d, e, f, k, p]:
                  if u**2 == squared_magic_sum - a**2 - f**2 - k**2 - p**2:
                    g = random.randint(1, N)
                    if g not in [a, b, c, d, e, f, k, p, u]:
                      h = random.randint(1, N)
                      if h not in [a, b, c, d, e, f, k, p, u, g]:
                        i = random.randint(1, N)
                        for i in range(1, magic_sum - f - g - h):
                          if i not in [a, b, c, d, e, f, k, p, u, g, h]:
                            j = magic_sum - f - g - h - i
                            if j not in [a, b, c, d, e, f, k, p, u, g, h, i]:
                              if j**2 == squared_magic_sum - f**2 - g**2 - h**2 - i**2:
                                for l in range(1, N):
                                  if l not in [a, b, c, d, e, f, k, p, u, g, h, i, j]:
                                    for q in range(1, magic_sum - b - g - l):
                                      if q not in [a, b, c, d, e, f, k, p, u, g, h, i, j, l]:
                                        v = magic_sum - b - g - l - q
                                        if v not in [a, b, c, d, e, f, k, p, u, g, h, i, j, l]:
                                          if v**2 == squared_magic_sum - b**2 - g**2 - l**2 - q**2:
                                            print(a, b, c, d, e, f, k, p, u, g, h, i, j, l, q, v)
