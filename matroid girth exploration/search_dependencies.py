import numpy as np
from gf_rank_null import nullspace_mod_p, enumerate_nullspace_vectors, rank_mod_p

def support(v, p):
    return tuple(i for i, x in enumerate(v) if int(x) % p != 0)

def is_minimal(M, v, p):
    S = support(v, p)
    if not S:
        return False
    for i in S:
        T = [j for j in S if j != i]
        if not T:
            continue
        sub = M[:, T] % p
        if rank_mod_p(sub, p) < len(T):
            return False
    return True

def weight(v, p):
    return int(np.count_nonzero(v % p))

def normalize(v, p):
    for x in v:
        if x % p != 0:
            inv = pow(int(x), -1, p)
            return (v * inv) % p
    return v

def generate_random_combos(basis, p, n, trials):
    k = len(basis)
    for _ in range(trials):
        c = np.random.randint(0, p, size=k)
        if not np.any(c):
            continue
        v = np.zeros(n, dtype=int)
        for a, b in zip(c, basis):
            if a % p:
                v = (v + a * b) % p
        yield v

def find_dependencies(M, p=2, max_weight=7, random_trials=6000):
    basis, free = nullspace_mod_p(M, p)
    n = M.shape[1]

    pool = []

    if free and p ** len(free) <= 400000:
        for v in enumerate_nullspace_vectors(basis, p):
            if np.any(v % p):
                pool.append(v % p)

    for v in generate_random_combos(basis, p, n, random_trials):
        pool.append(v % p)

    best = {}
    for v in pool:
        w = weight(v, p)
        if w == 0 or w > max_weight:
            continue

        v = normalize(v, p)
        S = support(v, p)
        if not S:
            continue

        m = is_minimal(M, v, p)

        key = (S, tuple(v.tolist()))
        if key in best:
            continue

        best[key] = {
            "support": S,
            "vector": v,
            "weight": w,
            "minimal": m
        }

    out = list(best.values())
    out.sort(key=lambda x: (x["weight"], not x["minimal"], x["support"]))
    return out

if __name__ == "__main__":
    from matrices import hamming_parity_check

    M = hamming_parity_check()
    deps = find_dependencies(M, p=2, max_weight=6, random_trials=10000)

    for d in deps[:20]:
        print(d["weight"], d["support"], d["minimal"])
