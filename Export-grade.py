from sympy.ntheory.residue_ntheory import discrete_log
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
p = int("0xde26ab651b92a129", 16)
g = int("0x2", 16)
A = int("0xdc5b63974ff0cefb", 16)
B = int("0x451b1bee7ea11770", 16)
iv = "30bac67ac581ad7f0fd0f0f7483feee0"
encrypted_flag = "1eed38849abbf30277c48f6fa894771461a1d7a01362e19c132e067530b62633"

a = discrete_log(p, A, g)
shared_secret = pow(B, a, p)

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

print(decrypt_flag(shared_secret, iv, encrypted_flag))

