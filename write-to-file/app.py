# writing files with python
print('Starting the write process to the file....')
fw = open('first.txt', 'w')  # create a file with name first.txt
fw.write("This is my first sentence in writing files \n")  # write first sentence
fw.write("Delink is cool \n")

fw.close()



