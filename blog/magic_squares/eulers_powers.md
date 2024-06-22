### Euler's Sum of Powers
Here we attempt to solve
$$ a_1^6 = b_1^6 + b_2^6 + b_3^6 + b_4^6 + b_5^6 + b_6^6 $$

### Primitive Solutions
Suppose there exist non-negative integers $a_1$, $b_1$, $b_2$, $b_3$, $b_4$, $b_5$, and $b_6$ that satisfy the equation. We will call the solution **primitive** if
$$ \gcd(a_1, b_1, b_2, b_3, b_4, b_5, b_6) = 1 $$
Note that if there exists a non-primitive solution, then we can deduce a primitive solution (in which each integer is smaller) by dividing all integers by their $\gcd$.

Hence, if solutions exist, the minimal one is primitive, so we restrict ourselves to primitive solutions.

### Sextic Residues
One can easily deduce that mod 7, mod 8, and mod 9, the sextic residues are $\{0, 1\}$.

Then for a primitive solution, it must be that $a_1^6 \equiv 1 \mod 7$, since if $a_1^6 \equiv 0 \mod 7$, then the integers would all share the common factor $7$, and hence not be primitive. By the same reasoning, one finds that $a_1^6 \equiv 1 \mod 8$ and $a_1^6 \equiv 1 \mod 9$.

In particular this means that $a_1^6 = 504k + 1$. Further, from $a_1^6 \equiv 1 \mod 7$, we can deduce that five of $b_1^6$, $b_2^6$, $b_3^6$, $b_4^6$, $b_5^6$, and $b_6^6$ are congruent to $0 \mod 7$, meaning that five of $b_1$, $b_2$, $b_3$, $b_4$, $b_5$, $b_6$ are congruent to $0 \mod 7$. By the same logic, we find that five of $b_1$, $b_2$, $b_3$, $b_4$, $b_5$, $b_6$ are congruent to each of $0 \mod 2$ and $0 \mod 3$.

TODO Explain more here.

Then $b_1^6 = 42^6c_1^6$, $b_2^6 = 42^6c_2^6$, $b_3^6 = 42^6c_3^6$, $b_4^6 = 21^6c_4^6$, $b_5^6 = 7^6c_5^6$, and $b_6^6 = c_6^6$. Hence, the equation can be rewritten as

$$ a_1^6 = 42^6c_1^6 + 42^6c_2^6 + 42^6c_3^6 + 21^6c_4^6 + 7^6c_5^6 + c_6^6 $$

### References
https://www.ams.org/journals/mcom/2003-72-242/S0025-5718-02-01445-X/S0025-5718-02-01445-X.pdf
http://euler.free.fr/