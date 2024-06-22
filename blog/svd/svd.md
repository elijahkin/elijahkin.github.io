## Image Compression with SVD
**February 27th, 2024**

### Eigenvalues & Diagonalization
Recall from linear algebra that an **eigenvector** of a square matrix $A \in \mathbb{R}^{n \times n}$ is a vector $\textbf{x} \in \mathbb{R}^n$ such that
$$ A\textbf{x} = \lambda\textbf{x} $$
for some scalar $\lambda \in \mathbb{R}$, called the **eigenvalue**.

To give a concrete example, consider
$$ A = \begin{bmatrix} 3 & 1 \\ 2 & 4 \end{bmatrix} $$
TODO

We will now discuss how to find eigenvalues. It can be shown that the eigenvalues of a matrix $A$ are exactly the solutions to the equation $\det(A - \lambda I) = 0$. The polynomial $\det(A - \lambda I)$ is sometimes called the **characteristic polynomial** of $A$.

Using our example matrix from earlier,
$$ A - \lambda I = \begin{bmatrix} 3 & 1 \\ 2 & 4 \end{bmatrix} - \lambda \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 3 - \lambda & 1 \\ 2 & 4 - \lambda \end{bmatrix} $$
and so taking its determinant and factoring, we find
$$ \det(A - \lambda I) = \lambda^2 - 5\lambda + 10 = (\lambda - 2)(\lambda - 5)$$
Hence, the eigenvalues of $A$ are $\lambda = 2$ and $\lambda = 5$, since these are the values for which $\det(A - \lambda I) = 0$.

### Singular Value Decomposition (SVD)
TODO

$$ M = U \Sigma V^* $$

### Compression
$nm$ versus $k(n + m + 1)$


### Examples
1 2 3

4 5 6

### References