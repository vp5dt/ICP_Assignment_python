print('Program to return the maximum length of the input words')

# Getting Inputs from the User
wordsList = input('Please enter your words list separated by a comma: ')
# Iterating the input by and forming
wordsList = [str(word) for word in wordsList.split(',')]
print(wordsList)

# Creating a new List which should contain list of Tuples
lenWordList = []

# Iterating the Input list
for wrd in wordsList:
    # Adding tuples (length of word, word) to the New List
    lenWordList.append(tuple((len(wrd), wrd)))

print(sorted(lenWordList))

# Sorting the final List for the 1st Key and setting reverse as TRUE
lenWordList = sorted(lenWordList, key= lambda x:x[0],reverse=True)

# Return first item which is the maximum length tuple.
print(lenWordList[0])
