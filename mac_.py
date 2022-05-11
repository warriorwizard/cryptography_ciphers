import os
import sys
import binascii

from cryptography.hazmat.primitives import cmac

from cryptography.hazmat.primitives.ciphers import algorithms

message = "message"
ctype="TripleDES"

if (len(sys.argv)>1):
	message=str(sys.argv[1])
if (len(sys.argv)>2):
	ctype=str(sys.argv[2])

message=message.encode()
key = os.urandom(32)

c = cmac.CMAC(algorithms.AES(key))

if (ctype=="AES"): 
  c = cmac.CMAC(algorithms.AES(key))
elif (ctype=="Camellia"): 
  c = cmac.CMAC(algorithms.Camellia(key))
elif (ctype=="TripleDES"): 
  key = os.urandom(16)
  c = cmac.CMAC(algorithms.TripleDES(key))
elif (ctype=="Blowfish"): 
  c = cmac.CMAC(algorithms.Blowfish(key))  
elif (ctype=="CAST5"): 
  key = os.urandom(16)
  c = cmac.CMAC(algorithms.CAST5(key))    
elif (ctype=="IDEA"): 
  key = os.urandom(16)
  c = cmac.CMAC(algorithms.IDEA(key))  
elif (ctype=="SEED"): 
  key = os.urandom(16)
  c = cmac.CMAC(algorithms.SEED(key)) 


c.update(message)

c_copy = c.copy() 

signature = c.finalize()

print (f"Message: {message.decode()}" )
print (f"Type: {ctype}" )
print (f"Key: {binascii.b2a_hex(key).decode()}")

print (f"CMAC signature: {binascii.b2a_hex(signature).decode()}")

try:
  rtn=c_copy.verify(signature)
  print ("Signature matches")
except:
  print ("Signature does not match")
