# Fungsi untuk mengenkripsi teks menggunakan Vigenere Cipher
def vigenere_encrypt(text, key):
    encrypted_text = []
    key_length = len(key)
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char.lower()) - ord('a')
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

# Fungsi untuk mendekripsi teks menggunakan Vigenere Cipher
def vigenere_decrypt(text, key):
    decrypted_text = []
    key_length = len(key)
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char.lower()) - ord('a')
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

# Fungsi untuk mengenkripsi teks menggunakan Affine Cipher
def affine_encrypt(text, a, b):
    encrypted_text = []
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(((a * (ord(char) - ord('a')) + b) % 26) + ord('a'))
            else:
                encrypted_char = chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A'))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

# Fungsi untuk mendekripsi teks menggunakan Affine Cipher
def affine_decrypt(text, a, b):
    decrypted_text = []
    a_inv = 0
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inv = i
            break
    for char in text:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr((a_inv * (ord(char) - ord('a') - b) % 26) + ord('a'))
            else:
                decrypted_char = chr((a_inv * (ord(char) - ord('A') - b) % 26) + ord('A'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

# Teks yang akan dienkripsi
text = "Success is not final, failure is not fatal, it is the courage to continue that counts"

# Kata kunci untuk Vigenere Cipher
vigenere_key = "ulfi"

# Kunci untuk Affine Cipher (a = 1, b = 2)
a = 1
b = 2

# Enkripsi menggunakan Vigenere Cipher
encrypted_vigenere = vigenere_encrypt(text, vigenere_key)
print("Teks terenkripsi menggunakan Vigenere Cipher:")
print(encrypted_vigenere)

# Dekripsi menggunakan Vigenere Cipher
decrypted_vigenere = vigenere_decrypt(encrypted_vigenere, vigenere_key)
print("Teks terdekripsi menggunakan Vigenere Cipher:")
print(decrypted_vigenere)

# Enkripsi menggunakan Affine Cipher
encrypted_affine = affine_encrypt(text, a, b)
print("\nTeks terenkripsi menggunakan Affine Cipher:")
print(encrypted_affine)

# Dekripsi menggunakan Affine Cipher
decrypted_affine = affine_decrypt(encrypted_affine, a, b)
print("Teks terdekripsi menggunakan Affine Cipher:")
print(decrypted_affine)