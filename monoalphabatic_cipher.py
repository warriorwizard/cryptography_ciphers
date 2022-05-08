dic={
  'A':'k',
  'B':'l',
  'C':'m',
  'D':'o',
  'E':'n',
  'F':'p',
  'G':'t',
  'H':'s',
  'I':'q',
  'J':'r',
  'K':'a',
  'L':'u',
  'M':'v',
  'N':'w',
  'O':'z',
  'P':'b',
  'Q':'c',
  'R':'d',
  'S':'e',
  'T':'f',
  'U':'x',
  'V':'y',
  'W':'j',
  'X':'g',
  'Y':'i',
  'Z':'h'
  }

def encrypt():
  pt=input("Enter the Plain Text=")
  ct=""
  for i in pt:
      ct=ct+dic[i]
  return ct

def decrypt():
  ct=encrypt()
  print("CIPHER TEXT=",ct)
  val=list(dic.values())
  key=list(dic.keys())
  di=dict(zip(val,key))
  dt=""
  for i in ct:
    dt=dt+di[i]
  print("DECRYPTED TEXT=",dt)
  
 decrypt()