# #exception handling is the precess of respoinding to unwanted and unexpected efnts when a comp program runs it deals 
# with these events to avoid the prgm or system crahsing and without this process, exceptions would disrupt normal 
#  operation of program


a = input("enter the number : ")
print(f"Multiplication table of {a} is :")

try:
 for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a) * i}")

except Exception as e:
  print("sorry some error occurred")

except ValueError:
  print("number entered is not integer")
print("end of code")