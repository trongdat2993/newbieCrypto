import requests
import json

def encrypt(plaintext, iv):
    URL = 'https://aes.cryptohack.org/symmetry/encrypt/'+plaintext+'/'+iv
    r = requests.get(URL)
    json_ans = json.loads(r.text)
    ct = json_ans['ciphertext']
    return ct

def get_encrypted():
    URL = 'https://aes.cryptohack.org/symmetry/encrypt_flag'
    r = requests.get(URL)
    json_ans = json.loads(r.text)
    ct = json_ans['ciphertext']
    return ct

ciphertext = get_encrypted()
iv = ciphertext[:32]
encrypted = ciphertext[32:]
plaintext = encrypt(encrypted, iv)
print(bytes.fromhex(plaintext))