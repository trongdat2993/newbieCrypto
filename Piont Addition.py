from Crypto.Util.number import inverse
from Crypto.Hash import SHA1

def PointAdd(P, Q, a, b, p):
    x1 = P[0]
    y1 = P[1]

    x2 = Q[0]
    y2 = Q[1]

    lamda = 0

    if x1 == 0 and y1 == 0:
        return Q
    
    if x2 == 0 and y2 == 0:
        return P
    
    if x1 == x2 and y1 == -y2:
        return [0, 0]
    
    if x1 == x2 and y1 == y2:
        lamda = ((3 * pow(x1, 2) + a) * inverse(2*y1, p))%p
    
    if x1 != x2 and y1 != y2:
        lamda =  ((y2 - y1) * inverse(x2 - x1, p))%p

    x3 = (lamda**2 - x1 - x2)%p
    y3 = (lamda*(x1 - x3) - y1)%p

    return [x3, y3]

def DAA(P, n, a, b, p):
    Q = P
    R = [0, 0]
    while n > 0:
        if n%2 == 1:
            R = PointAdd(R, Q, a, b, p)
        Q = PointAdd(Q, Q, a, b, p)
        n = n // 2
    
    return R

a = 497
b = 1768
p = 9739
Qa = [815, 3190]
nB = 1829
s = DAA(Qa, nB, a, b, p)
print(s)

