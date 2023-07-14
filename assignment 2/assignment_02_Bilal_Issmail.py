# Defining display menu main function from which other functions can be called
def displayMenu():
  choice = int(input("""Choose:
  1- Count Digits
  2- Find Maximum
  3-Count Tags
  4- Exit"""))
# Choice 1: Count Digits
  if choice == 1:
    def countDigits(num):
     if num < 10:
       return(1)
     else:
       return(1 + countDigits(num//10))
    num = int(input("Enter an integer:"))
    print(countDigits(num))
    displayMenu()
# Choice 2: Find max
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
    displayMenu()
# Choice 3: Count Tags
  elif choice == 3:
    def countTag ():
      cd = input("Enter your html code:")
      tg = ("<"+input("Enter the tag you want to count:")+">")
      count = 0
      if tg in cd:
        count+=1
        del (tg)
        return (cd)
        countTag()
      else:
        print("The number of occurences of "+ str(tg) + "in your code is: " + str(count))
    countTag()
    displayMenu()
# Choice 4: Exit
  elif choice == 4:
    print("You've terminated the program.")
# Wrong Choice
  else:
   print("Wrong choice. Please choose from inside the menu.")
   displayMenu()
displayMenu()