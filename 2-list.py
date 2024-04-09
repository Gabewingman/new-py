#List
familyName = ["Gab","Gab","RM","Tess"]

#Assigning list Items
familyName[0] = "Harold"
familyName[2] = "Gale"

#List Append
familyName.append("Harold")

#List Insert
familyName.insert(0,"Harold")

#List Remove
familyName.remove("Gab")

#List Pop
#it will remove the last value on the list
familyName.pop()
#or
#delete the specified value
familyName.pop(0)

#List Delete
del familyName[0]

#Clearing a List
familyName.clear()

#Copying a List
x = familyName.copy()

#Combining List
favorites = ["Ham","Veggies","Hotdog"]
print(familyName + favorites)

#List Extend
familyName.extend(favorites)
print(familyName)

#List Reverse
familyName.reverse()

#List Sort
#normal sort
Alphabet = ["D","C","B","A"]
Alphabet.sort()
print(Alphabet)
#reverse sort
Alphabet = ["","C","B","A"]
Alphabet.sort(reverse=True)
print(Alphabet)

#Nested List
familyName = ["Gab","Gab","RM","Tess",["Ham","Veggies","Hotdog"]]

#Tuples is READ-ONLY (it uses parentheses, not brackets)
familyName = ("Gab","Gab","RM","Tess")

#Length
print(len(familyName))

#List Count
print(familyName.count("RM"))

#Print to play the terminal
print(familyName)
