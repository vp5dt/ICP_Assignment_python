# ICP3

print('Program to return the frequency of words')

# Getting Input from the User
sentence = input('Please enter your sentence: ')
# Iterating the input sentence words split by a space(" ")
sentWords = [str(word) for word in sentence.split(' ')]

# Creating a new List
finalList = {}

# Iterating the Input words in sorting order
for wrd in sorted(sentWords):
    # If word is already present in dictionary, then we are increasing the count by 1
    if wrd in finalList:
        finalList[wrd] = finalList[wrd]+1
    # Else, we are just setting the count as '1'
    else:
        finalList[wrd] = 1

# Printing Final List
print("Output --> ",finalList)
