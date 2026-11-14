import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

out_dir = Path(__file__).resolve().parent / 'generated_visualizations'
out_dir.mkdir(exist_ok=True)

# Prime distribution plot
primes = []
for value in range(2, 251):
    is_prime = True
    for divisor in range(2, int(np.sqrt(value)) + 1):
        if value % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(value)

plt.figure(figsize=(10, 5))
plt.hist(primes, bins=20, color='steelblue', edgecolor='black')
plt.title('Prime Number Distribution up to 250')
plt.xlabel('Prime value')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig(out_dir / 'prime_distribution.png', dpi=200)
plt.close()

# Modular arithmetic heatmap
modulus = 13
values = np.arange(modulus)
X, Y = np.meshgrid(values, values)
Z = (X * Y) % modulus
fig, ax = plt.subplots(figsize=(7, 6))
img = ax.imshow(Z, cmap='viridis')
ax.set_title('Multiplication Table Modulo 13')
ax.set_xlabel('a')
ax.set_ylabel('b')
for i in range(modulus):
    for j in range(modulus):
        ax.text(j, i, str(Z[i, j]), ha='center', va='center', color='white')
fig.colorbar(img, ax=ax)
plt.tight_layout()
plt.savefig(out_dir / 'modular_arithmetic_heatmap.png', dpi=200)
plt.close()

# RSA workflow diagram
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')
ax.text(1.2, 8.5, 'Choose primes p and q', bbox=dict(boxstyle='round', fc='lightblue', ec='black'))
ax.text(4.8, 8.5, 'Compute n = p*q', bbox=dict(boxstyle='round', fc='lightblue', ec='black'))
ax.text(8.3, 8.5, 'Compute phi(n)', bbox=dict(boxstyle='round', fc='lightblue', ec='black'))
ax.text(1.2, 5.0, 'Choose public exponent e', bbox=dict(boxstyle='round', fc='lightgreen', ec='black'))
ax.text(4.8, 5.0, 'Compute d = e^{-1} mod phi(n)', bbox=dict(boxstyle='round', fc='lightgreen', ec='black'))
ax.text(8.3, 5.0, 'Public key: (e, n)', bbox=dict(boxstyle='round', fc='lightgreen', ec='black'))
ax.text(5.0, 1.8, 'Private key: (d, n)', bbox=dict(boxstyle='round', fc='salmon', ec='black'))
ax.annotate('', xy=(3.3, 8.5), xytext=(2.2, 8.5), arrowprops=dict(arrowstyle='->'))
ax.annotate('', xy=(6.7, 8.5), xytext=(5.7, 8.5), arrowprops=dict(arrowstyle='->'))
ax.annotate('', xy=(2.0, 5.0), xytext=(1.5, 7.6), arrowprops=dict(arrowstyle='->'))
ax.annotate('', xy=(5.8, 5.0), xytext=(5.5, 7.6), arrowprops=dict(arrowstyle='->'))
ax.annotate('', xy=(5.3, 2.2), xytext=(5.3, 4.2), arrowprops=dict(arrowstyle='->'))
plt.tight_layout()
plt.savefig(out_dir / 'rsa_workflow.png', dpi=200)
plt.close()
