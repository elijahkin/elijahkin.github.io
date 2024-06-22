def cubic_residues(n):
  return set([a**3 % n for a in range(n)])

for n in range(1, 10**5):
  if len(cubic_residues(n)) < 0.028 * n:
    print(n, len(cubic_residues(n)) / n)

n = 2**3 * 3**3 * 7 * 13 * 41
print(n, len(cubic_residues(n)) / n)

# A + B - C
n = 4
cub_res = cubic_residues(n)

# for a in cub_res:
#   for b in cub_res:
#     for c in cub_res:
#       if (a + b - c) % n in cub_res:
#         print(a, b, c, (a + b - c) % n)
#       else:
#         print(a, b, c, "BAD")