# RSA Algorithm Demonstration (From Scratch) - Python

## Overview

Project ini merupakan implementasi sederhana dari **algoritma RSA (Rivest, Shamir, Adleman)** menggunakan Python yang dibuat **dari awal (from scratch)** tanpa menggunakan library kriptografi seperti `rsa` atau `cryptography`.

Tujuan utama dari proyek ini adalah untuk **mendemonstrasikan cara kerja RSA secara edukatif**, termasuk proses:

- Pembangkitan kunci (Key Generation)
- Enkripsi pesan (Encryption)
- Dekripsi pesan (Decryption)

Program ini cocok digunakan untuk **pembelajaran kriptografi dasar**, **tugas kuliah**, atau **demonstrasi algoritma keamanan informasi**.

---

# Sejarah Singkat RSA

RSA dikembangkan pada tahun **1977** oleh:

- Ronald Rivest
- Adi Shamir
- Leonard Adleman

di **MIT (Massachusetts Institute of Technology)**.

RSA merupakan algoritma **kriptografi kunci publik (public-key cryptography)** yang memungkinkan komunikasi aman tanpa harus berbagi kunci rahasia sebelumnya.

RSA banyak digunakan pada teknologi keamanan modern seperti:

- HTTPS / SSL
- Digital Signature
- Email Encryption
- Secure Key Exchange

---

# Cara Kerja Algoritma RSA

Algoritma RSA terdiri dari tiga proses utama:

1. **Key Generation**
2. **Encryption**
3. **Decryption**

---

# 1. Key Generation (Pembangkitan Kunci)

Langkah pertama adalah membuat pasangan **public key** dan **private key**.

### Langkah-langkah:

1. Pilih dua bilangan prima besar
p = 61
q = 53

2. Hitung nilai `n`
n = p × q
n = 61 × 53 = 3233

3. Hitung fungsi Euler
φ(n) = (p-1)(q-1)
φ(n) = (60)(52) = 3120

4. Pilih bilangan `e` sehingga
gcd(e, φ(n)) = 1

contoh:
e = 17

5. Hitung `d`
d = e⁻¹ mod φ(n)
d = 2753

### Hasil

Public Key
(e, n) = (17, 3233)

Private Key
(d, n) = (2753, 3233)

---

# 2. Encryption (Enkripsi)

Plaintext diubah menjadi ciphertext menggunakan **public key**.

### Rumus
C = M^e mod n

Dimana:

- `M` = plaintext (dalam bentuk angka ASCII)
- `e` = public exponent
- `n` = modulus
- `C` = ciphertext

### Contoh

Plaintext:
 KRIPTO
 
Ciphertext:
[2576, 589, 866, 2642, 1929, 2605]


---

# Kelebihan RSA

- Menggunakan **public-key cryptography**
- Tidak perlu berbagi kunci rahasia sebelumnya
- Digunakan secara luas dalam sistem keamanan internet
- Mendukung **digital signature**

---

# Kelemahan RSA

- Proses komputasi relatif lambat
- Membutuhkan bilangan prima sangat besar
- Rentan jika ukuran kunci terlalu kecil
- Tidak efisien untuk mengenkripsi data berukuran besar

Biasanya RSA hanya digunakan untuk **pertukaran kunci**, kemudian data dienkripsi menggunakan algoritma simetris seperti **AES**.

---

# Tujuan Proyek

Project ini dibuat untuk:

- Demonstrasi algoritma RSA
- Pembelajaran kriptografi dasar
- Tugas kuliah keamanan informasi / kriptografi
- Memahami implementasi matematika RSA tanpa library eksternal

---

# Lisensi

Project ini dibuat untuk tujuan **edukasi dan pembelajaran**.
Bebas digunakan dan dimodifikasi.

