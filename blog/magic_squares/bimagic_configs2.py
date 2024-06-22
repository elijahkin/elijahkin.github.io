import numpy as np

def quadratic_residues(n):
  return set([a**2 % n for a in range(n)])

# Convert n to base b and pad to 10 digits
def base(n, b):
  digits = [0] * 10
  for k in range(9, -1, -1):
    d = n // b**k
    if d != 0:
      n -= d * b**k
      digits[9 - k] = d
  return digits

# We try to figure out the structure mod 8 of the squared square
count = 0
for n in range(3**10):
  # Convert to base 3 since there are 3 quadratic residues mod 8
  top = np.array(base(n, 3)).reshape(2, 5)

  # Replace 2 with 4 (the quadratic residues mod 8 are 0, 1, 4)
  top[top == 2] = 4

  # If the top two rows are not congruent mod 8, we don't need to proceed
  row_sum = top.sum(axis = 1) % 8
  magic_constant = row_sum[0]
  if (row_sum[1] == magic_constant):

    # Iterate through each possible pair sum
    for pair_sum in range(8):
      # Corresponding elements in the top and bot
      # should always add up to pair_sum mod 8
      bot = (pair_sum - np.flip(top)) % 8

      # Sum of bottom two rows must also be conguent to the magic constant
      bot_sum = bot.sum(axis = 1) % 8
      if (bot_sum[0] == magic_constant) and (bot_sum[1] == magic_constant):
        # In order to be squares, bot should consist
        # entirely of 0, 1, 4
        if not (np.any(bot == 2) or np.any(bot == 3) or np.any(bot == 5) or np.any(bot == 6) or np.any(bot == 7)):
          # Compute the missing middle row
          mid = np.array([[magic_constant] * 5])
          mid -= (top[0] + top[1] + bot[0] + bot[1])
          mid = mid % 8

          mss = np.concatenate((top, mid, bot))

          # Now we start testing conjectures (513 possibilities)

          # Conjecture 1
          if not np.all((mss == 0) + (mss == 4)):
            # From here we see all either all entries in the squared square
            # are divisible by 4 (suggesting all entries in the bimagic square
            # are even) or all entries are congruent to 1 mod 8 (suggesting all
            # entries in the bimagic square are odd).
            print(mss)
            print(magic_constant)
          count += 1

          # Conjecture 2
          # The magic constant is the center entry + 2 * pair_sum
          if mss[2][2] != magic_constant:
            print(mss)
            print(magic_constant)

          # Conjecture 3
          # From any bimagic consisting of entirely even entries
          # there exists a bimagic square of entirely odd entries

print(count)

# We now begin the search for all odd bimagic square
N = 10
for a in range(1, N):
  for b in range(1, N):
    for c in range(1, N):
      for d in range(1, N):
        for e in range(1, N):
          s1 = a + b + c + d + e
          if s1 % 5 == 0:
            s2 = a**2 + b**2 + c**2 + d**2 + e**2
            for f in range(1, N):
              print(s1, s2)