import os
print(os.getcwd())
# ReOpen the file
input_file1 = open("C:/Users/balan/OneDrive/Documents/Malini/Python/Training Practice/intro.txt","r")

# While true enter into an infinite loop (we handle it by a break)
while True:
    curr_line = input_file1.readline() # Read line by line, to variable current line
    if not curr_line:
        break                          # Break if there is no line to read

    if curr_line.strip() != '':
        print(curr_line.strip())                   # Use .strip() to print without blank spaces

# Close the File stream handler
input_file1.close()

# 2. what is r+, w+ modes in read/write files?
# r+ and w+ can be used to both read and write files except that w+ deletes the content of the file if it exists and creates a new file if it doesn't exist.
