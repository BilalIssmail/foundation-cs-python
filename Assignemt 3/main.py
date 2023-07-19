##############
#Assignment 3#
##############

#Choice 1: Sum Tuples
len1 = int(input("len1:"))
lst1 = []
for i in range(0,len1):
  int1 = int(input("enter integer to list 1 :"))
  lst1.append(int1)
  tup1 = tuple(lst1)
print("Tuple 1 is:" + str(tup1))
len2 = int(input("len2:"))
lst2 = []
for i in range(0,len2):
  int2 = int(input("enter integer to list 2 :"))
  lst2.append(int2)
  tup2 = tuple(lst2)
print("Tuple 2 is:" + str(tup2))


def sumTuple():
  if len(lst1) >= len(lst2):
    for i in range(len(lst2)):
      lst1[i] = lst2[i] + lst1[i]
      tup = tuple(lst1)
    print("Output tuple is:" + str(tup))
  else:
    for i in range(len(lst1)):
      lst2[i] = lst2[i] + lst1[i]
      tup = tuple(lst2)
    print("Output tuple is:" + str(tup))
sumTuple()
