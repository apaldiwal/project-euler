def sum_ap(N, d):
    """Return the sum of an arithmetic sequence."""
    n = N // d
    return (n * (2 * d + (n - 1) * d)) // 2

def sum_multiples():
    """Return the sum of all multiples of 3 or 5."""
    return sum_ap(N,3) + sum_ap(N,5) - sum_ap(N,15)

if __name__ == "__main__":
    N = 999
    print(sum_multiples())
