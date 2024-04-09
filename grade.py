firstGrade = float(input("Grade in Math: "))
secondGrade = float(input("Grade in Science: "))
thirdGrade = float(input("Grade in English: "))

Average = (firstGrade + secondGrade + thirdGrade) / 3

if Average > 100 or Average <= 50:
    print("Invalid Grade")
elif Average >= 98:
    print("With Highest Honor")
elif Average >= 95:
    print("With High Honors")
elif Average >= 90:
    print("With Honors")
elif Average >= 75:
    print("Passed")
elif Average >= 74:
    print("Failed")
else:
    print("No Grade")

print("Average: " + str(Average))