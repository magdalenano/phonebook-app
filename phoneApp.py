#! python3
import time,collections,re

phoneNumberRegex=re.compile(r'\d{3\s\d{3}\s\d{3}')

numbers={}

def menu():
    print ("1. Show Phone Numbers")
    print ("2. Add a Phone Number")
    print ("3. Remove a Phone Number")
    print ("4. Look for a Phone Number by Name")
    print ("5. Look for a Name by Phone Number")
    print ("6. Change Existing Name for Existing Name")
    print ("7. Change Number for Existing Name")
    print ("8. Quit")
    print()

#sorts entries by name
orderednumbers=collections.OrderedDict(sorted(numbers.items()))

#shows the content of ordered phonebook
def present_numbers():
    print("Name:" + ("Phone Number:").rjust(39))
    for i in orderednumbers.keys():
        print(i + orderednumbers[i].rjust(40 - len(i)))

import time,collections

menu_choice=0
menu()

while True:
  time.sleep(1)
  while True:
    try:
      menu_choice=int(input("Enter a number(1-8): "))
      break
    except ValueError:
      print("Please provide a number")
  if menu_choice == 1:
        present_numbers()

  elif menu_choice == 2:
        print ("Add name and number")
        while True:
            name=input("Enter a new name: ")
            if not name.isalpha():
                print("Name can only consits of letters")
            elif name in orderednumbers.keys():
                print ("This name is already used in Phonebook. To distinguish them, please provide different name")
            else:
                break
        while True:
            num=input("Enter a new number: ")
            if len(num)!=9 and not num.isnumeric():
              print("This number is wrong.\nPlease provide a legit number")
            elif num in orderednumbers.values():
              print ("This number is already in the Phonebook")
            else:
                break
        orderednumbers[name]=num
        print ("New number was added")
        present_numbers()

  elif menu_choice == 3:
        print ("Remove name and number")
        name=input("Enter a name you want to remove: ")
        if name in orderednumbers:
            del orderednumbers[name]
            present_numbers()
        else:
            print ("{} was not found in the Phonebook".format(name))

  elif menu_choice == 4:
        print ("Look for a Phone Number by Name")
        name=input("Enter a name: ")
        if name in orderednumbers:
            print (name + "'s number: "+numbers[name])
        else:
            print ("%s was not found in the Phonebook"%(name))

  elif menu_choice == 5:
        print ("Look for a Name by a Phone Number")
        num=input("Enter a number: ")
        if num in orderednumbers.values():
            for key,value in orderednumbers.items():
                if num==value:
                   print (value, "is ",key,"'s number")
        else:
            print ("There is no such number in the database")

  elif menu_choice==6:
        print ("Change existing name to a new name")
        name=input("Enter a name you want to change:")
        newname=input("Enter a new name:")
        if newname==name:
            print ("Names are the same")
        elif newname in orderednumbers.keys():
            print("This name already exists in the Phonebook")
        else:
            orderednumbers[newname]=orderednumbers[name]
            del orderednumbers[name]
        present_numbers()

  elif menu_choice==7:
        print ("Change number for existing contact")
        num=input("Enter a number:")
        if num not in orderednumbers.values():
            print ("There is no number like {} in the Phonebook".format(num))
        newnum=input("Enter a new number:")
        for key,value in orderednumbers.items():
            if value==num:
                orderednumbers[key]=newnum
        present_numbers()
        
  elif menu_choice == 8 :
        print ("Do you really want to quit? (y/n)")
        ans=input()
        if ans == "y" or ans=="yes":
          break
        elif ans=="n" or ans =="no":
          continue
  else:
        print ("You must choose a number form 1 to 8")

