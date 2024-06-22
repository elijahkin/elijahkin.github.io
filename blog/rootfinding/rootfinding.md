## A Survey of Rootfinding Algorithms
**February 27th, 2024**

### Motivation
A critical problem in mathematics is to determine the roots of some given function $f$, that is, to solve the equation
$$ f(x) = 0. $$
For example, this problem may come up when trying to maximize or minimize some function -- it may be helpful to identify the points $x$ at which its derivative is $0$. For some functions, such as
$$ x \mapsto x^2 - 1 \text{ and } x \mapsto \sin(x) $$
it may be straightforward to determine roots by hand (the roots of the functions above are $\{-1, 1\}$ and $\{\pi k \mid k \in \mathbb{Z}\}$ respectively). However, for other functions this is simply not feasible. For example, consider
$$ f(x) \coloneqq \cos(x) - x. $$
One would encounter great difficulty in determining exactly the root(s) of $f$, but in the analysis that follows, we will explore how to prove that a root of $f$ exists, that there is exactly one, and four methods of approximating its value.

### Existence and Uniqueness
Continuing with our function $f$ as defined above, the existence of a root follows from the intermediate value theorem. Recalling from calculus:

TODO IVT

and so observing that
$$ f(0) = 1 > 0 \text{ and } f(\pi / 2) = - \pi / 2 < 0. $$
Hence, by the intermediate value theorem, there exists some root of $f$ on the interval $(0, \pi / 2)$. To see that this is the *only* root of $f$, we compute
$$ f'(x) = \sin(x) - 1 \leq 0 $$

TODO

which happens to have a root at $x \approx 0.7391$.

### Bisection Method

```cpp
int x = 0;
```

### False Position Method

```cpp
int x = 0;
```

### Newton's Method

```cpp
int x = 0;
```

### Secant Method

```cpp
int x = 0;
```

### References