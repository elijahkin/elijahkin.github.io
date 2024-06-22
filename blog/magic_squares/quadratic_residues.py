# Check quadratic residues mod n
n = 7

quadratic_residues = set()
for x in range(n):
  quadratic_residues.add(x**2 % n)
print(f'Quadratic residues mod {n}: {quadratic_residues}')

for c in range(n):
  if c not in quadratic_residues:
        continue
  for a in range(n):
    if (c + a) % n not in quadratic_residues:
        continue
    elif (c - a) % n not in quadratic_residues:
        continue
    for b in range(n):
      if (c + b) % n not in quadratic_residues:
        continue
      elif (c - b) % n not in quadratic_residues:
        continue
      elif (c + (a + b)) % n not in quadratic_residues:
        continue
      elif (c - (a + b)) % n not in quadratic_residues:
        continue
      elif (c + (a - b)) % n not in quadratic_residues:
        continue
      elif (c - (a - b)) % n not in quadratic_residues:
        continue
      else:
        print(f'a={a}, b={b}, c={c}')