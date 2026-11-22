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

Let $N$ be an integer with $N \ge 2$, and let $d$ be one of the divisors examined by FDP.

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

## 8. Conclusion of the Base Case

The construction:

$$
\boxed{7(2)(2) + 1(7)(39) + 2(4) = 309}
$$

provides a concrete example of how an expression visually dominated by factors of 7 and even factors can produce a number divisible by 3 and not divisible by 7 or 2.

This supports three design decisions of FDP:

1. Examine the **resulting number**, regardless of the factors used to construct it.
2. Apply **exact divisibility**, without resorting to inferences based on algebraic appearance.
3. **Stop evaluation at the first proper divisor found**, avoiding unnecessary subsequent operations.

Mathematical result of the base case:

$$
\boxed{\text{FDP}(309) = (\text{COMPOSITE},\, 3,\, 103)}
$$

The case constitutes a verifiable justification of the correctness and early termination of the filter. Sections 9 and 10 extend the analysis to two complementary operations on the candidate: scalar multiplication and additive shift.

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

## 10. Controlled Divisor Selection via Additive Shifts

Section 9 established that scalar multiplication preserves an existing divisor and leaves the position of the detected divisor within $D$ invariant. The present section establishes the dual behavior: an additive shift modifies the residue class of the candidate, and therefore may change the position within $D$ at which FDP first detects a divisor.

### 10.1 Base construction

Let:

$$
B = 17 \times 13 \times 37 \times 103 = 842{,}231
$$

The base is the product of four primes. Its residue modulo 3 is:

$$
842{,}231 \bmod 3 = 2
$$

### 10.2 Proposition 6 — Congruence under additive shift

Let $B, a, d \in \mathbb{Z}$ with $d \ge 2$. Then:

$$
(B + a) \bmod d = \big((B \bmod d) + (a \bmod d)\big) \bmod d
$$

**Proof.** Direct consequence of the compatibility of congruence with addition. $\blacksquare$

### 10.3 Corollary 6.1 — Residue class dependence

For fixed $B$ and fixed $d \ge 2$, the residue $(B + a) \bmod d$ depends only on the residue class $a \bmod d$.

**Proof.** By Proposition 6, the value $(B + a) \bmod d$ is determined by $B \bmod d$ and $a \bmod d$. The former is fixed; the latter is invariant under changes of $a$ within its residue class modulo $d$. $\blacksquare$

### 10.4 Application to the base $B = 842{,}231$

With $B \bmod 3 = 2$ and $d = 3$, Proposition 6 specializes to:

$$
(B + a) \bmod 3 = (2 + a \bmod 3) \bmod 3
$$

Three cases follow:

- If $a \equiv 1 \pmod 3$: $(B + a) \bmod 3 = (2 + 1) \bmod 3 = 0$.
- If $a \equiv 2 \pmod 3$: $(B + a) \bmod 3 = (2 + 2) \bmod 3 = 1$.
- If $a \equiv 0 \pmod 3$: $(B + a) \bmod 3 = (2 + 0) \bmod 3 = 2$.

### 10.5 Case study: shifts $a \in \{1, 3, 4, 7\}$

The shifts $1, 4, 7$ satisfy $a \equiv 1 \pmod 3$ and therefore produce candidates divisible by 3. The shift $3$ satisfies $a \equiv 0 \pmod 3$ and produces a candidate with residue 2 modulo 3, which FDP then examines modulo 2.

| $a$ | $a \bmod 3$ | $B + a$ | First FDP divisor | Quotient | Checks executed |
|:---:|:-----------:|:-------:|:-----------------:|:--------:|:---------------:|
| 1 | 1 | 842,232 | 3 | 280,744 | 1 |
| 4 | 1 | 842,235 | 3 | 280,745 | 1 |
| 7 | 1 | 842,238 | 3 | 280,746 | 1 |
| 3 | 0 | 842,234 | 2 | 421,117 | 2 |

FDP verdicts:

```text
FDP(842232) = ("COMPOSITE", 3, 280744)   # 1 check
FDP(842235) = ("COMPOSITE", 3, 280745)   # 1 check
FDP(842238) = ("COMPOSITE", 3, 280746)   # 1 check
FDP(842234) = ("COMPOSITE", 2, 421117)   # 2 checks
```

### 10.6 Quantification of FDP execution

- Candidates evaluated: $4$.
- Candidates classified as composite by FDP: $4/4$.
- Checks executed under early termination: $1 + 1 + 1 + 2 = 5$.
- Checks under full evaluation of all four divisors: $4 \times 4 = 16$.
- Checks avoided: $16 - 5 = 11$.
- Reduction in divisibility checks: $11/16 = 68.75\%$.

### 10.7 Proposition 7 — Dual behavior with respect to Section 9

The FDP filter satisfies the following two complementary properties:

**(i) Multiplicative invariance.** If $d \mid N$, then $d \mid (N \cdot m)$ for every integer $m \ge 1$ (Proposition 4). Multiplication preserves every existing divisor of $N$.

**(ii) Additive displacement.** If $a_1 \equiv a_2 \pmod d$, then $(B + a_1) \equiv (B + a_2) \pmod d$ (Corollary 6.1). Conversely, if $a_1 \not\equiv a_2 \pmod d$, the residue class of the candidate modulo $d$ may differ, and the position within $D$ at which FDP first detects a divisor may change accordingly.

<img width="1320" height="957" alt="image" src="https://github.com/user-attachments/assets/8ecb634a-4835-46d3-941d-40e30f41e3ab" />


**Proof.** Part (i) is Proposition 4. Part (ii) is Corollary 6.1. $\blacksquare$

### 10.8 Formal consequence

For a fixed base $B$, the additive term $a$ acts as a control parameter on the residue class of the candidate $B + a$ modulo each divisor in $D$, and therefore on the position within $D$ at which FDP first detects a divisor.

In the case $B = 842{,}231$:

$$
\boxed{\forall a \in \{1, 4, 7\},\quad \text{FDP}(B + a) = (\text{COMPOSITE},\, 3,\, (B + a)/3)}
$$

$$
\boxed{\text{FDP}(B + 3) = (\text{COMPOSITE},\, 2,\, (B + 3)/2)}
$$

The four candidates lie within an interval of width $6$. The residue class of the additive shift, not the magnitude of the candidate, determines which divisor FDP detects first. FDP executes this classification through exact integer arithmetic and terminates at the first successful check, consistent with Proposition 3.

---

<div align="center">

**SPARTACO / FDP**

*The appearance is a guess. The residue is the evidence.*

**Verify the mathematics.**

</div>
