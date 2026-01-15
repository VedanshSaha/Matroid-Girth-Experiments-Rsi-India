import math

def singleton(n, k):
    return n - k + 1

def hamming_volume(n, q, t):
    return sum(math.comb(n, i) * (q - 1) ** i for i in range(t + 1))

def admissible_distances(n, q, k):
    out = []
    for d in range(1, n + 1):
        t = (d - 1) // 2
        if hamming_volume(n, q, t) <= q ** (n - k):
            out.append(d)
    return out

def hamming_upper(n, q, k):
    vals = admissible_distances(n, q, k)
    return max(vals) if vals else 0

def bound_profile(n, q, k):
    prof = []
    for d in range(1, n + 1):
        t = (d - 1) // 2
        prof.append((d, hamming_volume(n, q, t), q ** (n - k)))
    return prof

def compare_bounds(n, q, k):
    return {
        "singleton": singleton(n, k),
        "hamming": hamming_upper(n, q, k),
        "profile": bound_profile(n, q, k)
    }

if __name__ == "__main__":
    r = compare_bounds(15, 2, 7)
    print(r["singleton"], r["hamming"])
