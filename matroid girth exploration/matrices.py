import numpy as np

def hamming_parity_check():
    cols = [
        [0, 0, 1],
        [0, 1, 0],
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 1],
    ]
    return np.array(cols, dtype=int).T

def small_ternary_example():
    return np.array(
        [
            [1, 0, 1, 2],
            [0, 1, 1, 1],
        ],
        dtype=int,
    )

def random_matrix(r, n, p, seed=None):
    rng = np.random.default_rng(seed)
    return rng.integers(low=0, high=p, size=(r, n), dtype=int)

def pg22_points():
    return hamming_parity_check()

if __name__ == "__main__":
    print(hamming_parity_check().shape)
    print(small_ternary_example().shape)
    print(random_matrix(4, 10, 5, seed=1).shape)
