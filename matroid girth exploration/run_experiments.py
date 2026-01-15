import numpy as np
import pandas as pd
from matrices import hamming_parity_check, small_ternary_example, random_matrix
from search_dependencies import find_dependencies
from gf_rank_null import rank_mod_p
from bounds import compare_bounds

def run_on_matrix(M, p, label, max_weight):
    r, n = M.shape
    rnk = rank_mod_p(M % p, p)
    null_dim = n - rnk

    deps = find_dependencies(M % p, p=p, max_weight=max_weight, random_trials=8000)

    rows = []
    for d in deps:
        rows.append({
            "matrix": label,
            "field": p,
            "rows": r,
            "cols": n,
            "rank": rnk,
            "null_dim": null_dim,
            "weight": d["weight"],
            "support": list(d["support"]),
            "minimal": d["minimal"]
        })

    bounds = compare_bounds(n, p, null_dim)

    return pd.DataFrame(rows), bounds

def main():
    frames = []
    summaries = []

    M1 = hamming_parity_check() % 2
    df1, b1 = run_on_matrix(M1, 2, "Hamming_3x7", 6)
    frames.append(df1)
    summaries.append(("Hamming_3x7", b1))

    M2 = small_ternary_example() % 3
    df2, b2 = run_on_matrix(M2, 3, "Ternary_2x4", 5)
    frames.append(df2)
    summaries.append(("Ternary_2x4", b2))

    M3 = random_matrix(4, 10, 2, seed=42) % 2
    df3, b3 = run_on_matrix(M3, 2, "Random_4x10", 6)
    frames.append(df3)
    summaries.append(("Random_4x10", b3))

    full = pd.concat(frames, ignore_index=True)
    full.to_csv("dependency_experiments.csv", index=False)

    for name, b in summaries:
        print(name, b["singleton"], b["hamming"])

if __name__ == "__main__":
    main()
