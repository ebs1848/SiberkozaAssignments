# Python has functions for creating, reading, updating, and deleting files.

# Open a file 
myFile_ebs =open('myfile_ebs.txt', 'w')

# Get some info
print('Name: ', myFile_ebs.name)
print('Is Closed: ', myFile_ebs.closed)
print('Opening Mode: ', myFile_ebs.mode)

# Writw to file
myFile_ebs.write('I love Software')
myFile_ebs.write(' and Machine Learning')
myFile_ebs.close()

# Apend to file
myFile_ebs =open('myfile_ebs.txt', 'a')
myFile_ebs.write(' I also interested in AI')
myFile_ebs.close()

# Read to file
myFile_ebs =open('myfile_ebs.txt', 'r')
text_ebs = myFile_ebs.read(100)
print(text_ebs)