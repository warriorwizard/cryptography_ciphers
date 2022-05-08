#5 Multiplicative Cipher
def encrypt():
  pt=input("enter the plain text=")
  pt_no=[]
  for i in pt:
    if ord(i)>=65 and ord(i)<=90:
      pt_no.append(ord(i)-65)
    else:
      pt_no.append(ord(i)-97)
  key=int(input("enter the key="))
  for i in range(len(pt_no)):
    pt_no[i]=(pt_no[i]*key)%26
  ct=""
  for i in pt_no:
    ct+=chr(i+65)
  return ct
def decrypt():
  ct=encrypt()
  print("CIPHER TEXT=",ct)
  k2=int(input("Enter the inverse of key k1="))
  ct_no=[]
  for i in ct:
    if ord(i)>=65 and ord(i)<=90:
      ct_no.append(ord(i)-65)
    else:
      ct_no.append(ord(i)-97)
  dt_no=[]
  for i in ct_no:
    dt_no.append((i*k2)%26)
  dt=""
  for i in dt_no:
    dt+=chr(i+65)
  print("DECRYPTED TEXT=",dt)

decrypt()