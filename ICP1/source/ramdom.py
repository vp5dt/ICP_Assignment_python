import random

numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

randomNum = random.choice(numList)
print("Random Number: ", randomNum)

temp = 1

while temp == 1:

    inputNumber = int(input('Please enter your number: '))
    if inputNumber >= randomNum:
        if inputNumber == randomNum:
                                print("Your guess it CORRECT !!")
                                break
        else:
            print("Your number is GREATER than the random number")
            temp = 1
    else:
        print("Your number is LESS than the random number")
        temp = 1
