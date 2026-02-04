def pos_neg(a, b, n):
    return (min(a, b) < 0 and max(a, b) > 0) if not n else (a < 0 and b < 0)