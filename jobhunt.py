# Define the required skills
required_skills = [
    "Self Motivation",
    "Ability to work independently or as part of a team",
    "Polite and courteous",
    "Deadline-oriented"
]

# Gather input from the user
name = input("Name: ")
age = int(input("How old are you? Please type: "))
experience = input("Do you have experience? Please type True or False: ").lower() == "true"
graduate = input("Did you graduate? Please type True or False: ").lower() == "true"

# Check qualifications
if age >= 18 or experience or graduate:
    # Check if all required skills are present
    if all(skill in required_skills for skill in input("List your skills (comma-separated): ").split(',')):
        print("You are qualified for the role.")
    else:
        print("Please send me your CV.")
elif age <= 15 and not experience and not graduate:
    print("Sorry, you are not qualified for the role. Thanks for applying. We recommend gaining more experience.")
else:
    print("Thank you for applying.")
