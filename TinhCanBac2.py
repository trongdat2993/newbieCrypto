from math import log
from Crypto.Util.number import inverse
def Check_Legendre(a, p):
    return pow(a, (p-1)//2, p)

def phanTich(p):
    t = p - 1
    s = 0
    while (t%2 == 0):
        t = t//2
        s = s + 1
    return t, s

def tonelli_Shanks(a, p):
    if Check_Legendre(a, p) == -1%p:
        return 'a không có căn bậc hai theo mod p'
    
    b = 1
    while Check_Legendre(b, p) != -1%p:
        b = b + 1
    
    t = phanTich(p)[0]
    s = phanTich(p)[1]
    
    inv = inverse(a, p)
    c = pow(b, t, p)
    r = pow(a, (t + 1)//2, p)
    for i in range(1, s):
        luyThua = pow(2, s - i - 1)
        heSo = pow(r, 2) * inv
        d = pow(heSo, luyThua, p)
        if d == -1%p:
            r = (r*c)%p
        c = pow(c, 2, p)
    return r, -r%p

print(pow(588, -1, 379))