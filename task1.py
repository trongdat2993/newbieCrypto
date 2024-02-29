from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hashlib import md5

def encrypt(key):
    key1 = key
    key2 = b'\x00'
    key3 = key1

    key1 = md5(key1).digest()
    key2 = md5(key2).digest()
    key3 = md5(key1).digest()

    cipher1 = AES.new(key1, AES.MODE_ECB)
    cipher2 = AES.new(key2, AES.MODE_ECB)
    cipher3 = AES.new(key3, AES.MODE_ECB)

    enc = cipher1.encrypt(pad(b'}', 16))
    enc = cipher2.decrypt(enc)
    enc = cipher3.encrypt(enc)
    return enc

def decrypt(ciphertext, key):
    key1 = key
    key2 = b'\x00'
    key3 = key1

    key1 = md5(key1).digest()
    key2 = md5(key2).digest()
    key3 = md5(key1).digest()

    cipher1 = AES.new(key3, AES.MODE_ECB)
    cipher2 = AES.new(key2, AES.MODE_ECB)
    cipher3 = AES.new(key1, AES.MODE_ECB)

    enc = cipher1.decrypt(ciphertext)
    enc = cipher2.encrypt(enc)
    enc = cipher3.decrypt(enc)
    return enc.decode('ascii')

ciphertext = bytes.fromhex('df7a81e7d3fd2d54920c92afda088fecc8707ed0b09745e487e6dde04a35ddf280b13390b16ac55fe4cb0a405868be0e27c9bbe735081fa89fd09edbcaad108c4e934166aad172448e887bd40f9f47c7')

# for i in range(0, 256):
#     for j in range(0, 256):
#         for k in range(0, 256):
#             key = bytes([i, j ,k])
#             if encrypt(key) == ciphertext[-16:]:
#                 print(key)

key = b'\xea!\xea'

print(decrypt(ciphertext, key))