<div align="center">

# SPARTACO / FDP

### DETERMINISTIC PRELIMINARY FILTER — B1

**Exact divisibility · Sequential divisor evaluation · Early termination**

*A mathematical justification from SPARTACO SECURITY / OMEGA337.*

**Inspect the algebra. Verify the residues. Confirm the verdict.**

</div>

---

## 1. Objective

Justify the use of the independent **FDP** filter, based on exact divisibility and sequential evaluation of the divisors `(3, 2, 7, 5)`, through an algebraic construction example involving factors of 7, 2, and 4 — but whose result is divisible by 3.

The purpose is to demonstrate that the factors used to construct an expression do not, by themselves, determine all the divisors of the result of its sums.

---

## 2. Construction of the Number

The following expression is proposed:

$$
N = (7 \times 2 \times 2) + (1 \times 7 \times 39) + (2 \times 4)
$$

Calculating each term:

$$
N = 28 + 273 + 8
$$

Therefore:

$$
\boxed{N = 309}
$$

The construction uses multiplications and additions with a prominent presence of factor 7 and even factors.

However, that presence does not guarantee that the result is divisible by 7 or by 2.

---

## 3. Analysis of the Algebraic Structure

We group the terms containing factor 7:

$$
N = 7(4 + 39) + 8
$$

$$
N = 7(43) + 8
$$

Since $8 = 7 + 1$:

$$
N = 7(44) + 1
$$

Therefore:

$$
\boxed{309 \bmod 7 = 1}
$$

The number is **not divisible by 7**, although two of the three original terms contain that factor.

Moreover:

$$
309 \bmod 2 = 1
$$

The result is also **not divisible by 2**, although the construction contains several even factors.

---

## 4. Appearance of Divisibility by 3

We evaluate the residues of the three original terms modulo 3:

$$
28 \bmod 3 = 1
$$

$$
273 \bmod 3 = 0
$$

$$
8 \bmod 3 = 2
$$

Adding the residues:

$$
1 + 0 + 2 = 3
$$

And since:

$$
3 \bmod 3 = 0
$$

we obtain:

$$
\boxed{309 \bmod 3 = 0}
$$

Therefore:

$$
309 = 3 \times 103
$$

The constructed number is **composite**.

> **Observation.** The term $273 = 7 \times 39$ already contains factor 3. However, the divisibility of the complete sum depends on the combination of the residues of *all* its terms.

---

## 5. Application of the FDP Filter

The filter evaluates the divisors in the following order:

$$
D = (3, 2, 7, 5)
$$

Upon receiving the candidate $N = 309$, it executes its first check:

$$
309 \bmod 3 = 0
$$

Exact division yields:

$$
309 \div 3 = 103
$$

Consequently, it returns:

```text
FDP(309)
# ("COMPOSITE", 3, 103)
```

Execution terminates without needing to check divisors 2, 7, and 5.

Factor 103 is prime, so the complete factorization is:

$$
\boxed{309 = 3 \times 103}
$$

---

## 6. Mathematical Justification of the Filter

### Proposition 1 — Exact detection of composition

Let $N$ be an integer greater than or equal to 2, and let $d$ be one of the divisors examined by FDP.

If:

$$
1 < d < N
$$

and:

$$
N \bmod d = 0
$$

then there exists an integer $q = N/d > 1$ such that:

$$
N = d \cdot q
$$

By definition, $N$ is composite.

**Proof.** Exact division provides two integer factors greater than 1. Therefore, the `COMPOSITE` result emitted by FDP is mathematically justified. $\blacksquare$

### Proposition 2 — Independence from construction

The divisibility of a sum is determined by the residue of the complete expression, not solely by the factors present in its individual terms.

For any positive integer $d$:

$$
(A + B + C) \bmod d = \big((A \bmod d) + (B \bmod d) + (C \bmod d)\big) \bmod d
$$

The example of 309 demonstrates this property simultaneously for divisors 3 and 7.

### Proposition 3 — Early termination

If FDP finds an exact divisor at a position in its sequence, subsequent checks are unnecessary to establish that the candidate is composite.

In the case of 309, a single divisibility check is sufficient.

---

## 7. Architectural Justification

FDP can operate as an independent component of the main auditor.

Its responsibility is limited to identifying compositions through exact divisibility by a small, predetermined set of divisors.

The proposed flow is:

$$
N \longrightarrow \text{FDP}(N)
$$

- If FDP finds a proper divisor, it returns an elementary **certificate of composition**: divisor and quotient.
- If FDP finds none, it returns `PASSES_FILTER`, leaving the candidate available for subsequent audit procedures.

The order $(3, 2, 7, 5)$ is an **explicit evaluation policy**. The example of 309 justifies the convenience of examining 3 first for that candidate; this is deliberate at the architectural level.

| Position | Divisor | Role in the case $N = 309$ |
|:--------:|:-------:|:---------------------------|
| 1 | 3 | **Exact divisor found** — yields `103`, terminates |
| 2 | 2 | Skipped — unnecessary |
| 3 | 7 | Skipped — unnecessary |
| 4 | 5 | Skipped — unnecessary |

---

## 8. Conclusion

The construction:

$$
\boxed{7(2)(2) + 1(7)(39) + 2(4) = 309}
$$

provides a concrete example of how an expression visually dominated by factors of 7 and even factors can produce a number divisible by 3 and not divisible by 7 or 2.

This supports three design decisions of FDP:

1. Examine the **resulting number**, regardless of the factors used to construct it.
2. Apply **exact divisibility**, without resorting to inferences based on algebraic appearance.
3. **Stop evaluation at the first proper divisor found**, avoiding unnecessary subsequent operations.

Mathematical result of the case:

$$
\boxed{\text{FDP}(309) = (\text{COMPOSITE},\, 3,\, 103)}
$$

The case constitutes a verifiable justification of the correctness and early termination of the filter.

---

## 9. Hereditary Divisibility Under Scalar Multiplication

### Proposition 4 — Hereditary divisibility

Let $d, N, m \in \mathbb{Z}$ with $d \ge 2$, $N \ge 2$, $m \ge 1$. If $d \mid N$, then:

$$
d \mid (N \cdot m)
$$

**Proof.** If $d \mid N$, there exists $k \in \mathbb{Z}$ such that $N = dk$. Then:

$$
N \cdot m = d\,(k m)
$$

Since $km \in \mathbb{Z}$, it follows that $d \mid (N \cdot m)$. $\blacksquare$

### Corollary 4.1 — Preservation of the factor 3 under powers of 7

Let $N = 309$ and $d = 3$. Since $309 \bmod 3 = 0$, Proposition 4 gives:

$$
3 \mid (309 \cdot 7^k) \quad \text{for every } k \ge 0
$$

### Proposition 5 — Invariance of first-check detection under scaling

Let $N_k = 309 \cdot 7^k$ for $k \ge 0$. Under the FDP divisor order $D = (3, 2, 7, 5)$:

$$
\text{FDP}(N_k) = (\text{COMPOSITE},\, 3,\, N_k/3) \quad \text{for every } k \ge 0
$$

**Proof.** By Corollary 4.1, $3 \mid N_k$. Since 3 occupies the first position of $D$, the first check of FDP succeeds. By Proposition 3, execution terminates at that check without evaluating divisors 2, 7, or 5. $\blacksquare$

### Application to the case $k = 3$

$$
N_3 = 309 \times 7^3 = 309 \times 343 = 105{,}987
$$

First check:

$$
105{,}987 \bmod 3 = 0
$$

Exact division:

$$
105{,}987 \div 3 = 35{,}329
$$

Full factorization:

$$
35{,}329 = 103 \times 7^3
$$

Therefore:

$$
\boxed{105{,}987 = 3 \times 103 \times 7^3}
$$

### Family of candidates and first-check behavior

For $N_k = 309 \cdot 7^k$:

| $k$ | $N_k = 309 \cdot 7^k$ | First check | Quotient | Verdict |
|:---:|:----------------------:|:-----------:|:--------:|:-------:|
| 0 | 309 | $309 \bmod 3 = 0$ | 103 | COMPOSITE |
| 1 | 2,163 | $2{,}163 \bmod 3 = 0$ | 721 | COMPOSITE |
| 2 | 15,141 | $15{,}141 \bmod 3 = 0$ | 5,047 | COMPOSITE |
| 3 | 105,987 | $105{,}987 \bmod 3 = 0$ | 35,329 | COMPOSITE |

### Formal consequence

By Propositions 4 and 5, the parameter $k$ does not affect the position of the detected divisor within $D$. Scalar multiplication by powers of 7 preserves the divisibility already present in $N$ and leaves the first-check verdict of FDP invariant.

Hence, for the family $\{N_k\}_{k \ge 0}$:

$$
\boxed{\forall k \ge 0,\quad \text{FDP}(N_k) = (\text{COMPOSITE},\, 3,\, N_k/3)}
$$

The size of the candidate grows with $k$; the position of the detected divisor within $D$ does not change.

---

<div align="center">

**SPARTACO / FDP**

*The appearance is a guess. The residue is the evidence.*

**Verify the mathematics.**

</div>
