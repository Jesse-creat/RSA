import random

# Fungsi untuk menghitung GCD (Greatest Common Divisor)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Extended Euclidean Algorithm
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y

# Modular Inverse
def mod_inverse(e, phi):
    gcd_val, x, y = extended_gcd(e, phi)
    if gcd_val != 1:
        return None
    else:
        return x % phi

# Generate pasangan kunci RSA
def generate_keys():
    # pilih dua bilangan prima sederhana
    p = 61
    q = 53

    n = p * q
    phi = (p - 1) * (q - 1)

    # pilih e yang relatif prima terhadap phi
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # hitung d
    d = mod_inverse(e, phi)

    return (e, n), (d, n)

# Enkripsi
def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher

# Dekripsi
def decrypt(private_key, ciphertext):
    d, n = private_key
    plain = [chr((char ** d) % n) for char in ciphertext]
    return "".join(plain)

# Demo program
if __name__ == "__main__":
    public_key, private_key = generate_keys()

    print("Public Key (e, n):", public_key)
    print("Private Key (d, n):", private_key)

    message = input("Masukkan pesan: ")

    encrypted_msg = encrypt(public_key, message)
    print("Pesan terenkripsi:", encrypted_msg)

    decrypted_msg = decrypt(private_key, encrypted_msg)
    print("Pesan setelah didekripsi:", decrypted_msg)