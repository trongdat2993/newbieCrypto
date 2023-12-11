v = [[4,1,3,-1], [2,1,-3,4], [1,0,-2,7], [6, 2, 9, -5]]

def nhanVoHuong(u, v):
    return sum(x * y for x, y in zip(u, v))

def proj(u, nvh):
    return [i * nvh for i in u]

def tru2MaTran(v, proj1):
    ls = []
    for i in range(0, len(v)):
        ls.append(v[i] - proj1[i])
    return ls
       
def Gram_Schmidt(v):
    u = v[0]
    ls = []
    ls.append(u)
    print(ls)
    for i in range(1, len(v)):
        for j in ls:
            tmp = nhanVoHuong(j, v[i]) / nhanVoHuong(j, j)
            proj1 = proj(j, tmp)
            v[i] = tru2MaTran(v[i], proj1)
        ls.append(v[i])
    return ls    

for i in Gram_Schmidt(v):
    print(i)