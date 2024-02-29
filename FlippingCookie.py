import requests
import json
from pwn import xor


URL_GETCOOKIE = 'https://aes.cryptohack.org/flipping_cookie/get_cookie/'

def get_check_admin(cookie, iv):
    URL_CHECKAD = 'https://aes.cryptohack.org/flipping_cookie/check_admin/'+cookie+'/'+iv
    r = requests.get(URL_CHECKAD)
    try:
        flag = (json.loads(r.text))['flag']
    except:
        flag = (json.loads(r.text))['error']
    return flag

def getCookie():
    r = requests.get(URL_GETCOOKIE)
    json_ans = json.loads(r.text)
    return json_ans['cookie']

true = "admin=True;expir".encode()
false = 'admin=False;expi'.encode()
ciphertext = getCookie()
iv_hex = ciphertext[:32]
ct = ciphertext[32:]
iv_hex1 = xor(xor(true, false),bytes.fromhex(iv_hex))
print(get_check_admin(ct, iv_hex1.hex()))

