p = int("0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", 16)
g = int("0x02", 16)
A = int("0x43dfa1aca650344d2e0866aae656035e9ca5ed05d9f55c6baa581fd2c58ff9f3e742bf5a536e5672ce45eff0f2ec4bec511941571ba51748197b61dd892ba0777ab06aebfe1c72266346cfdb24dd44d1676d422039e422a9e15fc2dd53d43d7efb38ffb6551ef29d4e363c15706757bbbbd240a2203db132a4527afbb16d44d9fdef73f266b6d00a7208b1b5bb673cd4c2d247bd120d4cb25ae1855494a7938997d73bd8977a96d23754805d35b8ab2ae2f65e0199b6b0fb87fa2137174bbf31", 16)
B = int("0x62d9cb00aae0d828d6e801e16cae7d5c3212bf6c6f733e703b60043e7afa90e68e1c1925b46ca8f5be3cde5953c7b8c76758fae1dbd09114bc4f4ec540169ce4495e790c19daf68937956d8ec0c65b7d3980600e49b7d95bea64409f6ea41c554cf38986a21e18e99b27b85cd41883bf3456d97342453b227699c19c7a90341ec1533de26d749fde2384516f464b4137fd0ffc17b8c1f4bff5b8eca55d2b1a4c3fa62d6abb759a24f4a79d41548820f433bac89e25dc2b412508d4b0d168a212", 16)
print(hex(pow(g, 3, p)))
iv = "b8a143ef7140e6f2469e29159da005e4"
encrypted_flag =  "38be5c5d4e25261064b01c2812f3015ef3ec4d8dc81e435ca6d87cbd811f5d87"
shared_secret = pow(A, 3, p)
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


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