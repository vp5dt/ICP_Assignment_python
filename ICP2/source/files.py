# Reading the text file
infile = open('sample.txt','r')
length = 0

# Reading the 1st line of the file
line = infile.readline()

# We are opening the file to write the output, Here w+ helps to create the output file if it doesnt exist
f = open("output.txt","w+")

# Reading the file until we Reach END OF THE FILE.
while line != "":
    # Find length of file
    length = len(line)
    # rstrip will help to eliminate new line character
    f.write("%s, %d\n" % (line.rstrip('\n'),length))

    # Read the next line from the file infile
    line = infile.readline()
