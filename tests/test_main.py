from main import is_prime


def test_is_prime_true():  # [AI FIX]
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(13) is True


def test_is_prime_false():  # [AI FIX]
    assert is_prime(1) is False
    assert is_prime(4) is False
    assert is_prime(15) is False
    assert is_prime(-7) is False
    assert is_prime(0) is False


def test_hi():  # [AI FIX]
    # This function doesn't do anything yet, but we'll keep it there.
    pass
