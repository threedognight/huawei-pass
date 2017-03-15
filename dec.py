#from Crypto.Cipher import AES
import binascii, struct
#n = bytearray(b'p"VBAQ9<R;`t}XRO^MgR!%!!')
#n = bytearray(b'RT0}%[uVW16%Zb~-d5zONyx!')
n = bytearray(b'+_`!X\'4l_$hPsGVEaT*:E"2!')
p = bytearray(b'\xb8\x36\x3c\x9b\x77\xda\xed\x4b\x9a\xbb\x9f\x2f\x6d\xf5\xf1\xd5\xcb\x64\x97\x5d\x5d\x3b\xce\xe8\x82\x7f\x2f\x42\x23\x5f\x92\x29')
for j in range(len(n)):
    print(format(n[j], '02X'), end=' ')
print()
# "D:\Program Files (x86)\Python\Python36-32\python.exe" C:/Users/Loki/PycharmProjects/huawei/dec.py
# 0x70 0x22 0x56 0x42 0x41 0x51 0x39 0x3c 0x52 0x3b 0x60 0x74 0x7d 0x58 0x52 0x4f 0x5e 0x4d 0x67 0x52 0x21 0x25 0x21 0x21
# Process finished with exit code 0
crypted_string = bytearray(n)
for i in range(len(crypted_string)):
    if crypted_string[i] != 0x7e:
        crypted_string[i] -= 0x21
    else:
        crypted_string[i] = 0x1e
for j in range(len(crypted_string)):
    print(format(crypted_string[j], '02X'), end=' ')

a1 = crypted_string[0]+crypted_string[1]*93+crypted_string[2]*93*93+crypted_string[3]*93*93*93+crypted_string[4]*93*93*93*93
a2 = crypted_string[5]+crypted_string[6]*93+crypted_string[7]*93*93+crypted_string[8]*93*93*93+crypted_string[9]*93*93*93*93
a3 = crypted_string[10]+crypted_string[11]*93+crypted_string[12]*93*93+crypted_string[13]*93*93*93+crypted_string[14]*93*93*93*93
a4 = crypted_string[15]+crypted_string[16]*93+crypted_string[17]*93*93+crypted_string[18]*93*93*93+crypted_string[19]*93*93*93*93
print('\n')
print(binascii.hexlify(n))
print(binascii.hexlify(crypted_string))
print(hex(a1)+' '+hex(a2)+' '+hex(a3)+' '+hex(a4))
#print (format(a1, '04X')+format(a2, '04X')+format(a3, '04X')+format(a4, '04X'))
print(binascii.hexlify(struct.pack("<L", a1))+binascii.hexlify(struct.pack("<L", a2))+binascii.hexlify(struct.pack("<L", a3))+binascii.hexlify(struct.pack("<L", a4)))
k=20
passcode = bytearray(p)
for i in (11, 17, 23, 29):
    passcode[i] = crypted_string[k]
    k = k+1
# for j in range(len(p)):
#     print(hex(p[j]), end=' ')
print (binascii.hexlify(bytearray(p)))
print (binascii.hexlify(bytearray(passcode)))
#encobj = AES.new(key,mode,iv)

