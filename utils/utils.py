def is_same_seq(a, b):
    """Check if two sequences are the same (a and b should not be swapped)"""
    return len(a) == len(b) and all(a == b for a, b in zip(a, b))
