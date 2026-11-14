import unittest

from src.number_theory import (
    chinese_remainder_theorem,
    divisors,
    euler_theorem,
    euler_totient,
    extended_gcd,
    fermat_little_theorem,
    gcd_euclid,
    is_prime,
    lcm,
    modular_inverse,
    prime_factorization,
    solve_linear_congruence,
)


class NumberTheoryTests(unittest.TestCase):
    def test_divisors(self):
        self.assertEqual(divisors(36), [1, 2, 3, 4, 6, 9, 12, 18, 36])

    def test_prime_detection(self):
        self.assertTrue(is_prime(29))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(30))

    def test_prime_factorization(self):
        self.assertEqual(prime_factorization(60), [2, 2, 3, 5])

    def test_gcd_and_lcm(self):
        self.assertEqual(gcd_euclid(84, 30), 6)
        self.assertEqual(lcm(12, 18), 36)
        self.assertEqual(extended_gcd(30, 12)[0], 6)

    def test_modular_inverse(self):
        self.assertEqual(modular_inverse(7, 26), 15)

    def test_linear_congruence(self):
        self.assertEqual(solve_linear_congruence(3, 2, 11), [8])

    def test_crt(self):
        self.assertEqual(chinese_remainder_theorem([(2, 3), (3, 5), (2, 7)]), 23)

    def test_totient_and_fermat(self):
        self.assertEqual(euler_totient(12), 4)
        self.assertTrue(fermat_little_theorem(3, 5))
        self.assertTrue(euler_theorem(5, 12))


if __name__ == '__main__':
    unittest.main()
