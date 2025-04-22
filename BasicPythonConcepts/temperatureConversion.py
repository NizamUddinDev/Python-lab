unit=input("Is the temperature Celsius or Fahrenheit? (C/F):")
tempertaure=float(input("Enter temperature: "))

if unit=="C":
    result=round((tempertaure*9)/5+32, 3)
    print(f"The temperature in Farhenheit is: {result}")
    
elif unit=="F":
    result=round(((tempertaure-32)*5)/9, 3)
    print(f"The temperature in centigrade is: {result}")