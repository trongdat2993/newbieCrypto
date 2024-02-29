from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
p = int("0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", 16)
g = int("0x02", 16)
A = int("0xa1386dba9ce210214939779e63bfe4c17004bfff999a36b340363c6595e6dd2d519385cc8a3c1c9408db769e15daa5a73a62c0bf196935ef9defabb74d266e37a31a7b6e92eee45128a42eb54bfa082f0b2d12cc77bda107a4fa8ec777d63c868e5693ce39ed1116f61b8771934e9602b83c461577d5dd04d7c0706c236a92476881107dbe2e3a0757a1d911bfa0a750fd3287335411146e7a0584c39a325c67136802121c5fd161b43cffeb64567ed3bcb8acf9b54c7ab324d66f8f1d719e27", 16)
B = int("0x8d79b69390f639501d81bdce911ec9defb0e93d421c02958c8c8dd4e245e61ae861ef9d32aa85dfec628d4046c403199297d6e17f0c9555137b5e8555eb941e8dcfd2fe5e68eecffeb66c6b0de91eb8cf2fd0c0f3f47e0c89779276fa7138e138793020c6b8f834be20a16237900c108f23f872a5f693ca3f93c3fd5a853dfd69518eb4bab9ac2a004d3a11fb21307149e8f2e1d8e1d7c85d604aa0bee335eade60f191f74ee165cd4baa067b96385aa89cbc7722e7426522381fc94ebfa8ef0", 16)
shared_secret = int("0x2b22c28042690af9e5c530a93d8cede155e3df791dbaef4a1cdb1a53d98d92affaa331d7e7a567c694ad8c75576ec1a810b27bd678b81b4f4a5c299809131843057098810350793c2241ae6e2996ae938aa45946f859f114f4adf1998e57efbb0f585c13d763e8ded38b19034cd8af253026a04ed3eebd488770f26fbbd0f67ed0edb7a4152f7b8dfbb95376a4bbc30d8f80f509b5f2029d2c681db002c9360160b872109a7bda8fa395cb04bdfee7dd8f0b7e317ea79fde757cd62eb4b6f541", 16)
iv = "0e04b889dfaca930ec74c63185949963"
encrypted = "1a38b85fb3b47973cf2314c22803a4f34ab2688461f9f123afd19ee118aab257"
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

print(decrypt_flag(shared_secret, iv, encrypted))