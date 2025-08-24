from broker.math_utils import is_prime

def test_is_prime():
    """Test prime number detection"""
    # Test known primes
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(17) is True
    assert is_prime(9973) is True  # Largest 4-digit prime
    
    # Test known composites
    assert is_prime(25) is False
    assert is_prime(9999) is False
    
    # Test edge cases
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-7) is False
