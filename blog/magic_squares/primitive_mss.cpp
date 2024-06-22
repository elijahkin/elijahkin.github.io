#include <iostream>
#include <cmath>

bool is_square(uint64_t n) {
  if ((n % 5 == 2) || (n % 5 == 3)) {
    return false;
  }

  uint64_t root = floor(sqrt(n));
  return (root * root == n);
}

int main() {
  uint64_t c_lower = 1;
  uint64_t c_upper = 2 * pow(10, 9);

  int count = 0;

  for (uint64_t c = c_lower; c < c_upper; c += 24) {
    if (is_square(c)) {
      for (uint64_t a = 24; a < c / 2 + 1; a += 24) {
        if (is_square(c + a) && is_square(c - a)) {
          for (uint64_t b = a + 24; b < c - a; b += 24) {
            if (is_square(c + b) && is_square(c - b)) {
              count += 1;
              if (is_square(c + (a + b)) && is_square(c - (a + b)) && is_square(c + (a - b)) && is_square(c - (a - b))) {
                std::cout << a << " " << b << " " << c << std::endl;
              }
            }
          }
        }
      }
    }
  }

  std::cout << count << std::endl;

  return 0;
}