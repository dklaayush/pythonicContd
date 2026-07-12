import random
import string 



def encode(givenMsg):
  random_alphs1=random.choices(string.ascii_letters,k=3)
  random_alphs2=random.choices(string.ascii_letters,k=3)
  msgList=list(givenMsg)
  msgList.append(msgList.pop(0))
  combinedList=[*random_alphs1,*msgList,*random_alphs2]
  print("".join(combinedList))

  


def decode(toBeDecoded):
  decodeList=list(toBeDecoded)
  del decodeList[:3]
  del decodeList[-3:]
  
  decodeList.insert(0,decodeList.pop())
  print("".join(decodeList))
  


enteredMsg=input("press 1 for encoding you secret message  and 2 for decoding the message :")
enteredMsgInt=int(enteredMsg)

if(enteredMsgInt==1):
  print("u have chosen encoding of your message")
  givenMsg=input("enter your word to be encoded:")
  encode(givenMsg)
  

elif(enteredMsgInt==2):
  print("decoding have been chosen")
  
  toBeDecoded=input("enter the msg to be decoded :")
  decode(toBeDecoded) 

else:
  print("Error in number , enter correctly")





