def Ext_Ecd(a, b):
    x1 = y2 = 0
    x2 = y1 = 1
    while b > 0:
        q = a // b
        r = a - q*b
        x = x2 - q*x1
        y = y2 - q*y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    d = a
    x = x2
    y = y2
    return (d, x, y)

print(Ext_Ecd(32321, 26513))
        
        
    