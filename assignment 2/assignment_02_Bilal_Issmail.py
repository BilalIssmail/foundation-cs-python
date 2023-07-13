def displayMenu():
  choice = int(input("""Choose:
  1- Count Digits
  2- Find Maximum
  3- Exit"""))
  if choice == 1:
    def countDigits(num):
     if num < 10:
       return(1)
     else:
       return(1 + countDigits(num//10))
    num = int(input("Enter an integer:"))
    print(countDigits(num))
  elif choice == 2:
    list = []
    n = int(input("Enter an integer to add to the list or press zero to end list and find the maximum:"))
    while  n != 0:
      list.append(n)
      n = int(input("Enter an integer to add to the list or press zero to end list and find the maximum:"))
    else:
      print("The integers you've entered are "+ str(list))

    def findMax(list):
     if len(list) > 1:
      if list[0] > list[1]:
       del(list[1])
      else:
       del(list[0])
      findMax(list)
     else:
      print("The max integer is " + str(list) )
    findMax(list)
  else:
   print("error")
displayMenu()