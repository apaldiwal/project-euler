def sum_of_squares(N):
    """Return the sum of squares of natural numbers."""
    return (N * (N + 1) * (2 * N + 1)) // 6

def square_of_sum(N):
    """Return the square of sum of natural numbers."""
    return (N * (N + 1) // 2) ** 2

def compute_difference(N):
    """Return the difference between square of sum and sum of squares."""
    return square_of_sum(N) - sum_of_squares(N)

if __name__ == "__main__":
    N = 100
    print(compute_difference(N))
