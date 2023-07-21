'''#Choice 1: Sum Tuples
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
print("Tuple 2 is:" + str(tup2))'''

def sumTuple():
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

#Choice 2: Export JSON
import json
def writeJson(dictionary, filename):
  try:
    with open(filename, 'w') as file:
      json_str = json.dunps(dictionary, indent = 4)
      file.write(json_str)
    print(f"Dictionary successfully written to '{filename} as Json.")
  except Exception as e:
    print(f"Error while writing to Json file: {e}")

person = {
  "name" : "Bilal",
  "Course" : "FCS",
  "Cycle" : "46"  
}


#Choice 3: Import JSON
'''def formatJson(data, indent=0):
    if isinstance(data, dict):
        return '{' + ','.join([f'{" " * (indent + 4)}"{key}": {format_json(value, indent + 4)}' for key, value in data.items()]) + f'{" " * indent}}}'
    elif isinstance(data, list):
        return '[' + ','.join([f'{" " * (indent + 4)}{format_json(item, indent + 4)}' for item in data]) + f'{" " * indent}]'
    elif isinstance(data, str):
        return f'"{data}"'
    else:
        return str(data)

def writeDictToJson(dictionary, filename):
    try:
        with open(filename, 'w') as file:
            # Convert the dictionary to a JSON-formatted string
            json_str = format_json(dictionary, indent=0)
            # Write the JSON string to the file
            file.write(json_str)
        print(f"Dictionary successfully written to '{filename}' as JSON.")
    except Exception as e:
        print(f"Error while writing to JSON file: {e}")

# Example dictionary
person = {
  "name" : "Bilal",
  "Course" : "FCS",
  "Cycle" : "46"  
}

filename = "output.json"
writeDictToJson(data, indent=0)'''


##########
#####Menu#
##########
def showMenu():
 fun = int(input('''Choose one of the following functions:
 1- Sum Tuples
 2- Export JSON
 3- Import JSON
 4- exit'''))
 if fun in range(1,5):
   if fun == 1:
    sumTuple()
    showMenu()
   elif fun == 2:
    writeJson(dictionary, filename)
    showMenu()
   elif fun == 3:
    formatJson(data, indent=0)
    writeDictToJson(dictionary, filename)
    showmenu()
   else:
    print("You've terminanted the programm.")
 else:
    print("Wrong entry. Please select from the menu.")
    showMenu()
    

showMenu()

    

  