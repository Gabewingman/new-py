#if else statement in python. So much to know about this, very useful and powerfull.

name = "Gab"
grade = 89
honor = True

if name == "Gab" and grade >=90 and honor == True:
    print("You passed the test. Good job.")
else:
    print("Sorry. Try again next time.")

#if elif else statement (if-else-if) is used for 3 or more conditions.
age = int(input("Enter your Age: ")) #Used this statement when you want to run your python code into the terminal.
if age >= 18:
    print("Legal Age.")
elif age >= 13:
    print("Teenager, passed.")
else:
    print("Too Young.")

print("Thank you for using our program")

#Collection conditional statements
bag = ["ballpen","pencil","notebook","books"] #Using list in if else statement

if "gun" in bag:
    print("Bawal ka pumasok")
else:
    print("Go ahead!")