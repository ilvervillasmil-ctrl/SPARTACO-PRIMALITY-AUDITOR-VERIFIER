# UIS–TANA–OMEGA / SPARTACO

## Nodal–Algebraic Coupling Theorem and deterministic primality certification

**Author:** Ilver Villasmil  
**Document:** Mathematical treatise, ordered by logical dependency  
**Edition:** November 13, 2026

---

## 0. Conventions, scope, and declarations

### 0.1 Nature of the certification

The primality criteria in this treatise are **deterministic**. The search for witnesses can be costly or use heuristic strategies. The validity of a certificate that satisfies all the conditions of a criterion is deductive and exact.

### 0.2 Statement labels

| Label | Meaning |
|---|---|
| **[TEO]**, **[LEM]**, **[COR]**, **[PROP]** | Statement with a complete proof in this document. |
| **[CLASSICAL]** | Classical external result used as authority: Fermat, Lagrange, Pocklington (1914), Lehmer (1930), Morrison (1975), Hasse. |

### 0.3 Notation

Each main formula has an identifier `F-nn` and a name.

| Symbol | Meaning |
|---|---|
| $N$ | Integer greater than 1, object of the certification. |
| $\ell, p, q, r$ | Prime numbers. |
| $\lfloor\sqrt{N}\rfloor$ | Integer square root: the largest integer $r$ with $r^2 \le N$. |
| $\text{ord}_\ell(a)$ | Multiplicative order of $a$ modulo $\ell$, with $\ell \nmid a$. |
| $\gcd(x, y)$ | Greatest common divisor. |
| $(D/N)$ | Jacobi symbol. |
| $U_n(P, Q)$ | Lucas sequence of the first kind: $U_0 = 0$, $U_1 = 1$, $U_{n+2} = P \cdot U_{n+1} - Q \cdot U_n$. In this document $Q = 1$ and $D = P^2 - 4$. |
| $v_r(m)$ | Exponent of $r$ in the factorization of $m$. |

### 0.4 Logical dependency map

```text
§1 Fundamentals ──► §2 SPARTACO Framework ──► §3 Clamp ──┐
                                                     ├─► §4 Closure by congruence ─► §5 Pocklington ─► §5.5 Ladder
§6 Lucas (character identity, existence) ────────────┴─► §7 UIS Branches (T–B1, T–B2, T–B4, T–B5)
§8 Windows and ancestors ── §9 Elliptic restrictions
§10 Certification, traceability and termination ─► §11 Evidence format and verifier
§12 Documentary evidence ─► §13 Logic of certification
```

---

## 1. Fundamentals

**DEF-1 (Prime divisors of exploration).** For an integer $N > 1$:

```math
\text{F-01 · Exploration set: } \Omega_N = \{ \ell \text{ prime} : \ell \le \sqrt{N} \}
```

```math
\text{F-02 · Prime divisors of exploration: } D_N = \{ \ell \in \Omega_N : \ell \text{ divides } N \}
```

**TEO-1 [TEO] (Fundamental characterization).** Let $N > 1$. Then

```math
\text{F-03 · Primality characterization: } N \text{ is prime} \iff D_N = \varnothing
```

**Proof.** $(\Rightarrow)$ If $N$ is prime, its only prime divisor is $N$, and $N > \sqrt{N}$. Therefore no prime $\ell \le \sqrt{N}$ divides it. $(\Leftarrow)$ Suppose $N$ is composite. Then $N = ab$ with $1 < a \le \sqrt{N}$. Every prime divisor of $a$ is a prime $\le a \le \sqrt{N}$ that divides $N$, and therefore belongs to $D_N$. Thus $D_N \neq \varnothing$. $\square$

---

## 2. TANA Framework: memory of restrictions and closure

**DEF-2 (Valid restriction).** A set $Q$ of prime numbers is a **valid restriction** on $N$ if it has been proven that $D_N \subseteq Q$. An empirical observation is not enough.

**DEF-3 (Nodal memory).** Given valid restrictions $Q_1, \ldots, Q_k$:

```math
\text{F-04 · Initial memory: } M_0 = \Omega_N
```

```math
\text{F-05 · Memory after } i \text{ restrictions: } M_i = M_{i-1} \cap Q_i \quad (i = 1, \ldots, k)
```

**TEO-2 [TEO] (TANA-D1, preservation).** For each $i$, $D_N \subseteq M_i$.  
**Proof.** For $M_0 = \Omega_N$ it holds by definition of $D_N$. If $D_N \subseteq M_{i-1}$ and $D_N \subseteq Q_i$, then $D_N \subseteq M_{i-1} \cap Q_i = M_i$. $\square$

**TEO-3 [TEO] (TANA-D2, contraction).** $M_i \subseteq M_{i-1}$. It is immediate from the definition of intersection. $\square$

**TEO-4 [TEO] (TANA-D3, deterministic closure).** If $M_k = \varnothing$, then $N$ is prime.  
**Proof.** By TEO-2, $D_N \subseteq M_k = \varnothing$. Therefore $D_N = \varnothing$, and TEO-1 concludes. $\square$

The closure is universal: no binary length alters this implication. Efficiency depends on the ability to construct sufficiently informative restrictions.

**PROP-1 [TEO] (Independence of order and repetition).** The final memory $M_k$ does not depend on the order in which the restrictions are applied, nor on whether a restriction is applied more than once.  
**Proof.** Set intersection is commutative, associative, and idempotent. $\square$

**PROP-2 [TEO] (Dominance and redundancy).** If $Q_j \subseteq Q_i$, the restriction $Q_i$ is redundant: removing it does not change $M_k$. Adding a valid restriction never expands the memory, and therefore never undoes an already reached closure.  
**Proof.** If $Q_j \subseteq Q_i$, then $Q_j \cap Q_i = Q_j$. The rest follows from TEO-3. $\square$

**COR-1 [TEO] (Composition of independent criteria).** Let $Q_1$ be obtained by Pocklington, $Q_2$ by Lucas, and $Q_3$ by the Clamp, all valid. If $Q_1 \cap Q_2 \cap Q_3 = \varnothing$, then $N$ is prime.  
**Proof.** Each $Q_i$ is a valid restriction. TEO-4 is applied. $\square$  
*Consequence:* there can be a closure in which no restriction by itself reaches the void, but their intersection does.

---

## 3. The Clamp (La Pinza): exact exclusion

**TEO-5 [TEO] (Exclusion by the Clamp).** Let $B \ge 1$. If $N \bmod \ell \neq 0$ for all primes $\ell \le B$, then

```math
\text{F-06 · Clamp restriction: } D_N \subseteq \{ \ell \text{ prime} : B < \ell \le \sqrt{N} \}
```

If additionally $B \ge \lfloor\sqrt{N}\rfloor$, the set on the right is empty and $N$ is prime.  
**Proof.** It is a direct consequence of the definition of $D_N$ and TEO-1. $\square$

**Observation 3.1 (partial coverage).** If $B < \lfloor\sqrt{N}\rfloor$, the Clamp only proves that $N$ has no prime divisors $\le B$. It does not prove primality. Example: $B = 5$ and $N = 49 = 7 \cdot 7$. No prime $\le 5$ divides 49, and yet 49 is composite. A result of this type is a restriction (F-06), and it is combined with others according to §2 and §4.

**Observation 3.2 (root of the ladder).** In the certified ladder (§5.5), the root $q_0$ is established by the Clamp with $B = \lfloor\sqrt{q_0}\rfloor$.

---

## 4. Closure by congruence

**TEO-6 [TEO] (Closure by arithmetic progression).** Let $F \ge 1$ be an integer. Suppose that every prime divisor $\ell$ of $N$ satisfies $\ell \equiv 1 \pmod F$. If

```math
\text{F-07 · Closure condition by progression: } (F + 1)^2 > N \quad (\text{equivalent to } F > \sqrt{N} - 1)
```

then $N$ is prime.  
**Proof.** Every prime divisor $\ell$ of $N$ has the form $\ell = 1 + tF$ with $t$ an integer. The case $t = 0$ gives $\ell = 1$, which is not prime. The case $t < 0$ gives $\ell \le 1 - F \le 0$. Therefore $t \ge 1$ and $\ell \ge F + 1 > \sqrt{N}$. No prime $\le \sqrt{N}$ divides $N$, and TEO-1 concludes. $\square$

**TEO-7 [TEO] (Closure by interval and congruence).** Let $B \ge 0$ and $F \ge 1$ be integers. Suppose that: (i) no prime $\ell \le B$ divides $N$ (TEO-5); and (ii) every prime divisor $\ell$ of $N$ satisfies $\ell \equiv 1 \pmod F$. We define

```math
\text{F-08 · Lower bound of the index: } t_{\min} = \max\left( 1, \left\lfloor\frac{B - 1}{F}\right\rfloor + 1 \right)
```

```math
\text{F-09 · Upper bound of the index: } t_{\max} = \left\lfloor \frac{\lfloor\sqrt{N}\rfloor - 1}{F} \right\rfloor
```

If $t_{\min} > t_{\max}$, then $N$ is prime.  
**Proof.** Every $\ell \in D_N$ has the form $\ell = 1 + tF$ with $t \ge 1$ (as in TEO-6). The condition $\ell > B$ is equivalent to $t \ge \lfloor(B - 1)/F\rfloor + 1$. The condition $\ell \le \sqrt{N}$ is equivalent to $\ell \le \lfloor\sqrt{N}\rfloor$, that is, to $t \le t_{\max}$. If $t_{\min} > t_{\max}$, no compatible $t$ exists, and therefore $D_N = \varnothing$. $\square$

**LEM-1 [TEO] (2-adic refinement).** Let $N$ be odd and $F$ be odd. Suppose that every prime divisor $\ell$ of $N$ satisfies $\ell \equiv 1 \pmod F$. Then $\ell \equiv 1 \pmod{2F}$ and

```math
\text{F-10 · 2-adic bound: } \ell \ge 2F + 1
```

Therefore, if $(2F + 1)^2 > N$, then $N$ is prime.  
**Proof.** $\ell$ divides $N$, which is odd, so $\ell$ is odd and $2$ divides $\ell - 1$. Since $F$ is odd, $\gcd(2, F) = 1$, and $F \mid \ell - 1$ together with $2 \mid \ell - 1$ implies $2F \mid \ell - 1$. Therefore $\ell \ge 2F + 1$ and TEO-6 is applied with the larger bound. $\square$

**LEM-2 [TEO] (Refinement for Lucas).** Let $N$ be odd and $Q$ be odd. Suppose that every prime divisor $\ell$ of $N$ satisfies $\ell \equiv \pm 1 \pmod Q$. Then $\ell \ge 2Q - 1$.  
**Proof.** If $\ell \equiv 1 \pmod Q$, we proceed as in LEM-1 and $\ell \ge 2Q + 1$. If $\ell \equiv -1 \pmod Q$, then $Q \mid \ell + 1$ and $2 \mid \ell + 1$, so $2Q \mid \ell + 1$ and $\ell \ge 2Q - 1$. $\square$

---

## 5. Pocklington's criterion and UIS coupling

### 5.1 Congruential restriction by a prime factor

**TEO-8 [TEO] (Congruential restriction by known prime factor).** Let $q$ be a certified prime, $u$ a positive integer, and $N = uq + 1 > 2$. Suppose there exists a base $a$ such that

```math
\text{F-11 · Fermat condition: } a^{N-1} \equiv 1 \pmod N
```

```math
\text{F-12 · Order condition: } \gcd(a^u - 1, N) = 1
```

Then every prime divisor $\ell$ of $N$ satisfies $\ell \equiv 1 \pmod q$.  
**Proof.** Let $\ell$ be a prime divisor of $N$ and $d = \text{ord}_\ell(a)$. Condition F-11 implies $\ell \nmid a$ and $d \mid uq$. Condition F-12 implies $\ell \nmid a^u - 1$, that is, $d \nmid u$. Since $q$ is prime and $d \mid uq$ with $d \nmid u$, we have $q \mid d$. By Lagrange's theorem $d \mid \ell - 1$, hence $q \mid \ell - 1$. $\square$

### 5.2 P–UIS Criterion

**TEO-9 [TEO] (P–UIS: Pocklington with one ancestor).** Let $q$ be a certified prime, $u \ge 1$ an integer, and $N = uq + 1 > 2$. If there exists $a$ satisfying F-11 and F-12, and additionally

```math
\text{F-13 · Classical coverage bound: } q^2 > N
```

then $N$ is prime.  
**Proof.** By TEO-8, every prime divisor $\ell$ of $N$ satisfies $q \mid \ell - 1$, hence $\ell \ge q + 1 > q > \sqrt{N}$. There is no prime divisor $\le \sqrt{N}$, and TEO-1 concludes. $\square$

### 5.3 General form with composite factor

**TEO-10 [TEO] (Pocklington with factor $F$ of certified prime factorization).** Let $F$ be a positive integer with $F \mid N - 1$, with prime factorization $F = \prod r^{e_r}$ where each prime $r$ is certified. Suppose that for each prime $r \mid F$ there exists $a_r$ with

```math
\text{F-14 · Fermat per factor: } a_r^{N-1} \equiv 1 \pmod N
```

```math
\text{F-15 · Order per factor: } \gcd(a_r^{(N-1)/r} - 1, N) = 1
```

Then every prime divisor $\ell$ of $N$ satisfies $F \mid \ell - 1$. If additionally $F^2 > N$ (or F-07 or F-10 with their hypotheses), $N$ is prime.  
**Proof.** Fix $r \mid F$ and let $s = v_r(N - 1) \ge e_r$. Let $d = \text{ord}_\ell(a_r)$. We have $d \mid N - 1$. F-15 gives $d \nmid (N - 1)/r$, and therefore $v_r(d) = s \ge e_r$. Hence $r^{e_r} \mid d \mid \ell - 1$. Since powers of distinct primes are coprime, $F \mid \ell - 1$. The closure follows from TEO-6 or LEM-1. $\square$

### 5.4 Structural closure by ancestral factor

**COR-2 [TEO] (Closure by ancestral factor).** Let $q$ be an ancestral prime such that it has been proven that every prime divisor $\ell$ of $N$ satisfies $\ell \equiv 1 \pmod q$. If $q^2 > N$, then $N$ is prime.  
**Proof.** TEO-6 is applied with $F = q$: $(q + 1)^2 > q^2 > N$. $\square$  
*Consequence.* Primality information is transmitted from a certified ancestor to a descendant provided there exists an algebraic relation proving the restriction on the divisors of the descendant.

### 5.5 T–C1(+) Ladder

**TEO-11 [TEO] (Recursive ladder).** Let $q_0$ be a prime proven by the Clamp. Let a finite sequence

```math
\text{F-16 · Ladder recurrence: } q_i = u_i \cdot q_{i-1} + 1 \quad (i = 1, \ldots, r)
```

For each link, $q_{i-1}^2 > q_i$ and a witness $a_i$ are required with

```math
\text{F-17 · Fermat of the link: } a_i^{q_i - 1} \equiv 1 \pmod{q_i}
```

```math
\text{F-18 · Order of the link: } \gcd(a_i^{u_i} - 1, q_i) = 1
```

Then all $q_i$ are prime.  
**Proof.** Induction on $i$. The base is $q_0$. If $q_{i-1}$ is prime, TEO-9 with $q = q_{i-1}$ and $N = q_i$ proves that $q_i$ is prime. $\square$

**Traceability invariant.** Each node preserves its integer $q_i$, its prime predecessor $F = q_{i-1}$, the multiplier $u_i$, the base $a_i$, the identity $q_i = u_i \cdot F + 1$, the bound $F^2 > q_i$, and the two modular conditions.

### 5.6 Multi-ancestral coupling T–MA1

**TEO-12 [TEO] (T–MA1, multi-ancestral closure).** Let $N > 2$ be odd. Let $q_1, \ldots, q_r$ with $r \ge 2$ be **distinct** odd primes, already certified, with $q_i < N$ and $q_i \mid N - 1$. Suppose that for each $i$ there exists $a_i$ with

```math
\text{F-19 · Fermat of ancestor } i: a_i^{N-1} \equiv 1 \pmod N
```

```math
\text{F-20 · Order of ancestor } i: \gcd(a_i^{(N-1)/q_i} - 1, N) = 1
```

and that, with $F = q_1 \cdot q_2 \cdot \ldots \cdot q_r$, the following holds

```math
\text{F-21 · Multi-ancestral closure: } (F + 1)^2 > N
```

Then $N$ is prime.  
**Proof.** Let $\ell$ be a prime divisor of $N$. For each $i$, TEO-8 applied to $q_i$ and $u = (N - 1)/q_i$ gives $q_i \mid \ell - 1$. The $q_i$ are distinct primes and therefore coprime to each other, so $F \mid \ell - 1$. Since $\ell \ge 2$, it follows that $\ell \ge F + 1$. By F-21, $\ell > \sqrt{N}$. There is no prime divisor $\le \sqrt{N}$, and TEO-1 concludes. $\square$

*Validity conditions.* (a) The $q_i$ are odd primes. If $q = 2$ were admitted, $F$ would be multiplied by 2 without providing information. (b) The $q_i$ are distinct. If a prime were repeated, $F$ would overestimate the congruence. (c) Each $q_i$ must be certified before the node.

**Example 5.1 ($N = 211$, ancestors 5 and 7).** We have $N - 1 = 210 = 2 \cdot 3 \cdot 5 \cdot 7$, $F = 5 \cdot 7 = 35$, and the base $a = 2$ for both ancestors.

| Condition | Value |
|---|---|
| $2^{210} \bmod 211$ | 1 |
| $2^{42} \bmod 211$ ($\Rightarrow \gcd(2^{42} - 1, 211) = 1$) | 107 |
| $2^{30} \bmod 211$ ($\Rightarrow \gcd(2^{30} - 1, 211) = 1$) | 171 |
| $(5 + 1)^2 = 36 < 211$ | ancestor 5 alone does not close |
| $(7 + 1)^2 = 64 < 211$ | ancestor 7 alone does not close |
| $(35 + 1)^2 = 1296 > 211$ | the product closes |

Neither 5 nor 7 closes separately. Combined they give $\ell \equiv 1 \pmod{35}$, so every prime divisor of 211 satisfies $\ell \ge 36$, and $36 > 15 > \sqrt{211}$. Thus 211 is prime.

---

## 6. Lucas sequences

**DEF-4 (Lucas sequence).** For $Q = 1$ and integer $P$:

```math
\text{F-22 · Lucas recurrence: } U_0(P,1) = 0, \quad U_1(P,1) = 1, \quad U_{n+2}(P,1) = P \cdot U_{n+1}(P,1) - U_n(P,1)
```

```math
\text{F-23 · Discriminant: } D = P^2 - 4
```

**Basic facts [CLASSICAL].** Let $\alpha, \beta$ be the roots of $x^2 - Px + 1$, with $\alpha\beta = 1$. If $D \not\equiv 0 \pmod \ell$, then $\alpha \neq \beta$ in an extension of $\mathbb{F}_\ell$ and $U_n = (\alpha^n - \beta^n)/(\alpha - \beta)$. Furthermore, $\ell \mid U_m$ if and only if $\text{ord}(\alpha/\beta)$ divides $m$.

**TEO-13 [TEO] (Lucas character identity).** Let $p$ be an odd prime and $\chi$ the quadratic character modulo $p$, with $\chi(0) = 0$. Then

```math
\text{F-24 · Character sum: } S = \sum_{P \bmod p} \chi(P^2 - 4) = -1
```

**Proof.** Let $T$ be the number of pairs $(P, y)$ modulo $p$ with $y^2 \equiv P^2 - 4$. For each $P$ there are $1 + \chi(P^2 - 4)$ values of $y$, hence $T = p + S$. On the other hand, $P^2 - y^2 \equiv 4$ is equivalent to $(P - y)(P + y) \equiv 4$. Let $a = P - y$ and $b = P + y$. Then $ab \equiv 4$, with $a$ and $b$ nonzero. For each nonzero $a$ there is a unique $b = 4a^{-1}$. Since $p$ is odd, $2$ is invertible and $P = (a + b)/2$, $y = (b - a)/2$. The correspondence is bijective with the $p - 1$ nonzero values of $a$, so $T = p - 1$. From $T = p + S = p - 1$ we obtain $S = -1$. $\square$

**TEO-14 [TEO] (T–L: existence of the Lucas witness).** For every odd prime $N \ge 5$ there exists $P$ such that

```math
\text{F-25 · Lucas witness conditions: } (D/N) = -1, \quad \gcd(N, 2PD) = 1, \quad U_{N+1}(P,1) \equiv 0 \pmod N
```

**Proof.** Let $n_+$, $n_-$, and $n_0$ be the number of $P$ modulo $N$ with $\chi(D)$ equal to $1$, $-1$, and $0$. We have $n_0 = 2$ (the roots $P = \pm 2$). From TEO-13, $n_+ - n_- = -1$, and from $n_+ + n_- + n_0 = N$ it follows that $n_- = (N - 1)/2 \ge 2$. One can choose a nonzero $P$ with $\chi(D) = -1$, and then $D \not\equiv 0$ and $\gcd(N, 2PD) = 1$. Since $D$ is a non-residue, $x^2 - Px + 1$ is irreducible over $\mathbb{F}_N$, and its roots $\alpha, \beta$ are in $\mathbb{F}_{N^2}$, with $\alpha \neq \beta$ and $\alpha\beta = 1$. By Frobenius, $\alpha^N = \beta = \alpha^{-1}$, hence $\alpha^{N+1} = 1$ and also $\beta^{N+1} = 1$. The Lucas formula gives $U_{N+1} = (\alpha^{N+1} - \beta^{N+1})/(\alpha - \beta) = 0$. $\square$

---

## 7. UIS Branches: families T–B1, T–B2, T–B4, and T–B5

### 7.1 Positive branch $N = 2p + 1$ (T–B1)

**TEO-15 [TEO] (T–B1).** Let $p$ be a certified odd prime ($p \ge 3$) and $N = 2p + 1 > 3$. Then

```math
\text{F-26 · T–B1 Criterion: } N \text{ is prime} \iff 3 \nmid N \text{ and } 2^{N-1} \equiv 1 \pmod N
```

**Proof.** $(\Rightarrow)$ Fermat, and $N > 3$ with $N$ prime gives $3 \nmid N$. $(\Leftarrow)$ Let $\ell$ be a prime divisor of $N$. The order of 2 modulo $\ell$ divides $N - 1 = 2p$, hence it is 1, 2, $p$, or $2p$. Order 1 requires $\ell \mid 1$, impossible. Order 2 requires $\ell \mid 3$, excluded by $3 \nmid N$. Thus $p$ divides the order, and therefore $p \mid \ell - 1$. Since $\ell$ is odd and $p$ is odd, $2p \mid \ell - 1$ and $\ell \ge 2p + 1 = N$. Hence $\ell = N$ and $N$ is prime. $\square$

### 7.2 Negative branch $N = 2p - 1$ (T–B2)

**TEO-16 [TEO] (T–B2).** Let $p \ge 3$ be a certified prime and $N = 2p - 1$. Then $N$ is prime if and only if there exists $P$ with

```math
\text{F-27 · T–B2 Criterion: } (D/N) = -1, \quad \gcd(N, 2PD) = 1, \quad U_{N+1}(P,1) \equiv 0 \pmod N
```

**Proof.** $(\Rightarrow)$ It is TEO-14. $(\Leftarrow)$ Let $\ell$ be a prime divisor of $N$. Since $\gcd(N, 2PD) = 1$, $\ell$ is odd and $\ell \nmid P$, $\ell \nmid D$, and then $\alpha \neq \beta$ modulo $\ell$. Let $\omega = \text{ord}(\alpha/\beta) = \text{ord}(\alpha^2)$. From $U_{N+1} \equiv 0$ we have $\omega \mid N + 1 = 2p$. If $\omega = 1$, $\alpha = \beta$, which is impossible. If $\omega = 2$, then $\alpha^4 = 1$ with $\alpha^2 \neq 1$, hence $\alpha^2 = -1$ and $P = \alpha + \alpha^{-1} = 0$, against $\ell \nmid P$. Therefore $\omega \in \{p, 2p\}$ and $p \mid \omega$. If $D$ is a residue modulo $\ell$, $\alpha/\beta \in \mathbb{F}_\ell^*$ and $\omega \mid \ell - 1$. If it is not, by Frobenius $\alpha^{\ell+1} = \alpha\beta = 1$ and $\beta^{\ell+1} = 1$, hence $\omega \mid \ell + 1$. In both cases $\ell \equiv \pm 1 \pmod p$. Since $\ell$ and $p$ are odd, $\ell \equiv \pm 1 \pmod{2p}$ and $\ell \ge 2p - 1 = N$. Then $\ell = N$. $\square$

### 7.3 Generalized positive family (T–B4)

**TEO-17 [TEO] (T–B4).** Let $q \ge 3$ be a certified prime, $k \ge 1$, and $2^k \le 2q$. For $N = 2^k \cdot q + 1$:

```math
\text{F-28 · T–B4 Criterion: } N \text{ is prime} \iff \exists a : a^{N-1} \equiv 1 \pmod N \text{ and } \gcd(a^{2^k} - 1, N) = 1
```

**Proof.** $(\Leftarrow)$ It is TEO-8 with $u = 2^k$, and $q \mid \ell - 1$ for every prime divisor $\ell$. Since $\ell$ is odd, $2q \mid \ell - 1$ and $\ell \ge 2q + 1$. From $2^k \le 2q$, $N \le 2q^2 + 1 < (2q + 1)^2$, so $\sqrt{N} < 2q + 1 \le \ell$ and $N$ is prime (TEO-1). $(\Rightarrow)$ If $N$ is prime, a primitive root $a$ satisfies $a^{N-1} \equiv 1$ and has order $N - 1 = 2^k q > 2^k$, so $a^{2^k} \not\equiv 1$ and $\gcd(a^{2^k} - 1, N) = 1$. $\square$

### 7.4 Generalized negative family (T–B5)

**TEO-18 [TEO] (T–B5).** Let $q \ge 3$ be a certified prime, $k \ge 1$, and $2^k \le 2q$. For $N = 2^k \cdot q - 1$:

```math
\text{F-29 · T–B5 Criterion: } N \text{ is prime} \iff \exists P : (D/N) = -1, \gcd(N, 2PD) = 1,
```
```math
\gcd(U_{2^k}(P,1), N) = 1, U_{N+1}(P,1) \equiv 0 \pmod N
```

**Proof of sufficiency.** Let $\ell$ be a prime divisor of $N$ and $\omega$ the order of $\alpha/\beta$ modulo $\ell$. From $U_{N+1} \equiv 0$, $\omega \mid N + 1 = 2^k q$. From $\gcd(U_{2^k}, N) = 1$, $\ell \nmid U_{2^k}$, that is, $\omega \nmid 2^k$. If $q \nmid \omega$, then $\omega \mid 2^k$, which is impossible. Hence $q \mid \omega$. As in TEO-16, $q \mid \ell - 1$ or $q \mid \ell + 1$, and by LEM-2 $\ell \ge 2q - 1$. Furthermore, $N \le 2q^2 - 1 < (2q - 1)^2 = 4q^2 - 4q + 1$, because $2q^2 - 4q + 2 = 2(q - 1)^2 > 0$. Then $\sqrt{N} < 2q - 1 \le \ell$ and $N$ is prime. $\square$

---

## 8. UIS windows and ancestors

**PROP-3 [TEO] (Ancestors).** If $p = 2q + e$ with $e \in \{-1, +1\}$, and $N = 2p + d$, then

```math
\text{F-30 · Ancestor identity: } N = 4q + 2e + d
```

To obtain $N = 4q + 1$, it must hold that $d = 1 - 2e$. For $N = 4q - 1$, $d = -1 - 2e$.

**PROP-4 [TEO] (Limit of the immediate generator, T–B3).** If $p > |d| + 1$ and $N = 2p + d$, then

```math
\text{F-31 · Greatest common divisors of the generator: } \gcd(p, N - 1) = \gcd(p, d - 1), \quad \gcd(p, N + 1) = \gcd(p, d + 1)
```

For $d \neq 1$ the first greatest common divisor is 1. For $d \neq -1$ the second is 1.  
**Proof.** $N - 1 = 2p + (d - 1)$ and $N + 1 = 2p + (d + 1)$. Since $p$ is prime and $0 < |d \mp 1| < p$ when $d \neq \pm 1$, $p$ does not divide $d \mp 1$. $\square$

---

## 9. Elliptic restrictions and shared memory

**PROP-5 [CLASSICAL + explicit hypotheses] (Restriction by elliptic curve).** Let $E$ be an elliptic curve with good reduction modulo every prime $\ell \mid N$, and let a point whose reduction has certified prime order $r$. By Lagrange and Hasse:

```math
\text{F-32 · Hasse bound: } r \le \#E(\mathbb{F}_\ell) \le (\sqrt{\ell} + 1)^2 \implies \ell \ge (\sqrt{r} - 1)^2
```

This restriction can be intersected with the bounds of the Clamp and the congruences of Pocklington (§2). Validity requires checking the hypotheses of good reduction and order of the point in each relevant reduction.

---

## 10. Certification, traceability, and termination theorems

**TEO-19 [TEO] (Integrated fundamental theorem UIS–TANA).** Let $N > 1$. Suppose there exists a finite sequence of valid restrictions on its prime divisors not greater than $\sqrt{N}$, or a recursive chain of certificates starting from a proven prime root and whose links satisfy deterministic primality criteria. If the memory of restrictions closes to the empty set, or if the last link of the chain matches $N$, then $N$ is prime.  
**Proof.** In the first path, TEO-4 excludes all prime divisors $\le \sqrt{N}$. In the second, TEO-9 and TEO-12 prove each link from the previous ones, and induction concludes the primality of the last one. In both paths the conclusion depends on exact arithmetic relations. $\square$

**TEO-20 [TEO] (Separation between construction and verification).** Let $A$ be an algorithm that produces an integer $N$ and a certificate $C$, and let $V$ be an exact verifier that accepts $C$ only when all the premises of a deterministic primality theorem are satisfied. If $V$ accepts $C$, then $N$ is prime.  
**Proof.** Acceptance means that the conditions of the theorem were checked, and the proof of the theorem shows that those conditions imply the primality of $N$. The procedure by which $A$ found $N$ and $C$ does not intervene in that implication. $\square$  
*Consequence.* The generator can use sequential search, heuristic strategies, parallelism, or candidate selection. The search does not turn the proof into a probabilistic one.

**TEO-21 [TEO] (Sufficiency of recursive evidence).** A chain of certificates with a proven prime root and a finite sequence of valid nodes (Pocklington, Lucas, or multi-ancestral) constitutes a finite proof of the primality of the final target.  
**Proof.** The root provides the induction base. Each valid node proves the primality of its integer from that of its declared ancestors, which appear earlier in the chain. The chain is finite. $\square$

**TEO-22 [TEO] (Termination of verification).** The verification of a finite chain of $r$ nodes terminates after a finite number of exact integer operations.  
**Proof.** Checking the root by divisions up to its square root is finite. Modular exponentiation by successive squaring and the Euclidean algorithm terminate. Integer comparisons and equalities terminate. The sum over a finite chain is finite. $\square$

---

## 11. Evidence format and verifier

### 11.1 Certificate structure

Each JSON certificate contains: the target integer `N`, its length `bits_N`, and an `arbol` (tree) of nodes. The node types are:

| Type | Fields | Theorem applied |
|---|---|---|
| `pinza` | `n` | TEO-5 with $B = \lfloor\sqrt{n}\rfloor$ |
| `hibrido` | `n`, `Y` | Hybrid Clamp–Fermat closure (TANA specification) |
| `pock` | `n`, `F`, `u`, `a`, `regla` | TEO-9 (with bound F-13 or F-10) |
| `lucas` | `n`, `F`, `u`, `P`, `regla` | Lucas closure with $Q = F$: $Q^2 > N$, or $Q$ odd and $(2Q - 1)^2 > N$ by LEM-2 [CLASSICAL: Lehmer–Morrison; the congruence argument is that of TEO-18] |
| `multi_pock` | `n`, `ancestros` = list of {`q`, `a`}, `regla` | TEO-12 (T–MA1) |

The last node must match `N`, and `N.bit_length()` with `bits_N`.

### 11.2 Conditions verified per `pock` node

| ID | Condition |
|---|---|
| T3-1 | $n$ odd and $n > 1$ |
| T3-2 | $F$ is a certified prime (previous dependency in the tree) |
| T3-3 | $n - 1 = u \cdot F$ |
| T3-4 | $F^2 > n$, **or** $F$ odd and $(2F + 1)^2 > n$ |
| T3-5 | $a^{n-1} \equiv 1 \pmod n$ |
| T3-6 | $\gcd(a^u - 1, n) = 1$ |

### 11.3 Conditions verified per `multi_pock` node

| ID | Condition |
|---|---|
| MA-1 | $N$ odd and greater than 2 |
| MA-2 | At least two ancestors |
| MA-ancestor-i | $q_i$ odd prime, distinct from the others, with $2 < q_i < N$, and certified before the node |
| | $q_i$ divides $N - 1$ |
| | $a_i^{N-1} \equiv 1 \pmod N$ |
| | $\gcd(a_i^{(N-1)/q_i} - 1, N) = 1$ |
| MA-3 | $(F + 1)^2 > N$ with $F = \prod q_i$, and all ancestors passed their checks |

### 11.4 Appendix A. Independent verifier (Python 3, exact integer arithmetic)

This verifier reproduces the checks for `pinza`, `pock`, and `multi_pock` nodes. It uses only the classical bound $F^2 > n$ (it is stricter than the engine). It rejects unsupported node types.

```python
import json, sys
from math import gcd, isqrt
from pathlib import Path

def verificar_certificado(ruta):
    datos = json.loads(Path(ruta).read_text(encoding="utf-8"))
    arbol = datos["arbol"]
    assert arbol, "Empty chain"
    certificados = set()
    for i, nodo in enumerate(arbol):
        n = int(nodo["n"])
        assert n > 1
        if nodo["tipo"] == "pinza":
            for divisor in range(2, isqrt(n) + 1):
                assert n % divisor != 0, f"Composite root: {divisor}"
        elif nodo["tipo"] == "pock":
            F, u, a = map(int, (nodo["F"], nodo["u"], nodo["a"]))
            assert F in certificados, "F not previously certified"
            assert n == u * F + 1
            assert F * F > n
            assert pow(a, n - 1, n) == 1
            assert gcd(pow(a, u, n) - 1, n) == 1
        elif nodo["tipo"] == "multi_pock":
            ancestros = [(int(x["q"]), int(x["a"])) for x in nodo["ancestros"]]
            assert n > 2 and n % 2 == 1
            assert len(ancestros) >= 2
            qs = [q for q, _ in ancestros]
            assert len(set(qs)) == len(qs), "repeated ancestors"
            F = 1
            for q, a in ancestros:
                assert 2 < q < n and q in certificados, "ancestor not certified"
                assert (n - 1) % q == 0
                assert pow(a, n - 1, n) == 1
                assert gcd(pow(a, (n - 1) // q, n) - 1, n) == 1
                F *= q
            assert (F + 1) * (F + 1) > n
        else:
            raise ValueError(f"Unsupported node type: {nodo['tipo']}")
        certificados.add(n)
    objetivo = int(datos["N"])
    assert arbol[-1]["n"] == str(objetivo)
    assert objetivo.bit_length() == int(datos["bits_N"])
    return {"primo_certificado": True, "bits": objetivo.bit_length(), "nodos": len(arbol)}

if __name__ == "__main__":
    sys.set_int_max_str_digits(0)
    for archivo in sys.argv[1:]:
        print(archivo, verificar_certificado(archivo))
```

---

## 12. Documentary evidence

| File | Bits (declared = actual) | Nodes | Root | C++ Verifier | Python Verifier (Appendix A) |
|---|---:|---:|---:|---|---|
| `resumed_checkpoint.json` | 8190 | 10 (9 pock links) | 2147483929 | `PRIMO_CERTIFICADO`, `VALIDO` | correct |
| `UIS_certificado_16382_nuevo.json` | 16382 | 11 (10 pock links) | 2147483929 | `PRIMO_CERTIFICADO`, `VALIDO` | correct |

The node sizes in bits are:

- 8190 bits: 32, 62, 122, 242, 482, 962, 1922, 3842, 4096, 8190.
- 16382 bits: 32, 62, 122, 242, 482, 962, 1922, 3842, 7682, 8192, 16382.

---


13. Logic of Certification and Separation of Categories

In the analysis of the UIS–TANA–OMEGA architecture, it is essential not to conflate theorems regarding deterministic construction and certification with probabilistic conjectures concerning the distribution of prime numbers. These are distinct mathematical categories.

The system operates through three logically differentiated processes:

1. **How ​​is a prime found?** By constructing candidates within a given range and applying algebraic and arithmetic constraints (heuristic search).
2. **Why is it prime?** Because the conditions stipulated by the applicable theorems dictate that any prime divisor must satisfy constraints that are incompatible with the composite structure of $N$.
3. **How ​​is it certified?** Through a formal certificate, which verifies the hypotheses, the witnesses, and the ancestral dependencies.

### 13.1 Logical Formalization of Determinism

For the multi-ancestral theorem (TEO-12), the logical conclusion is:

```math
\forall N>2,\quad
\left[\mathrm{Hypothesis}_{T\text{-}MA1}(N)\right]
\Longrightarrow \mathrm{Prime}(N).
```

This implication is **deterministic and universal** with respect to the integers that satisfy its hypotheses. No probability factor appears in the conclusion, nor is any assumption regarding the density of prime numbers required.

The assertion that the search algorithm finds a prime within each specified range follows an additional logical form:

```math
\forall R\in\mathcal{R},\quad
\exists N\in R:
\mathrm{Hypothesis}_{T\text{-}MA1}(N).
```

This second proposition is also deterministic; however, it is established by the system’s construction and coverage theorems, rather than being derived solely from the certification implication. ### 13.2 The Performative Contradiction

If one accepts that all the sufficient hypotheses for a deterministic theorem (such as T–MA1) have been verified, yet still denies that the resulting number is mathematically certified, one incurs a **logical contradiction** with the accepted theorem.

Asking whether a candidate exists that satisfies these hypotheses within a given range is a matter of search, not of the validity of the certification. The distinction is crucial: the primality of the resulting number is a necessary conclusion—not an estimate or a prediction.

### 13.3 Correct Evaluation Chain

The formal analysis of the architecture must follow this chain:

```math
\boxed{
\text{Range}
\;\longrightarrow\;
\text{Construction}
\;\longrightarrow\;
\text{Constraints}
\;\longrightarrow\;
\text{Witnesses}
\;\longrightarrow\;
\text{Certification}
}
```

Each arrow is justified by the corresponding theorem. If this chain is proven for a given range, then the result of the construction and certification is likewise proven for that range. Imposing requirements regarding the infinitude of families or asymptotic superiority in order to judge the correctness of a specific certificate constitutes a category error.

The precise formulation is as follows: **UIS–TANA–OMEGA establishes mathematical rules for construction and certification. When the conditions of its proven theorems are verified, the conclusion of primality is deterministic and mathematically proven.**

## 14. Mathematical Conclusion: Primality as a Network Structure

Based on the evidence formalized in this treatise—the TANA Framework, Multiancestral Coupling (T-MA1), and Graph Optimization (T-MA4)—a structural interpretation is established regarding how primality proofs are constructed and organized.

### 14.1. The Constraint Space and the Collapse of the Set of Divisors

The classical formulation characterizes primality by the absence of non-trivial proper divisors. Within the UIS–TANA framework, this characterization is expressed using set theory.

Let $N > 1$ be an integer, and let $D_N$ be the set of its prime divisors that are no greater than its square root:

$$
D_N=\{\ell:\ell\text{ is prime},\ \ell\mid N,\ 2\leq\ell\leq\lfloor\sqrt{N}\rfloor\}.
$$

Each applicable theorem (e.g., Pocklington’s, Lucas’s) generates a necessary constraint $R_i(N)$ on the potential prime divisors of $N$.

The nodal memory is defined as the intersection of these constraints:

$$
M_k=\bigcap_{i=1}^{k}R_i(N).
$$

According to the Fundamental Theorem (TEO-1):

$$
N\text{ is prime}\iff D_N=\varnothing.
$$

Given that each constraint is valid, the following holds:

$$
D_N\subseteq M_k.
$$

Consequently:

$$
M_k=\varnothing
\Longrightarrow
D_N=\varnothing
\Longrightarrow
N\text{ is prime}.
$$

Therefore, when the space of admissible constraints collapses to the empty set, the primality of $N$ is deductively proven. The complete exclusion of potential prime divisors within the mathematically relevant interval constitutes an exact proof of primality.


### 14.2. Network-Based Primality Proof (Multi-Ancestral Coupling)

The core of this architecture lies in the distribution of the proof burden.

The classical criteria of Pocklington (1914) and their generalizations already allowed for the use of known factors of $N-1$. The structural contribution of UIS–TANA–OMEGA consists of organizing this cooperation through a network of ancestral dependencies and representing it via verifiable graphs.

Under Theorem T-MA1 (TEO-12), several distinct, certified prime ancestors $q_1, \ldots, q_r$ can jointly contribute to the proof of the primality of an integer $N$.

Their coupling yields the factor:

$$
F=\prod_{i=1}^{r}q_i.
$$

For each ancestor, the following requirements must be met:

$$
q_i\mid N-1,
$$

$$
a_i^{N-1}\equiv1\pmod N,
$$

$$
\gcd\left(a_i^{(N-1)/q_i}-1,N\right)=1.
$$

These conditions, combined with the previously certified primality of the ancestors, imply that any prime divisor $\ell$ of $N$ must satisfy:

$$
q_i\mid\ell-1
\qquad\text{for all }i.
$$

Since the ancestors are distinct primes:

$$
F\mid\ell-1.
$$

Therefore:

$$
\ell\geq F+1.
$$

If, in addition, the closure inequality is satisfied:

$$
(F+1)^2>N,
$$

then:

$$
\ell>\sqrt N.
$$

No prime divisor of $N$ can exist within the search interval defined in TEO-1. Consequently:

$$
\boxed{N\text{ is prime}.}
$$

No single ancestor needs to provide full coverage. The combined contribution of several verified ancestors may be sufficient to narrow down the range of possible divisors. The certainty of this conclusion is deterministic and depends exclusively on the precise verification of the theorem's conditions.

### 14.3. The Proof Graph as an Optimizable Object

Structuring proofs allows a primality proof to be represented as a Directed Acyclic Graph (DAG):

$$
G=(V,E),
$$

where the vertices represent certified propositions and the edges represent the mathematical dependencies between them.

This representation enables the application of combinatorial optimization techniques without altering the validity conditions of the theorems.

Let $S$ be a finite set of certificates, and let $\mathrm{Anc}(s)$ be the set of ancestral dependencies required to verify certificate $s$.

We define the shared verification cost as:

$$
C(S)=
\sum_{v\in\bigcup_{s\in S}\mathrm{Anc}(s)}
w(v),
\qquad w(v)\geq0.
$$

Here, $w(v)$ represents the cost assigned to verifying an ancestral dependency $v$, counted only once even when it is shared by multiple certificates. This weighted coverage function is submodular.

Let $A\subseteq B$ be two sets of certificates, and let $x$ be an additional certificate. Then:

$$
C(A\cup\{x\})-C(A)
\geq
C(B\cup\{x\})-C(B).
$$

This inequality expresses that the marginal cost of incorporating a certificate does not increase when a larger set of verified dependencies is already available.

To demonstrate this, we define:

$$
U_A=\bigcup_{s\in A}\mathrm{Anc}(s),
\qquad
U_B=\bigcup_{s\in B}\mathrm{Anc}(s).
$$

Since $A\subseteq B$, it follows that:

$$
U_A\subseteq U_B.
$$

Therefore:

$$
\mathrm{Anc}(x)\setminus U_B
\subseteq
\mathrm{Anc}(x)\setminus U_A.
$$ $$

Given that all weights are non-negative, we obtain:

$$
\sum_{v\in\mathrm{Anc}(x)\setminus U_A}w(v)
\geq
\sum_{v\in\mathrm{Anc}(x)\setminus U_B}w(v).
$$

This is precisely the submodularity inequality. This property formalizes the benefit of reusing certified ancestors and allows for the optimization of the work associated with shared dependencies. The pruning of dominated states (T-MA3) must, in all cases, preserve the sufficient conditions for certification. Thus, this optimization affects the organization and cost of the proof, but not its mathematical validity.

### 14.4. The Separation Between Search and Certification

The UIS–TANA–OMEGA architecture establishes a strict logical separation—formalized in Theorem TEO-20—between the generation of candidates and the proof of their primality.

The evaluation chain is as follows:

$$
\boxed{
\text{Candidate}
\longrightarrow
\text{Witnesses and dependencies}
\longrightarrow
\text{Exact verification}
\longrightarrow
\text{Certified primality}
}
$$

The search process may employ heuristics, parallelism, sequential procedures, or specific strategies for selecting candidates. However, the certainty of the conclusion does not depend on the procedure used to find the integer $N$, but rather on the exact arithmetic validity of the relationships and witnesses that constitute its certificate.

Certification is deterministic, as the acceptance of a certificate implies that the premises of a proven primality theorem have been satisfied. Consequently, the search and the certification are mathematically distinct operations: the former produces candidates and evidence, while the latter deductively establishes primality once sufficient conditions are met.

### Final Formulation

Primality is an intrinsic property of an integer. What UIS–TANA–OMEGA constructs is not the property itself, but rather its proof.

A primality proof can be organized as a finite, verifiable, and optimizable network of algebraic constraints, certified ancestors, and mathematical witnesses.

The UIS–TANA–OMEGA framework enables the structuring of this network through procedures for construction, linkage, and exact verification. Candidates are generated, constraints are combined, ancestral dependencies are verified, and primality is demonstrated via sufficient arithmetic conditions.

The architecture preserves the classical definition of a prime number and maintains a rigorous distinction between the search for candidates and the deductive certainty provided by their certification.

When a valid, deterministic certificate exists, primality is not merely estimated—it is proven.

*END OF THE TREATISE.*
