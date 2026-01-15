# Girth of Representable Matroids over GF(2) and GF(3)

This repository contains code to compute and test **girth** for matroids represented by matrices over small finite fields, mainly GF(2) and GF(3).

For a matrix \(M\), the associated matroid has ground set equal to the columns of \(M\).  
A circuit is a minimal linearly dependent set of columns.  
The girth is the size of the smallest circuit.

Equivalently, circuits correspond to nonzero vectors in the nullspace of \(M\) with minimal support.

---

## Matrix families tested

The code builds small representable matroids using:

- Parity-check matrices of small linear codes (e.g. Hamming-type codes)
- Small matrices from finite-geometry constructions
- Random matrices over GF(2) and GF(3)

Each matrix is treated as a representation of a linear matroid.

---

## Nullspace computation

Gaussian elimination modulo a prime field is implemented to compute:

- Rank
- A basis for the nullspace of the matrix

All computations are done over GF(2) or GF(3).

---

## Circuit search

Given a nullspace basis \(v_1,\dots,v_k\), the code searches for small-support nullspace vectors.

Methods used:
- Exhaustive enumeration for small GF(2) nullspaces
- Random linear combinations of basis vectors for larger nullspaces or GF(3)

For each nullspace vector, its support (nonzero coordinates) is recorded.

---

## Minimality testing

To test whether a dependency is a circuit:

For a support set \(S\):
- Remove each column \(i \in S\)
- Recompute rank of the restricted matrix
- If removing any column makes the set independent, then \(S\) is minimal

Only minimal supports are counted as circuits.

---

## Girth estimation

For each matrix, the smallest size of a minimal support found is recorded as the experimental girth.

The code logs:
- Field
- Matrix dimensions
- Rank and nullity
- Smallest circuit found

---

## Coding-theory comparison

When a matrix is used as a parity-check matrix of a linear code, the following bounds are computed:

- Singleton bound
- Hamming bound

These give reference values for the minimum distance and are compared to the smallest circuits found.

---

## Scale

The search is limited to small matrices because:
- Nullspaces grow exponentially
- Minimality checks are expensive

Typical ranges:
- Ranks up to about 5–7
- Block lengths up to about 15–25, depending on field and nullity

Random sampling is used beyond this range.

---

## References

- Oxley, *Matroid Theory*  
- MacWilliams and Sloane, *The Theory of Error-Correcting Codes*
- Standard definitions of circuits, girth, and code distance
