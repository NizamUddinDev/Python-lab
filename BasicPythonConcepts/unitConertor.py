weight=int(input("Enter weight of item: "))
unit=input("Kilograms or Pounds?? Kg or L: ")

if unit=="Kg":
    weight=weight*2.205
    unit="lbs"
    print(f"Your weight is: {round(weight, 2)} {unit}")
elif unit=="L":
    weight=weight/2.205
    unit="kgs"
    print(f"Your weight is: {round(weight, 2)} {unit}")
else:
    print(f"{unit} is not valid")