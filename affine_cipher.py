# 6 AFFINE CIPHER
def encrypt():
    pt = input("Enter the plain text=")
    pt_no = []
    for i in pt:
        if ord(i) >= 65 and ord(i) <= 90:
            pt_no.append(ord(i)-65)
        if ord(i) >= 97 and ord(i) <= 122:
            pt_no.append(ord(i)-97)
    k1 = int(input("Enter the key,k1="))
    k2 = int(input("Enter the key,k2="))
    k3 = int(input("Enter the inverse of key k1="))
    ct_no = []
    for i in pt_no:
        ct_no.append(((i*k1)+k2) % 26)
    ct = ""
    for i in ct_no:
        ct += chr(i+65)
    return ct


def decrypt():
    ct = encrypt()
    print("CIPHER TEXT=", ct)
    k2 = int(input("Enter the key,k2="))
    k3 = int(input("Enter the inverse of key k1="))
    ct_no = []
    for i in ct:
        if ord(i) >= 65 and ord(i) <= 90:
            ct_no.append(ord(i)-65)
        else:
            ct_no.append(ord(i)-97)
    dt_no = []
    for i in ct_no:
        dt_no.append((i-k2)*k3)
    f=[]
    for i in dt_no:
        if i < 0:
            i = i+26
            i = i % 26
            f.append(i)
        else:
            i = i % 26
            f.append(i)
    dt = ""
    for i in f:
        dt += chr(i+65)
    print("DECRYPTED TEXT=", dt)
	
decrypt()