def xtime(a):
    a = str(a)
    a = int(a,16)
    if (a & 0x80):
        return "{:02x}".format((((a << 1) ^ 0x1B) & 0xFF))
    else:
        return "{:02x}".format((a << 1))
 
print(xtime(57))
print(xtime(92))