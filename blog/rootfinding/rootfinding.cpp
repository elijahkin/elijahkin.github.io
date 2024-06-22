#include "function.h"
#include <cmath>
#include <iomanip>

int main() {
  std::cout << std::setprecision(15);
  Function myfun = Function([](double x) -> double { return cos(x) - x; });

  std::cout << "Bisection Method:" << std::endl;
  myfun.bisection(0, 2, 6);

  std::cout << "\nFalse Position Method:" << std::endl;
  myfun.false_position(0, 2, 6);

  std::cout << "\nNewton's Method:" << std::endl;
  myfun.newtons_method([](double x) -> double { return -sin(x) - 1; }, 1, 6);

  std::cout << "\nSecant Method:" << std::endl;
  myfun.secant_method(0, 1, 6);
  return 0;
}