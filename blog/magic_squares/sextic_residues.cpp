#include <iostream>
#include <math.h>

bool is_sextic(uint64_t n) {
  if ((n % 9 == 0) || (n % 9 == 1)) {
    if ((n % 8 == 0) || (n % 8 == 1)) {
      if ((n % 7 == 0) || (n % 7 == 1)) {
        return true;
      }
    }
  }
  return false;
}

int main() {
  for (uint64_t i = 0; i < 100000; i++) {
    if (is_sextic(i)) {
      std::cout << i << std::endl;
    }
  }

  uint64_t N = 100000;

  for (uint64_t x1 = 42; x1 < N; x1 += 42) {
    for (uint64_t x2 = 42; x2 < N; x2 += 42) {
      for (uint64_t x3 = 0; x3 < N; x3++) {
        for (uint64_t x4 = 0; x4 < N; x4++) {
          for (uint64_t x5 = 0; x5 < N; x5++) {
            if (is_sextic(pow(x1, 6))) {
              std::cout << x1 << std::endl;
            }
          }
        }
      }
    }
  }
  return 0;
}
