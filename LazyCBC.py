import requests
import json
from pwn import xor

def encrypt(plaintext):
    URL = 'https://aes.cryptohack.org/lazy_cbc/encrypt/'+plaintext
    r = requests.get(URL)
    json_ans = json.loads(r.text)
    ct = json_ans['ciphertext']
    return ct

def receive(ciphertext):
    URL = 'https://aes.cryptohack.org/lazy_cbc/receive/'+ciphertext
    r = requests.get(URL)
    try:
        json_ans = (json.loads(r.text))
    except:
        json_ans = (json.loads(r.text))["error"]
    return json_ans

def get_flag(flag):
    URL = 'http://aes.cryptohack.org/lazy_cbc/get_flag/'+flag
    r = requests.get(URL)
    json_ans = json.loads(r.text)
    return json_ans['plaintext']

ciphertext = b"\0" * 32
decrypted = receive(ciphertext.hex())['error'][-64:]

c0 = decrypted[:32] 
c1 = decrypted[32:]
xr = xor(bytes.fromhex(c0), bytes.fromhex(c1)).hex()
print(bytes.fromhex(get_flag(xr))) 