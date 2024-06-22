import numpy as np

# We conjecture the center entry of an associative 5x5
# magic squares is divisible by 4.

count = 0

# Generate the top two rows of the square
for n in range(8**10):
  bin_top = [int(d) for d in oct(n)[2:]]
  bin_top = [0] * (10 - len(bin_top)) + bin_top
  top = np.array(bin_top).reshape(2, 5)

  # If the two top rows do not sum to the same thing
  # then we need not proceed any further
  top_sum = top.sum(axis = 1) % 8
  magic_constant = top_sum[0]
  if (top_sum[1] == magic_constant):
    # The top and bottom should reflect around center
    bot = 8 - np.flip(top)

    # Sums of bottom rows must also be congruent to magic constant
    if np.all(bot.sum(axis = 1) % 8 == magic_constant):
      # Compute the middle row (makes summing down columns unnecessary)
      mid = np.array([[magic_constant] * 5])
      mid -= (top[0] + top[1] + bot[0] + bot[1])
      mid = mid % 8

      # Stitch the pieces together
      square = np.concatenate((top, mid, bot))

      # If we reach this point, it should be
      # guaranteed to be a magic square.
      # We now want to check if it is bimagic
      square2 = square**2 % 8
      square_row_sum = square2.sum(axis = 0) % 8
      square_col_sum = square2.sum(axis = 1) % 8
      if np.all(square_row_sum == square_row_sum[0]):
        if np.all(square_col_sum == square_row_sum[0]):
          if np.trace(square2) == square_row_sum[0]:
            if np.trace(np.flip(square2, axis=1)) == square_row_sum[0]:
              count += 1
              print(square)

print(count)
