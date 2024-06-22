def sextic_residues(n):
  return set([a**6 % n for a in range(n)])

for n in range(1, 20):
  print(len(sextic_residues(n)) / n, n, sextic_residues(n))

# res = sextic_residues(72)
# print(res)
