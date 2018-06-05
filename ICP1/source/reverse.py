# ICP1

print('Program to Reverse the Name')

# INPUTS
firstName = input('Enter First Name: ')
lastName = input('Enter Last Name: ')

fName = str(firstName)
lName = str(lastName)

# Concatenating them
fullName = fName+" "+lName

print('OUTPUT')

print(fullName[::-1])