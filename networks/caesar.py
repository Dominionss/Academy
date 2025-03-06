def caesar_cipher(text, key):
    """Encrypts or decrypts text using the Caesar Cipher algorithm."""
    result = ""
    for char in text:
        if char.isalpha():  # Only shift alphabetic characters
            shift = 65 if char.isupper() else 97  # ASCII offset for uppercase/lowercase
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result
