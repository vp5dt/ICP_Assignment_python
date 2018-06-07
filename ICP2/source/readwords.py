# Read the file sample1.txt
infile = open('sample1.txt','r')

# Read the first line from the file
line = infile.readline()

# Read complete file till the END OF THE FILE
while line != "":
    length = 0
    # Here we are splitting the line based on the words and finding how many words in the line
    for xStr in line.split(" "):
        length += 1
    print("%s, %d\n" % (line.rstrip("\n"), length))

    # Read the next line
    line = infile.readline()