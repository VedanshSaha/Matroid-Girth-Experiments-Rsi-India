# Experimental Girth of Representable Matroids (GF(2), GF(3))

This repository contains small-scale computational experiments on the **girth** of matroids that arise from matrices over finite fields, especially GF(2) and GF(3).  

For a matroid represented by a matrix, the girth is the size of the smallest dependent set of columns, which corresponds to the smallest nonzero vector in the nullspace (a smallest-weight codeword in coding theory language).

The goal of this project is not to solve any open problem, but to **experimentally explore how girth behaves** for concrete families of representable matroids coming from linear codes and simple finite-geometry constructions.

---

## What this code does

The pipeline implements the following steps.

### 1. Construct representable matroids
We build matroids as matrices over GF(2) or GF(3) using:
- Parity-check matrices of small linear codes (e.g. Hamming-type examples)
- Small matrices coming from finite-geometry or hand-built constructions
- Random small matrices for comparison

These matrices define linear matroids whose circuits correspond to minimal linear dependencies among columns.

---

### 2. Compute nullspaces over GF(p)
We implement Gaussian elimination modulo a prime field (p = 2 or 3) to:
- Compute the rank of each matrix
- Find a basis for its nullspace

Every vector in the nullspace gives a linear dependency among columns.

---

### 3. Search for small circuits
To find small dependent sets (small circuits), the code:
- Samples random linear combinations of nullspace basis vectors
- Records the **support** (nonzero positions) of each dependency
- Tracks the smallest supports found

For GF(2), some small nullspaces are also exhaustively enumerated.  
For GF(3), random sampling is used because the space grows quickly.

---

### 4. Test minimality
For each dependency found, the code checks if it is minimal:
- Remove each column in the support
- Recompute rank to see if the remaining columns are still dependent
- If removing any column makes the set independent, the support is a circuit

This filters out non-minimal dependencies.

---

### 5. Estimate girth
For each matrix, the smallest support size among all minimal dependencies is recorded as an experimental estimate of girth.

The code stores:
- Rank and nullity
- Smallest circuit size found
- Field size and matrix parameters

---

### 6. Compare with coding theory bounds
When a matrix is interpreted as a parity-check matrix of a linear code, we compute:
- Singleton bound
- Hamming bound

These are used only for rough comparison with the experimentally observed smallest circuit sizes.

---

## What this project is meant to show

These scripts are meant to:
- Explore how girth behaves in small representable matroids
- Compare different constructions (codes, geometries, random matrices)
- See which families tend to produce short circuits and which do not

The experiments are intentionally small-scale because:
- The nullspace grows exponentially
- Minimality testing is expensive
- Full enumeration is only possible for very small parameters

This is a **tool for building intuition**, not for proving theorems.

---

## Limitations

- Exhaustive enumeration is only feasible for very small matrices.
- For GF(3) most searches are randomized.
- Results depend on random sampling unless explicitly enumerated.
- Performance is not optimized for large matrices.

---

## References and background

The mathematical background comes from:
- Matroid theory (circuits and girth):  
  J. Oxley, *Matroid Theory*
- Coding theory and bounds:  
  F. J. MacWilliams and N. J. A. Sloane, *The Theory of Error-Correcting Codes*
- Basic bounds used here:
  - Singleton bound  
  - Hamming bound  

These references explain why nullspace vectors correspond to circuits and why coding-theoretic bounds give information about possible girth.

---

## Why this is here

This repository reflects a hands-on attempt to understand representable matroids by:
- Writing code to generate examples
- Searching for small circuits
- Comparing different constructions

It is meant to be a starting point for deeper theoretical or computational work.
