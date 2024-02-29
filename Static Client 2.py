from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from sympy.ntheory.residue_ntheory import discrete_log
from Crypto.Util.number import isPrime
from random import choice

# def smooth_num():
#     smooth_p = 1
#     prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
#     while True:
#         smooth_p = smooth_p * choice(prime)
#         if smooth_p > p and isPrime(smooth_p + 1):
#             smooth_p = smooth_p + 1
#             break 
#     return hex(smooth_p)

p = int("0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", 16)
g = int("0x02", 16)
A = int("0x307a582c8073692983fb5c865e16521b42f192e78aeae0dbd0e74198a82760f3aadfc6a66483130ff37520c33b02ccb6d936edf7a1f9e609af03b101299acf6dc08ec47d95e72a00f4d53663fe33a35ea074b4b07fa3acebe6158604012098ea298bd626042be788937bdd5965f9937e4882417e1a1b3e850c8cdff6356974739646010957411640c57ce44d9cfebc400dd76dc4c15c7623ebeb02c18204efbefe9b459194ccee5b6e3df71c8ea087fc34b154be6d26e9e5bcdf159ec70dbc56", 16)
B = int("0xd0d69585c6586c3b1a23e04245826be6db4aed1c9bc70f7110a30165ca878d31434aa357c2bd26d3c398284a17319504e1aeead141234afeb57dfef11417fdec44b21cea83920f300f4e0c3fb573a895371b24652c5e6ea0539b7719f0f966ac7adb9a292cc49f4d8b39560e02fa82aab3c273cc7df512a80e2de6f0e8840c00554f09460eaa2e221173a9ca13182d4e1342b1e54965e16ca5fc23b1aae80aedc7fb80e1aa9be8b0274812676e8e570e1abf65eea0c49f18794a5afba975c7c7", 16)
iv = "8d0e5b2fc489d1607bf4c8e624a54b79"
encrypted = "64058d11263837c1af61fc27103a1be5a175ddc535559e208b00a1ee0c2cea0b9f8ea13decc9ca0dbaeb5fab37c62a06"

# p1 = int(smooth_num(), 16)
# print(hex(p1))
p1 = int("0x3fd467f209528a0662b47b9770b196aedac7588347994cde7d82b1c1aac9b0b433241226ba8cd6c236fa98838383841ac501e43d80df5bd009ee6e88ed5c97c69c28e6f5394bcfeb731a4ca564cab1a3af7a0640f9de214a45eec7f4a94864fad90a94ba7d25e876ef7a090ec3fa6f027ee7b39d4eb7d48066431c54c9000a0a9d50dcbf291ac8fd1d883b940995be3f8b6dc70eb056c950c135121e634d4f7d0b7cfbed6222ff7f103832307fbb270a9feefc5ec964fa26aa15df00f9e8f5e55dc3f5923a68e98b99dc11019c0c783f3a5820ed893ac13d71b951b31516925eafb2f74cdaf567f8c59243c3d3df1b1811c5b978a41b63a19986c46acd0ba1f59d985d53a633c6e58efcce0f49cec1ac07c125fc50f10d00000000001", 16)
B1 = int("0x3ef780908fb33b1d2385d65c9d9a1acea641ae4d18fba29d177d9e6fbceb0abddcba88fa77dd9ad0259d317f6c72f1bcc655bfb20221408ad5653df2966ec7eaacf0d9857e2585f49f060cf0b824ddb16beaf83f2380f2d7533bc08a647af8759414bf9a98606f91164066554ef7d6240208c506abf551b054f2d70d40c89db2c55d91c6dc55694bcfddca22430e5fb973f9c94d721308f610de598f65a927b794f78afb8ff62d8dd892d365123b33da029443831733b92d75122de26ab408e6882889cd9cea2eb988e9932238b3a311c74a09aa94c92964b83f488fc61ac174be9bf47fb28d5e54b037de5e43bec97d1d7154df6112c9bb57a2c811aee56a69aa0997d0a4aadd7ea5285330f2ad163500905837f52a317b9c18d8624", 16)


b = discrete_log(p1, B1, g)
shared_secret = pow(A, b, p)

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
