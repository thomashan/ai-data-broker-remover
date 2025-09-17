def is_prime(n: int) -> bool:
    """Check if a number is prime.
    
    Args:
        n: Integer to check
        
    Returns:
        True if prime, False otherwise

    Examples:
        >>> is_prime(17)
        True
        >>> is_prime(25)
        False
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True
