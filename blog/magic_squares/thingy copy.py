def sextic_residues(n):
  return set([a**6 % n for a in range(n)])

# n = 42
# for n in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
for n in [13]:
  res = sextic_residues(n)
  # print(res)

  count = 0
  for x1 in res:
    for x2 in res:
      for x3 in res:
        for x4 in res:
          for x5 in res:
            if (42**6 * x1 + 42**6 * x2 + 21**6 * x3 + 7**6 * x4 + x5) % n in res:
              count += 1
            else:
              print(x1, x2, x3, x4, x5, (42**6 * x1 + 42**6 * x2 + 21**6 * x3 + 7**6 * x4 + x5) % n)
  print(n, count / len(res)**5)

# print(sextic_residues(19))
# print(sextic_residues(31))

# for n in range(20):
#   print(n, sextic_residues(n))

# print(sextic_residues(13))

# 5, 11, 13, 17, 19

# 0 - not primitive
# 1 0 0 0 1, 0
# 12 0 0 0 12, 0 12 1 12
