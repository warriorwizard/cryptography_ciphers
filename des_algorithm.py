# DES
# !pip install pyDes
import pyDes
 
def encrypt():
  data = input("Enter the text : ")
  k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5) 
  d = k.encrypt(data) 
  return d
def decrypt():
  d=encrypt()
  print(f"Encrypted:  {d}" )
  k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5) 
  print(f"Decrypted: {k.decrypt(d)}")
decrypt()