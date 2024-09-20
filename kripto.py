import streamlit as st
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

def hill_encrypt(text, key):
    text = text.upper().replace(" ", "")

    if len(text) % 2 != 0:
        st.error('Tolong masukkan kata yang jumlah hurufnya ganjil')

    text_vector = [ord(char) - ord('A') for char in text]

    result_text = ""
    for i in range(0, len(text_vector), 2):
        x1, x2 = text_vector[i], text_vector[i + 1]

        y1 = (x1 * key[0] + x2 * key[1]) % 26
        y2 = (x1 * key[2] + x2 * key[3]) % 26

        result_text += chr(y1 + ord('A')) + chr(y2 + ord('A'))

    return result_text


def hill_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper().replace(" ", "")

    ciphertext_vector = [ord(char) - ord('A') for char in ciphertext]

    det = (key[0] * key[3] - key[1] * key[2]) % 26
    inv_det = pow(det, -1, 26)

    adj_matrix = [key[3], -key[1], -key[2], key[0]]
    adj_matrix = [num % 26 for num in adj_matrix]

    inv_key = [(inv_det * num) % 26 for num in adj_matrix]

    result_text = ""
    for i in range(0, len(ciphertext_vector), 2):
        y1, y2 = ciphertext_vector[i], ciphertext_vector[i + 1]

        x1 = (y1 * inv_key[0] + y2 * inv_key[1]) % 26
        x2 = (y1 * inv_key[2] + y2 * inv_key[3]) % 26

        result_text += chr(x1 + ord('A')) + chr(x2 + ord('A'))

    return result_text


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
    key = st.text_input('Enter 4 numbers for key matrix (space-separated)', value='5 17 8 3')

    try:
        key_matrix = list(map(int, key.split()))
        if len(key_matrix) == 4:
            if st.button('Encrypt'):
                st.session_state['encrypted_text'] = hill_encrypt(input_text, key_matrix)
                st.write('Encrypted Text:', st.session_state['encrypted_text'])
            if st.button('Decrypt'):
                if st.session_state['encrypted_text']:  # Check if encrypted text is available
                    decrypted_text = hill_decrypt(st.session_state['encrypted_text'], key_matrix)
                    st.write('Decrypted Text:', decrypted_text)
                else:
                    st.write('Teks belum dienkripsi')
        else:
            st.error('Key must contain 4 numbers for 2x2 matrix')
    except ValueError:
        st.error('Invalid key. Please enter integers.')
