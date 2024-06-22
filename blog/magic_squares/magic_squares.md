## Open Problems Concerning Magic Squares
**February 27th, 2024**

### $3 \times 3$ Magic Square of Squares

### $5 \times 5$ Bimagic Square

### $3 \times 3$ Semi-magic Square of Cubes

### Euler's Sum of Powers
> Find six positive integers $x_1, x_2, \dots, x_6$ such that
> $$ x_1^6 + x_2^6 + x_3^6 + x_4^6 + x_5^6 = x_6^6 $$
> or prove that such integers do not exist.

Though this problem is not strictly related to magic squares, it somehow feels in the same spirit, so I have included it anyway.

Note that the sextic residues $\mod 9$ are $\{0, 1\}$. Hence, either $x_6^6 \equiv 0 \mod 9$ or $x_6^6 \equiv 1 \mod 9$. If the former, then all five others are $\equiv 0 \mod 9$. If latter, then exactly four of the five others are $\equiv 0 \mod 9$. Hence, at least four of $x_1, x_2, x_3, x_4, x_5$ are divisible by $3$.

Analogously, at least four of $x_1, x_2, x_3, x_4, x_5$ are divisible by $2$, and at least four of $x_1, x_2, x_3, x_4, x_5$ are divisible by $7$.

Therefore, at least two of $x_1, x_2, x_3, x_4, x_5$ are divisible by $2 \cdot 3 \cdot 7 = 42$.

Look at this $\mod 72$. The sextic residues $\mod 72$ are $\{0, 1, 9, 64\}$

If $x_6^6 \equiv 0 \mod 7$, then we can derive a smaller solution, so we need only concentrate on when $x_6^6 \equiv 1 \mod 7$. Then let
$$ x_5^6 \equiv 1 \mod 7 \text{ and } x_6^6 \equiv 1 \mod 7 $$
so the other four are all divisible by $7$. Hence we have
$$ (7y_1)^6 + (7y_2)^6 + (7y_3)^6 + (7y_4)^6 + x_5^6 = x_6^6 $$

Continuing, at least three are divisible by $21$, 

$$ (21z_1)^6 + (21z_2)^6 + (21z_3)^6 + (7y_4)^6 + x_5^6 = x_6^6 $$

and finally at least two are divisible by $42$, so

$$ (42\alpha_1)^6 + (42\alpha_2)^6 + (21z_3)^6 + (7y_4)^6 + x_5^6 = x_6^6 $$

Can we figure out which case is it? If not divisible from 3 and 7 fall on the same $x_k$, then $x_k \equiv 1 \mod 21$

### References
* http://multimagie.com/
* http://www.openproblemgarden.org/op/a_sextic_counterexample_to_eulers_sum_of_powers_conjecture