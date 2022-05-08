#8 RAIL FENCE CIPHER
def encrypt():
  pt=input("Enter the plain text=")
  u=""
  l=""
  ct=""
  for i in range(len(pt)):
    if pt[i]==" ":
      continue
    if i%2==0:
      u=u+pt[i]
    else:
      l=l+pt[i]
  ct=u+l
  return ct
def decrypt(): 
  ct=encrypt()
  e=""
  o=""
  print("CIPHER TEXT=",ct)
  mid=(len(ct)//2)+1
  e=ct[:mid]
  o=ct[mid:]
  p=0
  q=0
  dt=""
  for i in range(len(ct)):
    if(i%2==0):
      dt=dt+e[p]
      p=p+1
    else:
      dt=dt+o[q]
      q=q+1
  print("DECRYPTED TEXT=",dt)
decrypt()