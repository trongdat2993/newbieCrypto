import requests
import json
import string
from binascii import hexlify

alphabet = string.ascii_letters + string.digits + "!{_}?"
def encrypt(plaintext):
    URL = 'https://aes.cryptohack.org/ecb_oracle/encrypt/'+plaintext
    r = requests.get(URL)
    json_ans = json.loads(r.text)
    ct = json_ans['ciphertext']
    return ct

flag = 'crypto{'
while True:
    pt_sent = '1' * (31-len(flag))
    response = encrypt(pt_sent.encode().hex())
    for j in alphabet:
        plaintext = pt_sent + flag + j
        response1 = encrypt(plaintext.encode().hex())
        if response1[32:64] == response[32:64]:
            flag = flag + j
            break
    if flag[-1] == '}':
        break


print(flag)
