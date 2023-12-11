from math import sqrt
v1 = [846835985, 9834798552]
v2 = [87502093, 123094980]

def nhanVoHuong(v, u):
    return sum(x * y for x, y in zip(v, u))

def proj(u, nvh):
    return [i * nvh for i in u]

def tru2MaTran(v, proj1):
    ls = []
    for i in range(0, len(v)):
        ls.append(v[i] - proj1[i])
    return ls

def Gauss_Lattice(v1, v2):
    while (True):
        tmp1 = nhanVoHuong(v1, v1)
        tmp2 = nhanVoHuong(v2, v2)
        if(tmp2 < tmp1):
            tmp = []
            tmp = v1
            v1 = v2
            v2 = tmp
        m = nhanVoHuong(v1, v2)//nhanVoHuong(v1, v1)
        if(m == 0):
            return v1, v2
        v2 = tru2MaTran(v2, proj(v1, m))

    

u1 = Gauss_Lattice(v1, v2)[0]
u2 =  Gauss_Lattice(v1, v2)[1]
print(nhanVoHuong(u1, u2))