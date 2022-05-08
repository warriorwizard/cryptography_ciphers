#3 POLY SUBSTITUTION CIPHER(ONE TIME PAD)
def encrypt():
  '''this function is to convert plain text in to cipher text''' 
  pt=input("enter the plain text=")
  pt_no=[]
  for i in pt:
    if ord(i)>=65 and ord(i)<=90:
      pt_no.append(ord(i)-65)
    else:
      pt_no.append(ord(i)-97)
  key=input("enter the key=")
  k_no=[]
  for i in key:
    if ord(i)>=65 and ord(i)<=90:
      k_no.append(ord(i)-65)
    else:
      k_no.append(ord(i)-97)
  addition=[]
  for i in range(len(pt_no)):
      addition.append(pt_no[i]+k_no[i])
  for i in range(len(addition)):
    if addition[i]>25:
      addition[i]=addition[i]-26
  ct=""
  for i in range(len(addition)):
    ct+=chr(addition[i]+65)
  return ct
def decrypt():
  ct=encrypt()
  print("CIPHER TEXT=",ct)
  ct_no=[]
  dt=""
  for i in ct:
    if ord(i)>=65 and ord(i)<=90:
      ct_no.append(ord(i)-65)
    else:
      ct_no.append(ord(i)-97)
  key=input("enter the key=")
  k_no=[]
  for i in key:
    if ord(i)>=65 and ord(i)<=90:
      k_no.append(ord(i)-65)
    else:
      k_no.append(ord(i)-97)
  substraction=[]
  for i in range(len(ct_no)):
    substraction.append(ct_no[i]-k_no[i])
  for i in range(len(substraction)):
    if substraction[i]<0:
      substraction[i]+=26
  for i in range(len(substraction)):
    dt+=chr(substraction[i]+65)
  print("DECRYPTED TEXT=",dt)
 
decrypt()