import numpy as np

def inv_mod(a, p):
    a = a % p
    if a == 0:
        raise ZeroDivisionError("No inverse")
    return pow(int(a), -1, p)

def rref_mod_p(A, p):
    A = A.copy() % p
    rows, cols = A.shape
    r = 0
    pivots = []
    for c in range(cols):
        if r >= rows:
            break
        pivot = None
        for i in range(r, rows):
            if A[i, c] % p != 0:
                pivot = i
                break
        if pivot is None:
            continue
        if pivot != r:
            A[[r, pivot]] = A[[pivot, r]]
        inv = inv_mod(A[r, c], p)
        A[r, :] = (A[r, :] * inv) % p
        for i in range(rows):
            if i == r:
                continue
            if A[i, c] % p != 0:
                factor = A[i, c] % p
                A[i, :] = (A[i, :] - factor * A[r, :]) % p
        pivots.append(c)
        r += 1
    return A % p, pivots

def rank_mod_p(A, p):
    _, pivots = rref_mod_p(A, p)
    return len(pivots)

def nullspace_mod_p(M, p, enumerate_limit=None):
    A = M.copy() % p
    A_rref, pivots = rref_mod_p(A, p)
    rows, cols = A_rref.shape
    pivot_set = set(pivots)
    free_cols = [c for c in range(cols) if c not in pivot_set]
    basis = []
    for j in free_cols:
        vec = np.zeros(cols, dtype=int)
        vec[j] = 1
        for i, pcol in enumerate(pivots):
            prow = None
            for rr in range(rows):
                if A_rref[rr, pcol] % p == 1:
                    prow = rr
                    break
            if prow is None:
                continue
            s = 0
            for fc in free_cols:
                s = (s + int(A_rref[prow, fc]) * int(vec[fc])) % p
            vec[pcol] = (-s) % p
        basis.append(vec % p)
    return basis, free_cols

def enumerate_nullspace_vectors(basis, p, limit=None):
    r = len(basis)
    if r == 0:
        return [np.zeros_like(basis[0], dtype=int)] if basis else []
    total = p ** r
    if limit is None:
        limit = total
    results = []
    from itertools import product
    for coeffs in product(range(p), repeat=r):
        if len(results) >= limit:
            break
        v = np.zeros_like(basis[0], dtype=int)
        for ci, b in zip(coeffs, basis):
            if ci % p != 0:
                v = (v + (ci % p) * b) % p
        results.append(v)
    return results

if __name__ == "__main__":
    M = np.array([[1, 1, 0], [0, 1, 1]], dtype=int)
    b, f = nullspace_mod_p(M, 2)
    print(b, f)
    vecs = enumerate_nullspace_vectors(b, 2)
    print(vecs)
