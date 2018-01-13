# writing files with python
print('-----------------------------')
print('Writing to file in python....')
print('-----------------------------')

# input to print
inputText = input('What do you want to write to the file? ')
fw = open('first.txt', 'w')  # create a file with name first.txt
fw.write(inputText + '\n')  # write first sentence
fw.write('\n<<<Delink is cool>>\n')

fw.close()

# reading files in python
fr = open('first.txt', 'r')  # open the file
readText = fr.read()

print(readText)  # print the files content
fr.close()
