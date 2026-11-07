## Combinations without replacement

Given `n` distinct objects, the number of ways to select
`k` objects without regard to order is:

\[
\binom{n}{k} = \frac{n!}{k!(n-k)!}
\]

for \(0 \leq k \leq n\).

When \(k > n\), we define the number of combinations
as zero.

### Computational approach

The implementation uses:

\[
\binom{n}{k}
=
\prod_{i=1}^{k}
\frac{n-k+i}{i}
\]

after reducing `k` to `min(k, n-k)` by symmetry.

This avoids computing three factorials and retains
exact integer arithmetic.