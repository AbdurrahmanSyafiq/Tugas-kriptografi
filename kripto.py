import streamlit as st
import numpy as np
import string

def vigenere_encrypt(text, key):
    key = key.upper()
    result = []
    for i, char in enumerate(text.upper()):
        if char in string.ascii_uppercase:
            shift = ord(key[i % len(key)]) - ord('A')
            result.append(chr((ord(char) + shift - ord('A')) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

def vigenere_decrypt(text, key):
    key = key.upper()
    result = []
    for i, char in enumerate(text.upper()):
        if char in string.ascii_uppercase:
            shift = ord(key[i % len(key)]) - ord('A')
            result.append(chr((ord(char) - shift - ord('A')) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

def to_lowercase(text):
    return text.lower().replace(" ", "")

def generate_key_table(key):
    key = key.lower().replace('j', 'i')
    alphabet = ''.join(sorted(set(key + string.ascii_lowercase.replace('j', ''))))
    return [alphabet[i:i + 5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for r, row in enumerate(matrix):
        for c, val in enumerate(row):
            if val == char:
                return r, c
    return None

def format_plaintext(text):
    text = to_lowercase(text)
    formatted = []
    i = 0
    while i < len(text):
        char1 = text[i]
        char2 = text[i + 1] if i + 1 < len(text) else 'x'
        if char1 == char2:
            formatted.append((char1, 'x'))
            i += 1
        else:
            formatted.append((char1, char2))
            i += 2
    return formatted

def playfair_encrypt(matrix, plaintext_pairs):
    ciphertext = []
    for first, second in plaintext_pairs:
        row1, col1 = find_position(matrix, first)
        row2, col2 = find_position(matrix, second)

        if row1 == row2:
            ciphertext.append(matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:
            ciphertext.append(matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2])
        else:
            ciphertext.append(matrix[row1][col2] + matrix[row2][col1])
    return ''.join(ciphertext)

def playfair_decrypt(matrix, ciphertext):
    plaintext_pairs = []
    i = 0
    while i < len(ciphertext):
        char1 = ciphertext[i]
        char2 = ciphertext[i + 1] if i + 1 < len(ciphertext) else ''
        plaintext_pairs.append((char1, char2))
        i += 2

    plaintext = []
    for first, second in plaintext_pairs:
        row1, col1 = find_position(matrix, first)
        row2, col2 = find_position(matrix, second)

        if row1 == row2:
            plaintext.append(matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:
            plaintext.append(matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2])
        else:
            plaintext.append(matrix[row1][col2] + matrix[row2][col1])
    return ''.join(plaintext)


def create_key_matrix(key):
    """
    Membuat matriks kunci 3x3 dari string kunci.
    Kunci harus memiliki panjang minimal 9 karakter yang diubah menjadi angka (0-25).
    """
    key = key.lower()

    # Mengubah karakter kunci menjadi nilai numerik A=0, B=1, ..., Z=25
    key_matrix = [[ord(key[i]) % 97 for i in range(3)],
                  [ord(key[i + 3]) % 97 for i in range(3)],
                  [ord(key[i + 6]) % 97 for i in range(3)]]

    return np.array(key_matrix)

def text_to_vector(text):
    """
    Mengubah teks menjadi vektor numerik.
    Setiap huruf dikonversi menjadi angka berdasarkan posisinya dalam alfabet (A=0, ..., Z=25).
    """
    text = text.lower()
    vector = [ord(char) % 97 for char in text if char.isalpha()]

    # Tambah padding jika panjang teks tidak habis dibagi 3
    while len(vector) % 3 != 0:
        vector.append(0)  # Padding dengan 'A' (0)

    return np.array(vector).reshape(-1, 3)

def vector_to_text(vector):
    """
    Mengubah vektor numerik kembali menjadi teks huruf.
    """
    text = ''.join(chr(int(num) + 97) for num in vector.flatten())
    return text

def find_mod_inverse(matrix):
    """
    Mencari invers matriks (mod 26) menggunakan determinan dan adjoin.
    """
    determinant = int(np.round(np.linalg.det(matrix)))
    determinant_mod_inv = mod_inverse(determinant, 26)

    if determinant_mod_inv is None:
        return None

    matrix_mod_inv = (determinant_mod_inv * np.round(determinant * np.linalg.inv(matrix)).astype(int)) % 26
    return matrix_mod_inv

def mod_inverse(a, m):
    """
    Mencari invers a (mod m) menggunakan Extended Euclidean Algorithm.
    """
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def encrypt_hill(message, key):
    """
    Enkripsi teks menggunakan Hill Cipher.
    """
    if len(key) < 9:
        raise ValueError("Kunci harus memiliki panjang minimal 9 karakter.")

    key_matrix = create_key_matrix(key[:9])
    vector = text_to_vector(message)
    encrypted_vector = np.dot(vector, key_matrix) % 26  # Mod 26 untuk alfabet A-Z
    encrypted_text = vector_to_text(encrypted_vector)
    return encrypted_text.upper()

def decrypt_hill(cipher_text, key):
    """
    Dekripsi teks yang telah dienkripsi menggunakan Hill Cipher.
    """
    key_matrix = create_key_matrix(key[:9])
    vector = text_to_vector(cipher_text)

    # Cari invers kunci matriks (mod 26)
    key_matrix_inv = find_mod_inverse(key_matrix)

    if key_matrix_inv is None:
        raise ValueError("Kunci matriks tidak memiliki invers modulo 26, dekripsi tidak dapat dilakukan.")

    decrypted_vector = np.dot(vector, key_matrix_inv) % 26
    decrypted_text = vector_to_text(decrypted_vector)
    return decrypted_text.upper()


st.title('Cipher Implementation')

cipher_option = st.selectbox('Choose a Cipher', ['Vigenere Cipher', 'Playfair Cipher', 'Hill Cipher'])

if 'encrypted_text' not in st.session_state:
    st.session_state['encrypted_text'] = ''

if cipher_option == 'Vigenere Cipher':
    st.subheader('Vigenere Cipher')

    input_text = st.text_input('Input Text')
    key = st.text_input('Key')

    if st.button('Encrypt'):
        st.session_state['encrypted_text'] = vigenere_encrypt(input_text, key)
        st.write('Encrypted Text:', st.session_state['encrypted_text'])

    if st.button('Decrypt'):
        if st.session_state['encrypted_text']:  # Check if encrypted text is available
            decrypted_text = vigenere_decrypt(st.session_state['encrypted_text'], key)
            st.write('Decrypted Text:', decrypted_text)
        else:
            st.write('Teks belum dienkripsi')

elif cipher_option == 'Playfair Cipher':
    st.subheader('Playfair Cipher')

    input_text = st.text_input('Input Text')
    key = st.text_input('Key')
    key_matrix = generate_key_table(key)
    formatted_plaintext = format_plaintext(input_text)

    if st.button('Encrypt'):
        st.session_state['encrypted_text'] = playfair_encrypt(key_matrix, formatted_plaintext)
        st.write('Encrypted Text:', st.session_state['encrypted_text'])

    if st.button('Decrypt'):
        if st.session_state['encrypted_text']:  # Check if encrypted text is available
            decrypted_text = playfair_decrypt(key_matrix, st.session_state['encrypted_text'])
            st.write('Decrypted Text:', decrypted_text)
        else:
            st.write('Teks belum dienkripsi')

elif cipher_option == 'Hill Cipher':
    st.subheader('Hill Cipher')
    input_text = st.text_input('Input Text')
    key = st.text_input('Key')
    if st.button('Encrypt'):
        st.session_state['encrypted_text'] = encrypt_hill(input_text, key)
        st.write('Encrypted Text:', st.session_state['encrypted_text'])

    if st.button('Decrypt'):
        if st.session_state['encrypted_text']:  # Check if encrypted text is available
            decrypted_text = decrypt_hill(st.session_state['encrypted_text'], key)
            st.write('Decrypted Text:', decrypted_text)
        else:
            st.write('Teks belum dienkripsi')

