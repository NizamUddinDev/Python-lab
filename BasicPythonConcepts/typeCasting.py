#Type casting: (Converting from one data type to another)
age = 23 
cgpa=3.3
name="Ali"
is_Employed=True
#Showing variables data type
print("Showing variables data type")
print(type(age))
print(type(cgpa))
print(type(name))
print(type(is_Employed))

#Typecasting
print("\n Converting data from float to integer: ")
cgpa=int(cgpa)
print(cgpa)

print("\n Converting data from string to bool: ")
name=bool(name) #gives True if string is not empty else it gives False
print(name)

print("\n Converting data from float to bool: ")
cgpa=bool(cgpa) #gives False only when value is 0 else True and same for integer
print(cgpa)

print("\n Converting data from bool to integer: ")
is_Employed=int(is_Employed)
print(is_Employed) #gives result 1 if True else 0 for False and for float same just add .0
