# Choice 1: Count Digits
def countDigits(num):
  if num < 10:
    return(1)
  else:
    return(1 + countDigits(num//10))
num = int(input("Enter an integer:"))
print(countDigits(num))  


# Choice 2: Find max
def findMax():
  for i in range(len(list)):
    if list[i] > list[i+1]:
      
#test commit from phone
      