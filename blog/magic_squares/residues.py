# Determine restrictions on S_2 for 5x5 associative bimagic squares

# S_2 cannot be congruent to 3 mod 8

def quadratic_residues(n):
  return set([a**2 % n for a in range(n)])

# Check 8, 32, 128, 512
for n in [8, 32, 128, 512]:
  residues = list(quadratic_residues(n))
  possibilities = set()

  for m_squared in residues:
    for x_squared in residues:
      for y_squared in residues:
        possibilities.add((5 * m_squared + 2 * x_squared + 2 * y_squared) % n)

  for x in set(range(n)).difference(possibilities):
    if x % 8 != 3 and x % 32 != 12:
      print(x)

  print(f'{n}: {len(possibilities)} {100 * len(possibilities) / n}')