#include <functional>
#include <iostream>

class Function {
private:
  std::function<double(double)> f;

public:
  Function(std::function<double(double)> f) { this->f = f; }

  // Perform n iterations of the bisection method
  double bisection(double a, double b, int n) {
    double x;
    for (int i = 0; i < n; i++) {
      x = (a + b) / 2;
      if (f(x) * f(a) < 0) {
        b = x;
      } else {
        a = x;
      }
      std::cout << x << std::endl;
    }
    return x;
  }

  // Perform n iterations of the false position method
  double false_position(double a, double b, int n) {
    double x;
    for (int i = 0; i < n; i++) {
      x = b - f(b) * (b - a) / (f(b) - f(a));
      if (f(x) * f(a) < 0) {
        b = x;
      } else {
        a = x;
      }
      std::cout << x << std::endl;
    }
    return x;
  }

  // Perform n iterations of Newton's method (method of tangents)
  double newtons_method(std::function<double(double)> df, double x, int n) {
    for (int i = 0; i < n; i++) {
      x -= f(x) / df(x);
      std::cout << x << std::endl;
    }
    return x;
  }

  // Perform n iterations of the secant method
  double secant_method(double x0, double x1, int n) {
    double x2;
    for (int i = 0; i < n; i++) {
      x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0));
      x0 = x1;
      x1 = x2;
      std::cout << x2 << std::endl;
    }
    return x2;
  }
};
