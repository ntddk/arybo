from arybo.lib import MBA
def f(x):
    v0 = x*0xe5 + 0xF7
    v0 = v0&0xFF
    v3 = (((((v0*0x26)+0x55)&0xFE)+(v0*0xED)+0xD6)&0xFF )
    v4 = ((((((- (v3*0x2))+0xFF)&0xFE)+v3)*0x03)+0x4D)
    v5 = (((((v4*0x56)+0x24)&0x46)*0x4B)+(v4*0xE7)+0x76)
    v7 = ((((v5*0x3A)+0xAF)&0xF4)+(v5*0x63)+0x2E)
    v6 = (v7&0x94)
    v8 = ((((v6+v6+(- (v7&0xFF)))*0x67)+0xD))
    res = ((v8*0x2D)+(((v8*0xAE)|0x22)*0xE5)+0xC2)&0xFF
    return (0xed*(res-0xF7))&0xff

mba8 = MBA(8)
X = mba8.var('X')
res = f(X)
VD = res.vectorial_decomp([X])

print(res)
print("====")
print("Cst = " + hex(VD.cst().get_int_be()))
