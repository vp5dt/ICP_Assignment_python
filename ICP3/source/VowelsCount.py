# ICP3
# Vowels set
vowels = {'a', 'e', 'i', 'o', 'u'}

# Getting Input from the User
sentence = input('Enter a sentence: ')

# Counter
count = 0


# Iterating each word in the given sentence
for word in sentence:
    # Checking if the word is a part of vowels set
    if word in vowels:
        count = count + 1

print("Number of Vowels ",count)
