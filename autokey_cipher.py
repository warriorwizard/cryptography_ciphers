#4 AUTOKEY CIPHER
def encrypt():
  '''this function is to convert plain text in to cipher text''' 
  pt=input("enter the plain text=")
  pt_no=[]
  for i in pt:
    if ord(i)>=65 and ord(i)<=90:
      pt_no.append(ord(i)-65)
    else:
      pt_no.append(ord(i)-97)
  key=int(input("enter the key="))
  k_no=[]
  k_no.append(key)
  for i in range(len(pt_no)):
    k_no.append(0)
  for i in range(len(pt_no)):
    k_no[i+1]=pt_no[i]
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
  dt=""
  ct=encrypt()
  print("CIPHER TEXT=",ct)
  ct_no=[]
  for i in ct:
    if ord(i)>=65 and ord(i)<=90:
      ct_no.append(ord(i)-65)
    else:
      ct_no.append(ord(i)-97)
  #print(ct_no)
  key=int(input("Enter the key="))
  kno=[]
  kno.append(key)
  for i in range(len(ct_no)):
    kno.append(0)
  for i in range(1,len(ct_no)):
     kno[i]=ct_no[i-1]-kno[i-1]
  #print(kno)
  subs=[]
  for i in range(len(ct_no)):
    subs.append(ct_no[i]-kno[i])
  for i in range(len(subs)):
    if subs[i]<0:
      subs[i]+=26
  #print(subs)
  for i in range(len(subs)):
    dt+=chr(subs[i]+65)
  print("DECRYPTED TEXT=",dt)
  
decrypt()