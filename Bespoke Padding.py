from Crypto.Util.number import long_to_bytes
from pwn import *
from json import *

r = connect("socket.cryptohack.org", 13386)
r.recv()

send = {"option": "get_flag"}

r.send(dumps(send).encode())
receive = loads(r.recvuntil("}"))
a1 = receive['padding'][0]
b1 = receive['padding'][1]
ct1 = receive['encrypted_flag']

r.send(dumps(send).encode())
receive = loads(r.recvuntil("}"))
a2 = receive['padding'][0]
b2 = receive['padding'][1]
ct2 = receive['encrypted_flag']

e = 11
N = receive['modulus']
print(a1, a2, b1, b2, N, e)
plaintext = 754659823705280937426684693543545157731789888997963325308215810880829655843345426301
print(long_to_bytes(plaintext))