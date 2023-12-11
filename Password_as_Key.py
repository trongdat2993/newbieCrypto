from Crypto.Cipher import AES
import hashlib
import io

# /usr/share/dict/words from
# https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words
def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = password_hash

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}
    
    return decrypted


with open("D:\Code\Python\key.txt.txt", encoding="utf-8") as f:
    words = [w.strip() for w in f.readlines()]

for i in words:
    key = hashlib.md5(i.encode()).digest()
    flag = decrypt("c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66", key)
    if b'crypto' in flag:
        print(flag)
        break
    