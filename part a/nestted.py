age = int(input("Enter Age: "))
marks = float(input("Enter Marks: "))

# Voting Eligibility
if age >= 18:
    print("Eligible for Voting")

else:
    print("Not Eligible for Voting")

# Scholarship Eligibility
if marks >= 85:
    if age <= 25:
        print("Eligible for Scholarship")
    else:
        print("Not Eligible for Scholarship")
else:
    print("Not Eligible for Scholarship")
