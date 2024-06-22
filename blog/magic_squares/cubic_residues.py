def cubic_residues(n):
  residues = set()

  for a in range(n):
    residues.add(a**3 % n)
  return residues

print(cubic_residues(5))

for n in range(100):
  if len(cubic_residues(n)) == n:
    print(n)