def encrypt():
  pt=input("Enter the plain text:")
  k=int(input("enter the key:"))
  ct=""
  for i in pt:
    if ord(i)>=65 and ord(i)<=90:
      ct+=chr((((ord(i)-65)+k)%26)+65)
    else:
      ct+=chr((((ord(i)-97)+k)%26)+97)
  return ct
def decrypt():
  ct=encrypt()
  print("Cipher Text:",ct)
  k=int(input("enter the key:"))
  dt=""
  for i in ct:
    if ord(i)>=65 and ord(i)<=90:
      dt+=chr((((ord(i)-65)-k)%26)+65)
    else:
      dt+=chr((((ord(i)-97)-k)%26)+97)
  print("Decrypted Text:",dt)