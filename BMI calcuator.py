height=float(input("Enter your height in cm:"))
weight=float(input("Enter your weight in kg:"))

BMI=weight/(height/100)**2

print("your BMI is:",BMI)

if BMI<=18.4:
    print("you are underweight")
elif BMI<=24.9:
    print("you are healthy")
elif BMI<=29.9:
    print("you are over weight")
elif BMI<=39.9:
    print("you are severly over weight")
elif BMI<=39.9:
    print("you are abese")
else:
    print("you are severly obese")
