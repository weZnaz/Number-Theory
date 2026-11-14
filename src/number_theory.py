from __future__ import annotations

from math import isqrt


def divisors(n: int) -> list[int]:
    """Return all positive divisors of a positive integer n."""
    if n < 0:
        raise ValueError('n must be non-negative.')
    if n == 0:
        return []
    result = []
    for value in range(1, isqrt(n) + 1):
        if n % value == 0:
            result.append(value)
            paired = n // value
            if paired != value:
                result.append(paired)
    return sorted(result)


def is_prime(n: int) -> bool:
    """Return True if n is prime, otherwise False."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    limit = isqrt(n)
    for candidate in range(3, limit + 1, 2):
        if n % candidate == 0:
            return False
    return True


def prime_factorization(n: int) -> list[int]:
    """Return the prime factorization of n."""
    if n < 2:
        return []
    factors: list[int] = []
    divisor = 2
    working = n
    while divisor * divisor <= working:
        while working % divisor == 0:
            factors.append(divisor)
            working //= divisor
        divisor += 1 if divisor == 2 else 2
    if working > 1:
        factors.append(working)
    return factors


def gcd_euclid(a: int, b: int) -> int:
    """Compute gcd(a, b) using the Euclidean algorithm."""
    left = abs(int(a))
    right = abs(int(b))
    while right:
        left, right = right, left % right
    return left


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Return (gcd, x, y) such that ax + by = gcd(a, b)."""
    a = int(a)
    b = int(b)
    if b == 0:
        return abs(a), 1 if a >= 0 else -1, 0
    gcd_value, x1, y1 = extended_gcd(b, a % b)
    return gcd_value, y1, x1 - (a // b) * y1


def lcm(a: int, b: int) -> int:
    """Compute the least common multiple of a and b."""
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd_euclid(a, b) * b)


def modular_add(a: int, b: int, modulus: int) -> int:
    """Return (a + b) mod modulus."""
    if modulus <= 0:
        raise ValueError('modulus must be positive.')
    return (a % modulus + b % modulus) % modulus


def modular_multiply(a: int, b: int, modulus: int) -> int:
    """Return (a * b) mod modulus."""
    if modulus <= 0:
        raise ValueError('modulus must be positive.')
    return (a % modulus * b % modulus) % modulus


def modular_pow(base: int, exponent: int, modulus: int) -> int:
    """Compute base^exponent modulo modulus efficiently."""
    if modulus <= 0:
        raise ValueError('modulus must be positive.')
    result = 1 % modulus
    base %= modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result


def modular_inverse(a: int, modulus: int) -> int:
    """Return the modular inverse of a modulo modulus, if it exists."""
    if modulus <= 0:
        raise ValueError('modulus must be positive.')
    gcd_value, x, _ = extended_gcd(a, modulus)
    if gcd_value != 1:
        raise ValueError(f'{a} does not have an inverse modulo {modulus}.')
    return x % modulus


def solve_linear_congruence(a: int, b: int, modulus: int) -> list[int]:
    """Solve a*x ≡ b (mod modulus)."""
    if modulus <= 0:
        raise ValueError('modulus must be positive.')
    gcd_value, x0, _ = extended_gcd(a, modulus)
    if b % gcd_value != 0:
        return []
    factor = modulus // gcd_value
    base = (x0 * (b // gcd_value)) % factor
    return [(base + k * factor) % modulus for k in range(gcd_value)]


def chinese_remainder_theorem(congruences: list[tuple[int, int]]) -> int:
    """Solve x ≡ a_i (mod n_i) for pairwise-coprime moduli."""
    if not congruences:
        raise ValueError('At least one congruence is required.')
    result = 0
    modulus_product = 1
    for a_i, n_i in congruences:
        if n_i <= 0:
            raise ValueError('All moduli must be positive integers.')
        if gcd_euclid(modulus_product, n_i) != 1:
            raise ValueError('Moduli must be pairwise coprime for this implementation.')
        inverse = modular_inverse(modulus_product % n_i, n_i)
        term = ((a_i - result) % n_i) * inverse % n_i
        result = result + term * modulus_product
        modulus_product *= n_i
    return result % modulus_product


def totient(n: int) -> int:
    """Count the positive integers up to n that are coprime to n."""
    if n <= 0:
        raise ValueError('n must be positive.')
    count = 0
    for value in range(1, n + 1):
        if gcd_euclid(value, n) == 1:
            count += 1
    return count


def euler_totient(n: int) -> int:
    """Alias for totient."""
    return totient(n)


def fermat_little_theorem(a: int, p: int) -> bool:
    """Check whether Fermat's little theorem holds for prime p."""
    if not is_prime(p):
        raise ValueError('p must be prime.')
    return modular_pow(a, p - 1, p) == 1


def euler_theorem(a: int, n: int) -> bool:
    """Check Euler's theorem for gcd(a, n) = 1."""
    if n <= 0:
        raise ValueError('n must be positive.')
    if gcd_euclid(a, n) != 1:
        return False
    return modular_pow(a, totient(n), n) == 1
