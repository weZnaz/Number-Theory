# Number Theory and Cryptography

This repository was created as an academic learning project inspired by the workshop materials from the Maths and Physics Club, IIT Bombay. The purpose is to study number theory, understand how it underpins modern cryptography, and implement the important algorithms in Python with clear explanations.

## Reference repository checklist

The reference workshop material covers the following major topics:

- Divisibility and arithmetic structure
- Prime numbers and composite numbers
- Prime factorization
- GCD and Euclidean algorithm
- Extended Euclidean algorithm
- LCM and divisibility relationships
- Modular arithmetic and congruences
- Linear congruences and modular inverses
- Fermat's little theorem and Euler's theorem
- Euler's totient function
- Chinese remainder theorem
- Classical cryptography ideas
- Public-key cryptography
- RSA key generation, encryption, and decryption

This repository does not copy the workshop notebooks line by line. Instead, it reorganizes the core ideas into a cleaner academic structure with original explanations, code, examples, practice notebooks, and test cases.

## Repository structure

```text
Number-Theory/
├── README.md
├── requirements.txt
├── .gitignore
├── reference_summary.md
├── notebooks/
│   ├── 01_Number_Theory_Foundations.ipynb
│   ├── 02_Modular_Arithmetic_and_Congruences.ipynb
│   ├── 03_Primes_Factorization_and_GCD.ipynb
│   ├── 04_Modular_Inverse_and_CRT.ipynb
│   ├── 05_Euler_Fermat_and_Totient.ipynb
│   ├── 06_RSA_Implementation.ipynb
│   └── 07_Cryptography_Practice.ipynb
├── src/
│   ├── __init__.py
│   ├── number_theory.py
│   └── cryptography.py
├── figures/
│   ├── generate_visualizations.py
│   └── generated_visualizations/
│       ├── prime_distribution.png
│       ├── modular_arithmetic_heatmap.png
│       └── rsa_workflow.png
├── examples/
│   └── sample_outputs.md
├── tests/
│   ├── test_number_theory.py
│   └── test_rsa.py
└── .gitignore
```

## Main learning goals

- Understand divisibility and prime factorization
- Implement GCD, LCM, and modular arithmetic manually
- Solve simple congruence and inverse problems
- Learn Euler's theorem and the totient function
- Explain the mathematics behind RSA with small examples
- Connect number theory to classical and public-key cryptography

## Educational RSA note

The RSA implementation in this project is intentionally educational and uses small numbers so the math is easy to follow. It is not a production-grade cryptographic implementation and is included for learning purposes only.

## Quick start

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m unittest discover -s tests
```

## Author

- Name: Syed Nazmul Islam
- Student ID: IT22023
