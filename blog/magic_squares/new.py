for n in range(20):
  s2_residues = set()

  for a in range(n):
    for b in range(n):
      for c in range(n):
        for d in range(n):
          for e in range(n):
            s1 = a + b + c + d + e
            if s1 % 5 == 0:
              s2 = a**2 + b**2 + c**2 + d**2 + e**2
              s2_residues.add(s2 % n)
  if len(s2_residues) != n:
    print(n, s2_residues)