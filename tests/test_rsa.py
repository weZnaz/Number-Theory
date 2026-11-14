import unittest

from src.cryptography import generate_rsa_keypair, rsa_decrypt, rsa_encrypt


class RSATests(unittest.TestCase):
    def test_rsa_roundtrip(self):
        keys = generate_rsa_keypair(13, 17, 5)
        ciphertext = rsa_encrypt(7, keys.public_key())
        self.assertEqual(rsa_decrypt(ciphertext, keys.private_key()), 7)


if __name__ == '__main__':
    unittest.main()
