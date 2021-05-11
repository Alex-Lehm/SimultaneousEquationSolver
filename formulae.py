def highest_common_factor(a, b):
    """Method to calculate the highest common factor of two values, using the modulus form of Euclid's
        algorithm:
        1. Compare the values. Take the modulus of the two: highest % lowest.
        2. Check if either value is 0.
        3. If not, repeat 1.
        4. If yes, return the non-zero value."""

    if a == b:
        return a

    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a if b == 0 else b


def lowest_common_multiple(a, b):
    """Makes use of highest_common_factor() to calculate the LCM efficiently, as:
        LCM = (a*b) / HCF(a, b). Return this value"""

    return (a * b) / highest_common_factor(a, b)
