from __future__ import annotations

from dataclasses import dataclass

from .number_theory import gcd_euclid, is_prime, modular_inverse, modular_pow


def caesar_encrypt(message: str, shift: int) -> str:
    """Encrypt a string using a Caesar cipher."""
    encrypted_chars = []
    for ch in message:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            offset = (ord(ch) - base + shift) % 26
            encrypted_chars.append(chr(base + offset))
        else:
            encrypted_chars.append(ch)
    return ''.join(encrypted_chars)


def caesar_decrypt(message: str, shift: int) -> str:
    """Decrypt a Caesar cipher text."""
    return caesar_encrypt(message, -shift)


def affine_encrypt(message: str, a: int, b: int) -> str:
    """Encrypt using E(x) = (ax + b) mod 26."""
    if gcd_euclid(a, 26) != 1:
        raise ValueError('a must be coprime with 26.')
    result = []
    for ch in message:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            value = ord(ch) - base
            result.append(chr(base + ((a * value + b) % 26)))
        else:
            result.append(ch)
    return ''.join(result)


def affine_decrypt(message: str, a: int, b: int) -> str:
    """Decrypt using the inverse affine relation."""
    inv_a = modular_inverse(a, 26)
    result = []
    for ch in message:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            value = ord(ch) - base
            result.append(chr(base + ((inv_a * (value - b)) % 26)))
        else:
            result.append(ch)
    return ''.join(result)


@dataclass
class RSAKeyPair:
    p: int
    q: int
    n: int
    e: int
    d: int
    phi_n: int

    def public_key(self) -> tuple[int, int]:
        return (self.e, self.n)

    def private_key(self) -> tuple[int, int]:
        return (self.d, self.n)


def generate_rsa_keypair(p: int, q: int, e: int | None = None) -> RSAKeyPair:
    """Generate a small educational RSA key pair."""
    if p <= 1 or q <= 1:
        raise ValueError('p and q must be greater than 1.')
    if p == q:
        raise ValueError('p and q must be different prime numbers.')
    if not is_prime(p) or not is_prime(q):
        raise ValueError('p and q must be prime numbers.')

    n = p * q
    phi_n = (p - 1) * (q - 1)
    if e is None:
        e = 65537
    if gcd_euclid(e, phi_n) != 1:
        raise ValueError('e must be coprime to phi(n).')
    d = modular_inverse(e, phi_n)
    return RSAKeyPair(p=p, q=q, n=n, e=e, d=d, phi_n=phi_n)


def rsa_encrypt(message: int, public_key: tuple[int, int]) -> int:
    """Encrypt a message using the public key (e, n)."""
    e, n = public_key
    return modular_pow(message, e, n)


def rsa_decrypt(ciphertext: int, private_key: tuple[int, int]) -> int:
    """Decrypt ciphertext using the private key (d, n)."""
    d, n = private_key
    return modular_pow(ciphertext, d, n)


def rsa_demo() -> dict[str, int | tuple[int, int]]:
    """Return a simple RSA example for notebook work."""
    keypair = generate_rsa_keypair(13, 17, 5)
    message = 7
    ciphertext = rsa_encrypt(message, keypair.public_key())
    recovered = rsa_decrypt(ciphertext, keypair.private_key())
    return {
        'message': message,
        'ciphertext': ciphertext,
        'recovered': recovered,
        'public_key': keypair.public_key(),
        'private_key': keypair.private_key(),
    }
