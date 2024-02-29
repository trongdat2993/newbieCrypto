from Crypto.Cipher import AES
from string import printable
                
ct1 = b'\xe5\xf2\xa3\xc6\xdes\x9b\x91\xf5;\x0bI\x93\x08\xa1\xc0\x97]\xcc\x1a\x89\xc1\xc0h\xcc\xb0%~t\xf9\x8e\xbd'
ct2 = b'\x0bc="\xdc\xec\x90\x94d\xd4qd\xc7\xbd\x99\x0e\x97\xa3\x95\xa77\xdf\xa8"\x84g\xcf\xb3rY\xb3u'
key2 = b''
key1 = b''

for i in printable:
    for j in printable:
        for k in printable:
            key = b'daylakeymothi'
            key = key + (i + j + k).encode()
            cipher2 = AES.new(key, mode=AES.MODE_ECB)
            pt1 = cipher2.decrypt(ct2)
            if pt1 == ct1:
                key2 = key
                break
print(key2)
for i in printable:
    for j in printable:
        for k in printable:
            key = b'daylakeymothi'
            key = key + (i + j + k).encode()
            cipher1 = AES.new(key, mode=AES.MODE_ECB)
            pt = cipher1.decrypt(ct1)
            if b'KCSC' in cipher1.decrypt(ct1):
                print(pt, key)
                break

